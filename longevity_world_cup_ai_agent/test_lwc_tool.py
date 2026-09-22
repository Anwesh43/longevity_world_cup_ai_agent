from tools.lwc_tools import getLongeivityWorldCup, getLongeivityWorldCupPersons
from typing import Dict 
import json 

def writeFile(data : Dict, fileName : str):
    with open(fileName, "w") as f:
        f.write(json.dumps(data))
    print(f"Writing data to {fileName}")

if __name__ == "__main__":
    writeFile(getLongeivityWorldCupPersons(), "test_lwc_persons.json")
    writeFile(getLongeivityWorldCup("Benjamin Garden"), "test_bg_person.json")
