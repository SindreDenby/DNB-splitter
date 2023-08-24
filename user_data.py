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
        return json.load(f)
    
def new_type(typeName):
    """
    WIP
    """
    pass

def new_store(typeName, storeName):
    """
    WIP
    """
    pass
