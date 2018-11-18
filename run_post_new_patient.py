import requests

def send_new_patient():
    r = requests.post("http://vcm-7474.vm.duke.edu:5000/api/new_patient", json = {"patient_id":"3",
                                                            "attending_email":"suyash@duke.edu",
                                                            "user_age":8})
    #print(r.json())

if __name__ == "__main__":
    send_new_patient()