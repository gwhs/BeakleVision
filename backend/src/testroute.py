from main import app
from pydantic import BaseModel
from json import dump # stdlib json > fastapi json

class Match(BaseModel):
    L1: int
    L2: int
    L3: int
    L4: int

def writedata(path: str, match: Match):
    with open(path, 'x') as file:
        dat = {
                "L1": match.L1,
                "L2": match.L2,
                "L3": match.L3,
                "L4": match.L4
                }
        dump(dat, file)

@app.post("/match")
def match(match: Match):
    writedata("DELETEME.json", match)
