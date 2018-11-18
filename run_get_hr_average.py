import requests

def get_patient_average():
    """
    This returns all HR data registered under Patient ID.
    """
    r = requests.get("http://vcm-7474.vm.duke.edu:5000/api/heart_rate/average/2")
    print(r.text)


if __name__ == "__main__":
    get_patient_average()