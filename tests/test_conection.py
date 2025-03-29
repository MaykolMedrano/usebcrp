from usebcrp.conection import ConectionBCRP

cachepath = "cache_bcrp"
verbose = "True"
series=["PN38706PM", "PN38707PM"]
range="2013-1 2024-9"
sleep_sec = 1.0

ConexionBcrp = ConectionBCRP(series=series, range=range)

"""
Test the ConextionBCRP class
"""

def test_conectionbcrp_conectionapi():
    result = ConexionBcrp.conectionAPI(cachepath=cachepath, verbose=verbose, sleep_sec=sleep_sec)
    assert result is not None