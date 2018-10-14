import requests


def get_user_location(system):
    r = requests.get(
        f"{system['apiEndpoint']}/v1/devices/{system['device']['deviceId']}/settings/address",
        headers={"Authorization": f"Bearer {system['apiAccessToken']}"}
    )

    print(r.status_code)
    print(r.text)

    if r.status_code == 200:
        return r.json()

    else:
        return None
