import requests
import json

# Replace these with your actual credentials
API_KEY = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiIwX2FwcmVzdG9hbWlnb0BnbWFpbC5jb21fMiIsIm1vZGlmeV9wYXNzd29yZCI6MSwic2NvcGUiOlsiYWxsIl0sImRldGFpbCI6eyJvcmdhbml6YXRpb25JZCI6MCwidG9wR3JvdXBJZCI6bnVsbCwiZ3JvdXBJZCI6bnVsbCwicm9sZUlkIjotMSwidXNlcklkIjoxNDk1NDYwOCwidmVyc2lvbiI6MTAwMSwiaWRlbnRpZmllciI6ImFwcmVzdG9hbWlnb0BnbWFpbC5jb20iLCJpZGVudGl0eVR5cGUiOjIsIm1kYyI6IkZPUkVJR05fMSIsImFwcElkIjoiMzEyNDA3MTcyNDg0NzUwIn0sImV4cCI6MTc0NDM3Nzc4MywibWRjIjoiRk9SRUlHTl8xIiwiYXV0aG9yaXRpZXMiOlsiYWxsIl0sImp0aSI6ImM2MjdhNDhjLTljZTctNDc2Ni04Zjk2LWM4ZjJiMzY2YjEyMiIsImNsaWVudF9pZCI6InRlc3QifQ.GP4HJ_cIcvw2EnWIfkDCJx-RyLQAEVBNogtIR21EFvnhg-9_e-HfpwpMa2Gi6uXHYE4wz9NLtWuhVW7mNML12jsf5XSr3xCbxJxxIUdnrOlirMPXjD_77yipMDkIi70Gi4Nuj8hnOUiIS29AEK9t3ydqNM_vwQabq4k_I-zbPEadUMTHaj-uCq9DWbgDN7-U1hzJ3U_xaaJQuuYKE8JPfNXppXAbt49SWwoDHf7RWdzMd-Whbz-wbc9OP8kMm9V-t2dOKsjL64AkjDwtKPiLD6RYh_iTPSgKMa2fVLF79eo_hl2poyDrOyIgSc_nJzFtG44CGj_zS5n1Mrh3mOL_tA"
STATION_ID = "ID62674180"
BASE_URL = "https://globalapi.solarmanpv.com"  # Replace with the actual API base URL


# Endpoint for retrieving real-time power station data
# ENDPOINT = "{}/station/v1.0/realTime".format(BASE_URL)
ENDPOINT = "{}/station/v1.0/list".format(BASE_URL)

# Headers for the API request
headers = {
    "Authorization": "Bearer {}".format(API_KEY),
    "Content-Type": "application/json",
}
params = {
    "page": 1,
    "pageSize": 10,  # Adjust as needed
}

# Make the API request
response = requests.post(ENDPOINT, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    print "Real-time Power Station Data:"
    print json.dumps(data, indent=4)  # Pretty-print the JSON data
else:
    print "Failed to retrieve data. Status code: {}".format(response.status_code)
    print "Response: {}".format(response.text)
