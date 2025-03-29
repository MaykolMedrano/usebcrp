from usebcrp.utils import ParseDates

date_str = "2013-1 2024-9"

parsedates = ParseDates(date_str=date_str)

def test_parsedates_parse_spanish_date():
    result = parsedates._parse_spanish_date()
    assert result is not None