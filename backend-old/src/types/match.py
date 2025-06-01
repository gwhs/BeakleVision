from pydantic import BaseModel

class Match(BaseModel):
    # Key:
    # A = Auton
    # T = Teleop
    # M = Miss
    # Alg = Algae
    # P = Processor
    # B = Barge
    AL1: int
    AL1M: int
    AL2: int
    AL2M: int
    AL3: int
    AL3M: int
    AL4: int 
    AL4M: int 
    TL1: int
    TL1M: int
    TL2: int
    TL2M: int
    TL3: int
    TL3M: int
    TL4: int
    TL4M: int
    AlgB: int
    AlgBM: int
    AlgP: int
    AlgPM: int
    TeamNum: int
    Fouls: int
    Defense: bool
    Speed: int # should be 1 to 5 inclusive
