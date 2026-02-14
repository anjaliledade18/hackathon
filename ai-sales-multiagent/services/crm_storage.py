import json

def save_to_crm(record):

    try:
        with open("data/crm.json", "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(record)

    with open("data/crm.json", "w") as f:
        json.dump(data, f, indent=2)
