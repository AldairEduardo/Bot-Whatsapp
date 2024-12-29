import requests
import json

def SentMessangeWhatsapp(data):
    try:
        token = "EAAQXQmSZAMuEBO6Nk4YIRi7tnPEkqCJyoyjhZBxFmnaV59EsZCUFfZBxk3q8iChB5YNcyPbctowXNLJNoAfoXLMgYHvHTWG4ahXLqgQIS29tLlV0BZCabTeZA7FNSnaJuzbCYjU1qLPFNTuLvoj87PckLy8TmFLZBlCYCuoZCPdAdNtlSZAnL2wPx8XWtWrdGgHz1eQZDZD"
        api_url = "https://graph.facebook.com/v21.0/473126452558811/messages"
        headers = {"content-type": "application/json","Authorization": "Bearer "+token}
        response = requests.post(api_url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            return "Message sent successfully"
        else:
            return "Error sending message"
    except Exception as exception:
        print(exception)
        return "Error sending message"
    