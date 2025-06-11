import asyncio

from src.utils.cache.valkey import get_cache, set_cache

endpoint = "team/frc5507"
test_json = {
    "address": None,
    "city": "San Francisco",
    "country": "USA",
    "gmaps_place_id": None,
    "gmaps_url": None,
    "key": "frc5507",
    "lat": None,
    "lng": None,
    "location_name": None,
    "motto": None,
    "name": "PG&E/Salesforce/Gene Haas Foundation/Sunset 29/Molex/Fabworks/Rivian/Cruise/Intuitive/Friends of Beakle&George Washington High School",  # noqa: E501
    "nickname": "Robotic Eagles",
    "postal_code": "94121",
    "rookie_year": 2015,
    "school_name": "George Washington High School",
    "state_prov": "California",
    "team_number": 5507,
    "website": "http://www.team5507.org/",
}


def test_cache():
    endpoint = "team/frc5507"

    asyncio.run(set_cache(test_json, endpoint, write_json=False))
    cached_json = asyncio.run(get_cache(endpoint, check_json=False))

    assert cached_json is not False, "Unexpected cache miss"
    assert type(cached_json) is dict, "Cached JSON should be a dictionary"

    for key in test_json.keys():
        assert test_json[key] == cached_json[key], (
            f"Mismatch for key {key}: {test_json[key]} != {cached_json[key]}"
        )
