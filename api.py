# api.py
# This code contains all the functions required to interact (e.g. get or post requests) with a server.
# Modified Nov 13, 2018
# Written by Haeryn Kim
from flask import Flask, jsonify

app = Flask(__name__)


def parse(dict, str):
    """ Finds key associated with an input string in the input dictionary, and returns the key's value.
    Tests if the key is a string, and gives an error statement.
    Tests if dict is a jsonified dictionary.

    :param dict: dictionary
    :param str: string
    :return: value (string or number)
    """
    return dict[str]

def add_to_dictionary(newdict, key, val):
    """ Adds the input key and value pair into a dictionary called dict.

    :param newdict: dictionary
    :param key: string
    :param val: string or number
    :return: dictionary
    """
    newdict[key] = val
    return newdict

@app.route("/api/new_patient", methods=["POST"])
def post_new_patient():
    """
    This code creates an instance and sends a post request to 1) initialize and 2) register the patient
    within the heart rate server.
    Tests if input dictionary is a jsonified dictionary.

    :return: jsonified dictionary
    """
    patient = requests.get_json()  # parse through the request from client passed as json dictionary
    #Do I need to declare s as a new dictionary item before I call it?
    add_to_dictionary(s, "patient_id", parse(patient, "patient_id"))  # write code here that is
    add_to_dictionary(s, "attending_email", parse(patient, "attending_email"))
    add_to_dictionary(s, "user_age", parse(patient, "user_age"))
    return s, 200 # output status code reflecting that an entity has been posted as result of the function