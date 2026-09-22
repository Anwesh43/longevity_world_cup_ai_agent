from services.lwc_service import LWCService

lwcService = LWCService()

def getLongeivityWorldCupPersons():
    print(f"Calling getLongeivityWorldCupPersons tool")
    return lwcService.getLWCPersons()
