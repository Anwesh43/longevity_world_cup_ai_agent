from services.lwc_service import LWCService

lwcService = LWCService()

def getLongeivityWorldCupPersons():
    print(f"Calling getLongeivityWorldCupPersons tool")
    return lwcService.getLWCPersons()

def getLongeivityWorldCup(name : str):
    print(f"Calling getLongeivityWorldCup tool {name}")
    return lwcService.getLWCPerson(name)

def getImageBaseURL():
    print(f"Calling getImageBaseURL tool")
    return lwcService.getBaseURL()