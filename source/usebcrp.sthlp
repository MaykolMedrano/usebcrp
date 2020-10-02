{smcl}
{* *! version 1.0.0 8jan2020}{...}
{vieweralsosee "use" "help use"}{...}
{vieweralsosee "freduse" "help freduse"}{...}
{title:Title}

{p2colset 5 16 20 2}{...}
{p2col :{cmd:usebcrp} {hline 2}}Import data from the Peruvian Central Bank BCRP){p_end}
{p2colreset}{...}

{title:Syntax}

{p 8 16 2}
{cmd:usebcrp}
{it:series1} [... {it:series10}]
[{cmd:,}
{opt range(start_date end_date)}
{opt cache:path(string)}
{opt clear}
{opt v:erbose}
{opt sleep(seconds)}
]

{title:Description}

{pstd}
{cmd:usebcrp} imports data from the Peruvian Central Bank's statistical database.

{pstd}
The IDs for each time series can be located {browse "https://estadisticas.bcrp.gob.pe/estadisticas/series/index":here} (by category)

{pstd}By frequency:

{p 8 8 2} - {browse "https://estadisticas.bcrp.gob.pe/estadisticas/series/diarias":daily} (106 series){p_end}
{p 8 8 2} - {browse "https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales":monthly} (5736 series){p_end}
{p 8 8 2} - {browse "https://estadisticas.bcrp.gob.pe/estadisticas/series/trimestrales":quarterly} (2100 series){p_end}
{p 8 8 2} - {browse "https://estadisticas.bcrp.gob.pe/estadisticas/series/anuales":annually} (5357 series){p_end}

{pstd}
Start and end dates must be in Stata format. Examples:

{pstd}{inp:usebcrp PN01288PM PN01289PM, range(2013m1 2016m9)}{p_end}
{pstd}{inp:usebcrp PN03492MQ, range(2013q1 2016q4)}{p_end}
{pstd}{inp:usebcrp PD04658MD, clear range(1jan1999 31dec2002)}{p_end}
{pstd}{inp:usebcrp PM06069MA, clear range(2007 2009)}{p_end}


{title:Technical Notes}

{pstd}
It follows the API described at
{browse "https://estadisticas.bcrp.gob.pe/estadisticas/series/ayuda/api"}.

{pstd}
The command works perfectly in Windows 10, but if your computer is another version it is necessary to install {browse "https://curl.haxx.se":Curl}.

{title:Author}

{pstd}
Maykol Medrano, National University of San Antonio Abad of Cusco. {browse "mailto:maykolmedrano35@gmail.com":maykolmedrano35@gmail.com}
{p_end}

