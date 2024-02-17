from urllib.request import urlopen
from flask import Flask, jsonify
import datetime
from flask_cors import CORS, cross_origin
#import 1. library that can fetch website's code 2. flask basically the whole server/api 3. tells time 4. fixes CORS problems
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#defining the app before startup
@app.route('/', methods=['GET'])
def get_data():
    f = urlopen("http://192.168.88.45/") #loads the site
    f = str(f.read()) #saves the site's code in to the f variable
    f = f.split(" ")  # cutting the code to only get the wanted information
    f = f[39].split("cm")
    f  = str(f[0])
    print(f) # for debugging prints in to the console content that will be sent to the client
    cas = datetime.datetime.now()
    cas = cas.strftime("%d.%m.%y %H:%M:%S")
    data = {
        'hladina': f,
        'cas': cas,
        }
#setting up the json that will be sent
    return jsonify(data)
# sending the json back to the clientcm
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)
    #running the app
