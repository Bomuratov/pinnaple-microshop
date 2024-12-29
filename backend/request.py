# import requests

# # Base API url, your Gateway API token and a phone number
# BASE_URL = "https://gatewayapi.telegram.org/"
# TOKEN = "AAFXAgAAPxg-KyLJlkrPr-nNSD7URd4TWk6Nr-n5uDTHvA"
# PHONE = "+998881836222"
# HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}


# # Function to query the API
# def post_request_status(endpoint):
#     json_body = {
#         "phone_number": PHONE,  # Must be the one tied to request_id
#         "code_length": 6,  # Ignored if you specify your own 'code'
#         "ttl": 60,  # 1 minute
#         "payload": "my_payload_here",  # Not shown to users
#         "callback_url": "https://my.webhook.here/auth",
#     }
#     url = f"{BASE_URL}{endpoint}"
#     response = requests.post(url, headers=HEADERS, json=json_body)
#     if response.status_code == 200:
#         response_json = response.json()
#         if response_json.get("ok"):
#             res = response_json.get("result", {})
#             return res
#         else:
#             error_message = response_json.get("error", "Unknown error")
#             print(f"Error: {error_message}")
#             return None
#     else:
#         print(f"Failed to get request status: HTTP {response.status_code}")
#         return None


# endpoint = "sendVerificationMessage"


# result = post_request_status(endpoint)
# print(result["request_id"])
# print(result)

# # endpoint = 'checkSendAbility'

# # json_body = {
# #     'phone_number': PHONE # E.164 format
# # }

# # result = post_request_status(endpoint, json_body)

# # if result:
# #     request_id = result.get('request_id')
# #     print(f"Request ID: {request_id}")


# endpoint = "checkVerificationStatus"

# json_body = {
#     "request_id": 172197712647187,  # Relevant request id
#     "code": 997957,  # The code the user entered in your app
# }

# result = post_request_status(endpoint, json_body)

# # Assuming the request was successful
# status = result.get("verification_status", {}).get("status")
# print(status == "code_valid")  # True if the user entered the correct code
























