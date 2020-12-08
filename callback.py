import requests
import base64

# Get auth token use client_id and client_secret
def get_token() -> "global response":
    client_id = "XXXXXX"
    client_secret = "XXXXXXXX"
    authorization = base64.b64encode(bytes(client_id + ":" + client_secret, "ISO-8859-1")).decode("ascii")
    request_headers = {"Authorization": f"Basic {authorization}","Content-Type": "application/x-www-form-urlencoded"}
    request_body = {"grant_type": "client_credentials"}
    global response
    response = requests.post("https://login.mypurecloud.de/oauth/token", data=request_body, headers=request_headers)
    global requestHeaders
    response_json = response.json()
    requestHeaders = {"Authorization": f"{ response_json['token_type'] } { response_json['access_token']}"}
    error_handling("token is generated")

#Creates a callback interaction, info on https://developer.mypurecloud.com/api/rest/v2/conversations/index.html#postConversationsCallbacks
def create_callback() -> None:
    body = {
    "queueId": "c76fea65-d8fa-461f-897f-1c7e7e09b9f0",
    "callbackNumbers": ["+4915238484530"],
    "callbackUserName":"Test"}
    response = requests.post("https://api.mypurecloud.de/api/v2/conversations/callbacks", json = body, headers = requestHeaders)
    error_handling("successfully created")

# Deletes a session
def kill_session() -> None:
    response = requests.delete("https://api.mypurecloud.de/api/v2/tokens/me", headers=requestHeaders)
    error_handling("Token deleted")

# Simple error handling
def error_handling(text:str) -> None:
    if response.status_code > 200 or response.status_code < 300:
        print(text)
    else:
        print(f"Failure: { str(response.status_code) } - { response.reason }")
        sys.exit(response.status_code)


get_token()
create_callback()
kill_session()




