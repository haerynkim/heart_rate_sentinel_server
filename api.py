# api.py
# This code contains all the functions required to interact (e.g. get or post requests) with a server.
# Modified Nov 13, 2018
# Written by Haeryn Kim
from flask import Flask, jsonify, request
from datetime import datetime
from time import strftime

app = Flask(__name__)

db = [{"patient_id": "0000"}]  # initialize db as non-empty list


def parse(dict, str):
    """ Finds key associated with an input string in the input dictionary, and returns the key's value.
    Tests if the key is a string, and gives an error statement.
    Tests if key is in the dictionary.
    Tests if dict is a jsonified dictionary.

    :param dict: dictionary
    :param str: string
    :return: value (string or number)
    """
    return dict[str]


def add_to_dictionary(newdict, key, val):
    """ Adds the given key and value pair into a dictionary called dict.

    :param newdict: dictionary
    :param key: string
    :param val: string or number
    :return: dictionary
    """
    newdict[key] = val
    return newdict


def add_to_database(dictionary, database):
    """
    receives a dict with "patient_id"as a value, parses through the database for that patient's information and replaces
    the values if they are different than the ones that previously existed, with the exception of heart rate and timestamp.
    Heart rate and time stamp values are appended.

    :param dict: dictionary
    :param database: list of dictionaries
    :return:
    """
    HRdata = dict()
    for i in database:
        if i["patient_id"] != dictionary["patient_id"]:
            continue
    if i["patient_id"] == dictionary["patient_id"]:
        # print("same patient exist in db")
        if "heart_rate" in list(dictionary.keys()):
            HRdata["HR"] = dictionary["heart_rate"]
            HRdata["Time"] = datetime.now()
            i["heart_rate"].append(HRdata)  # append dictionary with HR and timestamp keys to list
            print("Patient {0} exists in the database. Heart rate information with current time appended.".format(
                i["patient_id"]))
        else:
            print("Patient {0} already exists in the database. No new information added.".format(i["patient_id"]))
    else:
        database.append(dictionary)
        print("Patient {0}'s information was added to the database.".format(dictionary["patient_id"]))


@app.route("/api/new_patient", methods=["POST"])
def post_new_patient():
    """
    This code creates an instance and sends a post request to 1) initialize and 2) register the patient
    within the heart rate server.
    Tests if input dictionary is a jsonified dictionary.

    :return: jsonified dictionary
    """
    global db
    patient = request.get_json()  # parse through the request from client passed as json dictionary
    try:  # raise a validation error if a key is not found in the request
        validate_new_patient_request(patient)
    except ValidationError as inst:
        return jsonify({"Error message": inst.message}), 500

    s = dict()
    add_to_dictionary(s, "patient_id", parse(patient, "patient_id"))
    add_to_dictionary(s, "attending_email", parse(patient, "attending_email"))
    add_to_dictionary(s, "user_age", parse(patient, "user_age"))
    add_to_dictionary(s, "heart_rate", [])
    add_to_database(s, db)
    print(db)
    return jsonify(s), 200  # output status code reflecting that an entity has been posted as result of the function


NEW_PATIENT_KEYS = [
    "patient_id",
    "attending_email",
    "user_age"
]


class ValidationError(Exception):
    def __init__(self, message):
        self.message = message


def validate_new_patient_request(patient_req):
    for key in NEW_PATIENT_KEYS:
        if key not in patient_req.keys():
            raise ValidationError("Key '{0}' not present in request".format(key))


@app.route("/api/heart_rate", methods=["POST"])
def post_heart_rate():
    global db
    patient = request.get_json()
    try:
        validate_heart_rate_request(patient)
    except ValidationError as inst:
        return jsonify({"Error message": inst.message}), 500
    for i in db:
        if patient["patient_id"] != i["patient_id"]:
            continue
    if patient["patient_id"] == i["patient_id"]:
        h = dict()
        add_to_dictionary(h, "patient_id", parse(patient, "patient_id"))
        add_to_dictionary(h, "heart_rate", parse(patient, "heart_rate"))
        add_to_database(h, db)
        print(db)
        return jsonify(h), 200
    else:
        return "Patient ID does not exist. Post new patient first.", 400


HEART_RATE_KEYS = [
    "patient_id",
    "heart_rate"
]


def validate_heart_rate_request(patient_req):
    for key in HEART_RATE_KEYS:
        if key not in patient_req.keys():
            raise ValidationError("Key '{0}' not present in request".format(key))


@app.route("/api/server_test")
def servertest():
    return "server active"


@app.route("/api/status/<patient_id>", methods=["GET"])
def get_status(patient_id):
    global db
    for i in db:
        if i["patient_id"] != patient_id:
            continue
    if i["patient_id"] == patient_id:
        HRdic = i["heart_rate"][-1]  # returns dictionary of storing latest HR and time
        latestHR = HRdic["HR"]
        latesttime = HRdic["Time"]  # currently returns datetime.datetime(info) variable
        print(type(latesttime))
        if is_tachycardic(i["user_age"], latestHR):
            return "Patient is tachycardic as of {0}.".format(latesttime.strftime('%Y-%m-%d %H:%M:%S'))
        else:
            return "Patient is not tachycardic as of {0}.".format(latesttime.strftime('%Y-%m-%d %H:%M:%S'))
    else:
        return "Patient ID does not exist. Post new patient and heart rate info first.", 300


def is_tachycardic(age, heartrate):
    """
    Returns True if heart rate is tachycardic for that patient's age.

    :param age: int
    :param heartrate: int
    :return: boolean
    """
    if (0 <= age <= 1) and heartrate > 159:
        return True
    if (1 < age <= 2) and heartrate > 179:
        return True
    if (2 < age <= 4) and heartrate > 137:
        return True
    if (4 < age <= 7) and heartrate > 133:
        return True
    if (7 < age <= 11) and heartrate > 130:
        return True
    if (11 < age <= 15) and heartrate > 119:
        return True
    if age > 15 and heartrate > 100:
        return True
    else:
        return False


@app.route("/api/heart_rate/<patient_id>", methods=["GET"])
def get_hr(patient_id):
 global db
 all_hr = []
 for i in db:
     if i["patient_id"] != patient_id:
         continue
 if i["patient_id"] == patient_id:
     if len(i["heart_rate"]) != 0:  # there is previous heart rate information stored inside list
         patient_hrs, avg_hr = compile_avg(i["heart_rate"], all_hr)
         return jsonify(patient_hrs)
     else:  # there is no previous heart rate information stored inside list
         return "There is no heart rate data for Patient {0}. Post heart rate info first".format(patient_id), 300
 else:
     return "Patient ID does not exist. Post new patient and heart rate info first.", 300


def compile_avg(list_of_dicts, new_list):
    """
    This takes all the HR key's values in the dictionaries inside list_of_dicts and appends them to a new_list. Then it
    computes and returns the average.

    :param list_of_dicts: list
    :param new_list: list
    :return: list, float
    """
    for i in list_of_dicts:  # iterates through all the dictionaries with key "HR
        new_list.append(i["HR"])
        if len(new_list) == 1:
            avg_new_list = i["HR"]
        else:
            avg_new_list = sum(new_list) / len(new_list)
    return new_list, avg_new_list


if __name__ == "__main__":
    app.run(host="127.0.0.1")  # IP needs swapped out if running on VM
