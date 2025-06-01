from enum import StrEnum

class MatchWinner(StrEnum):
    Red = "red"
    Blue = "blue"
    Tie = "tie"

class MatchStatus(StrEnum):
    Upcoming = "Upcoming"
    Completed = "Completed"

class MatchType(StrEnum):
    Invalid = "Invalid"
    Quals = "qm"
    Eigth = "ef"
    Quarter = "qf"
    Semi = "Semi"
    Final = "f"

class EventStatus(StrEnum):
    Invalid = "Invalid"
    Upcoming = "Upcoming"
    Ongoing = "Ongoing"
    Completed = "Completed"

class EventType(StrEnum):
    Invalid = "Invalid"
    Regional = "Regional"
    District = "District"
    District_cmp = "District_cmp"
    Chamos_div = "Chamos_div"
    Einstein = "Einstein"
    Offseason = "Offseason"
