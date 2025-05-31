from main import app
from pydantic import BaseModel
from json import dump # stdlib json > fastapi json
from types.match import Match

def writedata(path: str, match: Match):
    with open(path, 'x') as file:
        dat = {
                "AL1": match.AL1,
                "AL2": match.AL2,
                "AL3": match.AL3,
                "AL4": match.AL4
                }
        dump(dat, file)

@app.post("/match")
def match(match: Match):
    writedata("DELETEME.json", match)
