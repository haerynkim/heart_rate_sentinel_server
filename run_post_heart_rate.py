import requests


def send_heart_rate():
    r = requests.post("http://vcm-7474.vm.duke.edu:5000/api/heart_rate", json={"patient_id": "3",
                                                                    "heart_rate": 78})
    print(r.text)
    # right now, major error where you must run post_new_patient first.

if __name__ == "__main__":
    send_heart_rate()
