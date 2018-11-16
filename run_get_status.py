import requests

def get_patient_status():
    """
    This returns whether patient's tachycardic.

    :return:
    """
    r = requests.get("http://127.0.0.1:5000/api/status/2")
    print(r.text)


if __name__ == "__main__":
    get_patient_status()