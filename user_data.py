import os
import json

appdata_dir = (os.getenv('APPDATA')).replace("\\", "/") + "/dnbSplitter/" # type: ignore

print(appdata_dir)
def data_setup():
    os.makedirs(appdata_dir, exist_ok=True)

    if 'types.json' not in os.listdir(appdata_dir):
        with open(appdata_dir + 'types.json', "w+") as f:
            f.write('{"non_managed: []"}')

def read_data() -> dict:
    with open(appdata_dir + 'types.json', 'r') as f:
        data = json.load(f)
        data = dict(sorted(data.items()))
        key_to_move = 'non_managed'

        sorted_dict = {key_to_move: data[key_to_move]}
        sorted_dict.update({key: value for key, value in data.items() if key != key_to_move})
        return sorted_dict
    
def new_type(typeName):
    """
    WIP
    """
    data = read_data()

    if typeName in data: return

    data[typeName] = []

    save_data(data)

    pass

def new_store(typeName, storeName):
    """
    WIP
    """
    pass

def save_data(inpData):
    with open(appdata_dir + 'types.json', "w+") as f:
        f.write(json.dumps(inpData))
