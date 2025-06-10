import asyncio

from src.tba.main import tba_api_call

endpoint = "team/frc5507"
test_json = {
    'address': None,
    'city': 'San Francisco',
    'country': 'USA',
    'gmaps_place_id': None,
    'gmaps_url': None,
    'key': 'frc5507',
    'lat': None,
    'lng': None,
    'location_name': None,
    'motto': None,
    'name': 'PG&E/Salesforce/Gene Haas Foundation/Sunset 29/Molex/Fabworks/Rivian/Cruise/Intuitive/Friends of Beakle&George Washington High School',
    'nickname': 'Robotic Eagles',
    'postal_code': '94121',
    'rookie_year': 2015,
    'school_name': 'George Washington High School',
    'state_prov': 'California',
    'team_number': 5507,
    'website': 'http://www.team5507.org/'
}


def test_teams_api_call():

    tba_json, _ = asyncio.run(tba_api_call(endpoint))

    assert type(tba_json) is dict, "TBA API call should return a dictionary"

    for key in test_json.keys():
        assert key in tba_json, f"Key {key} not found in TBA JSON"
        assert test_json[key] == tba_json[key], f"Mismatch for key {key}: {test_json[key]} != {tba_json[key]}"


def test_teams_api_cached():

    tba_json, etag = asyncio.run(tba_api_call(endpoint))

    assert type(tba_json) is dict, "TBA API call should return a dictionary"

    cached_json, _ = asyncio.run(tba_api_call(endpoint, etag=etag))

    assert cached_json is not False, "Unexpected cache miss"
    assert type(cached_json) is dict, "Cached JSON should be a dictionary"

    for key in test_json.keys():
        assert key in cached_json, f"Key {key} not found in cached JSON"
        assert test_json[key] == cached_json[key], f"Mismatch for key {key}: {test_json[key]} != {cached_json[key]}"
