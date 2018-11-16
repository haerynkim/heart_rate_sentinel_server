import requests

def get_patient_status():
    """
    This returns all HR data registered under Patient ID.
    """
    r = requests.get("http://127.0.0.1:5000/api/heart_rate/2")
    print(r.text)


if __name__ == "__main__":
    get_patient_status()