from typing import TypedDict

from src.types.enums import EventType, MatchStatus, MatchType, MatchWinner


class TeamDict(TypedDict):
    """
    TypedDict that holds team specific information from TBA
    """
    team: int
    name: str
    rookie_year: int
    country: str | None
    state: str | None
    city: str | None
    district: str | None


class EventDict(TypedDict):
    """
    TypedDict that holds event specific information from TBA.
    """
    year: int
    key: str
    name: str
    country: str | None
    state: str | None
    city: str | None
    district: str | None
    start_date: str
    end_date: str
    time: int
    type: EventType
    week: int
    video: str | None


class BreakdownDict(TypedDict):
    """
    TypedDict that holds match breakdown information that comes with each match 
    download from TBA. Each match has a match breakdown.
    
    The breakdown is different for each season. For more info see the TBA API at 
    https://www.thebluealliance.com/apidocs/v3 and look at src.tba.breakdown to 
    see how the API values are converted into values here.
    """
    score: int | None
    no_foul_points: int | None
    foul_points: int | None
    auto_points: int | None
    teleop_points: int | None
    endgame_points: int | None
    endgame_1: int | None
    endgame_2: int | None
    endgame_3: int | None
    rp_1: bool | None
    rp_2: bool | None
    rp_3: bool | None
    tiebreaker: int | None
    comp_1: int | float | None
    comp_2: int | float | None
    comp_3: int | float | None
    comp_4: int | float | None
    comp_5: int | float | None
    comp_6: int | float | None
    comp_7: int | float | None
    comp_8: int | float | None
    comp_9: int | float | None
    comp_10: int | float | None
    comp_11: int | float | None
    comp_12: int | float | None
    comp_13: int | float | None
    comp_14: int | float | None
    comp_15: int | float | None
    comp_16: int | float | None
    comp_17: int | float | None
    comp_18: int | float | None


class MatchDict(TypedDict):
    """
    TypedDict that holds match results from TBA.
    """
    event: str
    key: str
    match_type: MatchType
    set_number: int
    match_number: int
    status: MatchStatus
    video: str | None
    red_1: int
    red_2: int
    red_3: int | None
    red_dq: str
    red_surrogate: str
    blue_1: int
    blue_2: int
    blue_3: int | None
    blue_dq: str
    blue_surrogate: str
    winner: MatchWinner | None
    time: int
    predicted_time: int | None
    red_score: int | None
    blue_score: int | None
    red_score_breakdown: BreakdownDict
    blue_score_breakdown: BreakdownDict


empty_breakdown: BreakdownDict = {
    "score": 0,
    "no_foul_points": None,
    "foul_points": None,
    "auto_points": None,
    "teleop_points": None,
    "endgame_points": None,
    "endgame_1": None,
    "endgame_2": None,
    "endgame_3": None,
    "rp_1": False,
    "rp_2": False,
    "rp_3": False,
    "tiebreaker": None,
    "comp_1": None,
    "comp_2": None,
    "comp_3": None,
    "comp_4": None,
    "comp_5": None,
    "comp_6": None,
    "comp_7": None,
    "comp_8": None,
    "comp_9": None,
    "comp_10": None,
    "comp_11": None,
    "comp_12": None,
    "comp_13": None,
    "comp_14": None,
    "comp_15": None,
    "comp_16": None,
    "comp_17": None,
    "comp_18": None,
}
