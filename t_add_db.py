from api import add_to_database


database = [{"patient_id":"1"}]
d = {"patient_id":"0", "heart_rate":98}

if __name__ == "__main__":
    add_to_database(d, database)
    print(database)