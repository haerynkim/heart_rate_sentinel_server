import requests

def send_int_avg():
    r = requests.post("http://127.0.0.1:5000/api/heart_rate/interval_average", json = {"patient_id":"3",
                                                            "heart_rate_average_since":"2018-03-09 11:00:36.372339"})
    print(r.text)

if __name__ == "__main__":
    send_int_avg()