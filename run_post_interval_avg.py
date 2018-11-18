import requests

def send_int_avg():
    r = requests.post("http://vcm-7474.vm.duke.edu:5000/api/heart_rate/interval_average", json = {"patient_id":"2",
                                                            "heart_rate_average_since":"2018-03-09 11:00:36.372339"})
    print(r.text)

if __name__ == "__main__":
    send_int_avg()