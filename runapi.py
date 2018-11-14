import requests
from flask import jsonify

def send_new_patient():
    r = requests.post("http://127.0.0.1:5000/api/new_patient", {"patient_id":"1",
                                                            "attending_email":"suyash.kumar@duke.edu",
                                                            "user_age":52})
    return jsonify(r)

if __name__ == "__main__":
    send_new_patient()