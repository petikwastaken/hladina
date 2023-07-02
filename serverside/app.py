from urllib.request import urlopen
from flask import Flask, jsonify
#import 1. libraty that can fetch website's code 2. flask basically the whole server/api
app = Flask(__name__)
#defining the app before startup
@app.route('/', methods=['GET'])
def get_data():
    f = urlopen("http://192.168.88.45/") #loads the site
    f = str(f.read()) #saves the site's code in to the f variable
    f = f.split(" ")  # cutting the code to only get the wanted information
    f = f[39].split("cm")
    f  = str(f[0])
    print(f) # for debugging prints in to the console content that will be sent to the client
    data = {
        'hloubka': f
    }
#setting up the json that will be sent
    return jsonify(data)
# sending the json back to the clientcm
if __name__ == '__main__':
    app.run()
    #running the app