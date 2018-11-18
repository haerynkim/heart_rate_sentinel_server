import requests

def get_patient_status():
    """
    This returns whether patient's tachycardic.

    :return:
    """
    r = requests.get("http://vcm-7474.vm.duke.edu:5000/api/status/3")
    print(r.text)


if __name__ == "__main__":
    get_patient_status()