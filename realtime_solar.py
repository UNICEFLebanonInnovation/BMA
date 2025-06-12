import requests
import hashlib
import json

# Configuration - Replace with your own credentials
APP_ID = '312407172484750'
APP_SECRET = '6a136cb4efe6fe16ceb7b724ae30cc4a'
# EMAIL = 'aprestoamigo@gmail.com'
EMAIL = 'iolleik@unicef.org'
# EMAIL = 'unicef.maditechnology@gmail.com'
# USERNAME = 'DEMO12'
# PASSWORD = 'Adsae1e_'
PASSWORD = 'Solarman_12'
# PASSWORD = 'Solar@102030'
hashed_password = hashlib.sha256(PASSWORD.encode()).hexdigest()
# STATION_ID = 62771521  # Replace with your actual station ID
STATION_ID = 63894995  # Replace with your actual station ID


# Step 2: Obtain Access Token
def get_access_token():
    try:

        response = requests.post(
            # url="https://globalapi.solarmanpv.com/account/v1.0/token",
            url="https://globalapi.solarmanpv.com/oauth-s/oauth/token",
            params={"appId": APP_ID, "language": "en"},
            headers={"Content-Type": "application/json"},
            json={  # Use json instead of data=json.dumps()
                "username": EMAIL,
                "password": hashed_password,
                "appSecret": APP_SECRET
            }
        )

        result = response.json()
        print(result)
        return result['access_token']
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def get_station_list(access_token):
    try:

        response = requests.post(
            url="https://globalapi.solarmanpv.com/station/v1.0/list",
            params={"appId": APP_ID, "language": "en"},
            headers={
                "Content-Type": "application/json",
                "appId": APP_ID,
                "Authorization": "Bearer {}".format(access_token)
            },
            json={  # Use json instead of data=json.dumps()
                "page": 1,
                "email": EMAIL,
                "password": PASSWORD,
                "appId": APP_ID,
                "appSecret": APP_SECRET,
                "Authorization": "Bearer {}".format(access_token)
            }
        )

        print(response)
        result = response.json()
        print(result)
        return result
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


# Step 3: Retrieve Real-Time Power Station Data
def get_real_time_data(access_token):

    try:

        response = requests.post(
            url="https://globalapi.solarmanpv.com/station/v1.0/realTime",
            params={"language": "en",
                    # "appId": APP_ID
                    },
            headers={
                # "Content-Type": "application/json",
                # "appId": APP_ID,
                # "stationId": STATION_ID,
                "Authorization": "Bearer {}".format(access_token)
            },
            json={  # Use json instead of data=json.dumps()
                # "email": EMAIL,
                # "password": PASSWORD,
                # "appId": APP_ID,
                # "appSecret": APP_SECRET,
                "stationId": STATION_ID,
                # "Authorization": "Bearer {}".format(access_token)
            }

        )

        result = response.json()
        return result
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


# Main execution
try:
    token = get_access_token()
    # station_list = get_station_list(token)
    # real_time_data = get_real_time_data(token)
    # print("Real-Time Data:", real_time_data)
except Exception as e:
    print("Error:", e)
