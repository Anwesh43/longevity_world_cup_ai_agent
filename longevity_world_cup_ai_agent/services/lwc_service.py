from services.base_http_client import BaseHTTPClient 
import os 
from dotenv import load_dotenv 

load_dotenv()

class LWCService:
    def __init__(self):
        self.client = BaseHTTPClient(os.environ["LWC_BASE_URL"])
        self.lwcPersonIDMap = {}

    def getBaseURL(self):
        return os.environ["LWC_BASE_URL"]

    def getLWCPersons(self):
        try:
            response = self.client.getCall("api/data/athletes")
            result = []
            for res in response:
                obj = {}
                obj["name"] = res["Name"]
                obj["CurrentPosition"] = res["CurrentPlacement"]
                self.lwcPersonIDMap[obj["name"]] = res 
                result.append(obj)
            return result 
        except Exception as e:
            print("Error", e)
            return {
                "status": "Error",
                "message": str(e)
            }
    def getLWCPerson(self, name : str):
        if not(name in self.lwcPersonIDMap):
            return {
                "status": "not found",
                "results": []
            }
        return self.lwcPersonIDMap[name]
    