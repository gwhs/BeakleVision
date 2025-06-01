from typing import List, TypedDict

from enums import MatchType, MatchWinner


class TeamDict(TypedDict):
    Address: str | None
    City: str | None
    Country: str | None
    Gmaps_place_id: str | None
    Gmaps_url: str | None
    Key: str | None
    lat: float | None
    lng: float | None
    Location_name: str
    Motto: str | None
    name: str | None  # this is the name with all the sponsors
    Nickname: str | None
    Postal_code: str | None  # only a thing for US teams
    Rookie_year: int | None
    School_name: str | None
    State_prov: (
        str | None
    )  # also basically only US teams although maybe it would be the providence of a canadian team
    Team_number: int | None
    website: str | None


class Webcast(TypedDict):
    channel: str | None
    type: str | None


class EventDict(TypedDict):
    Address: str | None
    City: str | None
    Country: str | None
    district: (
        str | None
    )  # prob a string but couldn't find an event where it wasn't null
    Division_keys: (
        List[str] | None
    )  # also couldn't find places where it isn't blank but prob list of strings
    End_date: str | None
    Event_code: str | None
    Event_type: int | None
    Event_type_string: str | None
    First_event_code: str | None
    First_event_id: (
        str | int
    )  # I would say int but seeing TBA's record of making things that should be ints strings I Don't trust them
    Gmaps_place_id: str | None
    Gmaps_url: str | None
    Key: str | None  # the TBA one
    lat: float | None
    lng: float | None
    Location_name: str | None
    Name: str | None
    Parent_event_key: str | None
    Playoff_type: int | None
    Playoff_type_string: str | None
    Postal_code: str | None
    Short_name: str | None
    Start_date: str | None
    State_prov: str | None
    Timezone: str | None
    Webcasts: List[Webcast] | None
    Website: str | None
    Week: int | None
    Year: int | None


class TeamKeys(TypedDict):
    T1: str | None
    T2: str | None
    T3: str | None


class AllianceDict(TypedDict):
    Dq_team_keys: List[str] | None
    score: int | None
    surrogate_team_keys: List[str] | None
    Team_keys: TeamKeys | None


class MatchDict(TypedDict):
    Alliances: List[AllianceDict] | None
    winner: MatchWinner
    Match_num: int | None
    Comp_level: MatchType
