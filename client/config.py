# Configuration file used for client node when running on local
from os import environ

DEFAULT_SERVER_URL = 'http://localhost:5000'
GLOBAL_TMP_PATH = 'None'
GLOBAL_DATASETS = '/Users/angelmarques/tfg/federated-learning-network/datasets'

if environ.get('CLIENT_URL') == "http://localhost:5001":
    print("I'm client 1")
    GLOBAL_TMP_PATH = '/tmp1'
elif environ.get('CLIENT_URL') == "http://localhost:5002":
    print("I'm client 2")
    GLOBAL_TMP_PATH = '/tmp2'
elif environ.get('CLIENT_URL') == "http://localhost:5003":
    print("I'm client 3")
    GLOBAL_TMP_PATH = '/tmp3'
elif environ.get('CLIENT_URL') == "http://localhost:5004":
    print("I'm client 4")
    GLOBAL_TMP_PATH = '/tmp4'

   




