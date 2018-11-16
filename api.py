# api.py
# This code contains all the functions required to interact (e.g. get or post requests) with a server.
# Modified Nov 13, 2018
# Written by Haeryn Kim
from flask import Flask, jsonify, request
from datetime import datetime

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
                break
            else:
                print("Patient {0} already exists in the database. No new information added.".format(i["patient_id"]))
                break
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

    h = dict()
    add_to_dictionary(h, "patient_id", parse(patient, "patient_id"))
    add_to_dictionary(h, "heart_rate", parse(patient, "heart_rate"))
    add_to_database(h, db)
    print(db)
    return jsonify(h), 200


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


if __name__ == "__main__":
    app.run(host="127.0.0.1")  # IP needs swapped out if running on VM
