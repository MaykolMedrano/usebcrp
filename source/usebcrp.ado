capture program drop usebcrp
program define usebcrp
	syntax namelist(name=series max=10), [ ///
		RANGE(string) ///
		CACHEpath(string) ///
		FORMAT(string) ///
		CLEAR ///
		Verbose ///
		SLEEP(real 1.0) ///
		]
	
	* Parse series
	gettoken serie1 _ : series
	loc freq = substr("`serie1'", length("`serie1'"), 1)
	loc freq = "t" + lower("`freq'")

	foreach serie of local series {
		loc _ = substr("`serie'", length("`serie'"), 1)
		loc _ = "t" + lower("`_'")
		_assert "`freq'" == "`_'", ///
			msg("All series must have the same freq")
	}

	* Parse date range
	if ("`freq'" == "ta") loc freq ty
	assert inlist("`freq'", "td", "tm", "tq", "ty")
	if ("`freq'" == "td") loc fmt "%tdCCYY-NN-DD"
	if ("`freq'" == "tm") loc fmt "%tmCCYY!-nn"
	if ("`freq'" == "tq") loc fmt %tqCCYY-q
	if ("`freq'" == "ty") loc fmt "%ty"

	* Parse other options
	loc clear = ("`clear'" != "")
	loc verbose = ("`verbose'" != "")
	loc sleep = `sleep' * 1000 // msec
	if ("`format'" == "") loc format %8.4f

	* Clear data (or fail trying)
	if (`c(changed)' & "`clear'"=="") error 4
	clear

	* Build API URL
	mata: st_local("url_series", invtokens(tokens("`series'"), "-"))
	loc baseurl "https://estadisticas.bcrp.gob.pe/estadisticas/series/api"
	if ("`range'" != "") {
		loc fun `freq'
		if ("`freq'" == "ty") loc fun // No function for years
		gettoken t0 t1 : range
		loc t0 = string(`fun'(`t0'), "`fmt'")
		loc t1 = string(`fun'(`t1'), "`fmt'")
		loc suffix "`t0'/`t1'"
	}
	loc url "`baseurl'/`url_series'/txt/`suffix'"
	if (`verbose') di as text "[URL] `url'"
	if (`verbose') di as text "[FREQ] `freq'"

	loc download 1
	if ("`cachepath'" != "") {
		mata: st_local("hash", strofreal(hash1("`url'"), "%30.0g"))
		loc hash "bcrp-`hash'.raw"
		loc fn "`cachepath'/`hash'"
		cap findfile "`hash'", path("`cachepath'")
		
		if (c(rc)==0) {
			loc download 0
			if (`verbose') di as text " - found in cache: `hash'"
		}
	}

	if (`download') {
		if ("`cachepath'" != "") {
			loc fn "`cachepath'/`hash'"
		}
		else {
			tempfile fn
		}
		if (`verbose') di as text " - downloading series"
		winexec curl  -o "`fn'" --request GET "`url'"
		// Avoid overloading their server
		sleep `sleep'
	}

	// Load CSV
	qui import delimited using "`fn'", ///
		delim("\t") varnames(nonames) case(preserve) asdouble
	qui drop if missing(v1) // empty row added at the end

	// Time variable
	qui {
		if ("`freq'" == "tm") {
			replace v1 = subinstr(v1, "Ene", "Jan", .)
			replace v1 = subinstr(v1, "Abr", "Apr", .)
			replace v1 = subinstr(v1, "Ago", "Aug", .)
			replace v1 = subinstr(v1, "Set", "Sep", .)
			replace v1 = subinstr(v1, "Dic", "Dec", .)
			gen int time = monthly(v1, "MY")
		}
		else if ("`freq'" == "tq") {
			gen byte q = real(substr(v1, 2, 1))
			gen int y = 2000 + real(substr(v1, 4, .))
			replace y = y - 100 if y > 2050
			gen int time = yq(y, q)
			drop y q
		}
		else if ("`freq'" == "td") {
			replace v1 = subinstr(v1, "Ene", "Jan", .)
			replace v1 = subinstr(v1, "Abr", "Apr", .)
			replace v1 = subinstr(v1, "Ago", "Aug", .)
			replace v1 = subinstr(v1, "Set", "Sep", .)
			replace v1 = subinstr(v1, "Dic", "Dec", .)
			gen long time = date(v1, "DM20Y")
			replace time = date(v1, "DM19Y") if yofd(time) > 2050
		}
		else if ("`freq'" == "ty") {
			gen time = real(v1)
		}
	}

	format %`freq' time
	assert !missing(time) if _n > 1
	drop v1
	order time
	
	// Rename and label variables
	qui ds time, not
	loc vars `r(varlist)'
	loc backup_series `series'
	foreach var of local vars {
		loc label = `var'[1]
		loc label = subinstr("`label'", "&aacute;", "a", .)
		loc label = subinstr("`label'", "&eacute;", "e", .)
		loc label = subinstr("`label'", "&iacute;", "i", .)
		loc label = subinstr("`label'", "&oacute;", "o", .)
		loc label = subinstr("`label'", "&uacute;", "u", .)
		la var `var' "`label'"
		gettoken s series : series
		rename `var' `s'
	}
	qui drop in 1
	qui destring `backup_series', replace
	format `format' `backup_series'
	note: "URL: `url'"
end
