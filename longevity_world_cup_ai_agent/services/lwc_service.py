from services.base_http_client import BaseHTTPClient 
import os 
from dotenv import load_dotenv 

load_dotenv()

class LWCService:
    def __init__(self):
        self.client = BaseHTTPClient(os.environ["LWC_BASE_URL"])

    def getLWCPersons(self):
        try:
            response = self.client.getCall("api/data/athletes")
            return response 
        except Exception as e:
            print("Error", e)
            return {
                "status": "Error",
                "message": str(e)
            }