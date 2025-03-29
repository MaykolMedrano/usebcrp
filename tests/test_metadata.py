from usebcrp.metadata import Metadata

text_inf = "pesca"
cache = True

metadata = Metadata(text_inf=text_inf)

"""
Test for Metadata class

Note: Sometimes we get errors, probably because a request 
is being made to a URL and there are time slots that 
are updated.

"""

# def test_metadata_browse():
#     result = metadata._browse(cache=cache)
#     assert result is not None

def test_metadata_load_bcrp_metadata():
    result = metadata._load_bcrp_metadata()
    assert result is not None