import requests

def send_new_patient():
    r = requests.post("http://127.0.0.1:5000/api/new_patient", json = {"patient_id":"1",
                                                            "attending_email":"suyash@duke.edu",
                                                            "user_age":4})
    #print(r.json())

if __name__ == "__main__":
    send_new_patient()