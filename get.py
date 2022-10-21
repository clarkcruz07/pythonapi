#def showName(name):
#    print(f'Hi, {name}')

#if __name__ == '__main__':
#    showName('Clark')


from flask import *
import json, datetime
import base64, secrets

header = ":" + base64.b64encode(secrets.token_bytes(32)).decode() + ":"

app = Flask(__name__)

@app.route('/get/', methods=['GET'])
def get():
    query = str(request.args.get('doornumber')) #/get/?params=1234
    data_set = {'Pandora': '', 'door_number': f'{query}', 'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    #json_dump = json.dumps(data_set)

    return data_set

if __name__ == '__main__':
    app.run(port=7777)