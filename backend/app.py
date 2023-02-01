from main import handle_player_request, get_scores, handle_matchups
from calls import current_event_name
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
app.config['JSON_AS_ASCII'] = False
@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

@app.route("/getscores", methods=["GET"])
def get_scores_endpoint():
    return get_scores()['16-10-2022']

@app.route("/geteventname", methods=["GET"])
def get_eventname():
    app.config['JSON_AS_ASCII'] = False
    res = jsonify(current_event_name())
    # json.dumps(json.loads(res.data.decode('utf-8')), ensure_ascii=False)
    res.headers.add("Access-Control-Allow-Origin", "*")
    return res

@app.route("/matchups", methods=["GET"])
def start():
    player = request.args.get('player')
    res = handle_matchups()
    app.logger.info(res)
    res = jsonify(res)
    

    res.headers.add("Access-Control-Allow-Origin", "*")
    return res

# app = Flask(__name__)
# app.config['CORS_HEADERS'] = "Content-Type"
# ALLOWED_ORIGINS = ['localhost', '127.0.0.1']
# cors = CORS(app, resources={"/*": {"origins": ALLOWED_ORIGINS}}, support_credentials=True)

# @app.route("/", methods=['GET'])
# def helloWorld():
#     response = jsonify(message="Simple server is running")

#     # Enable Access-Control-Allow-Origin
#     response.headers.add("Access-Control-Allow-Origin", "*")
#     print(response.headers)
#     return response


# # # app = Flask(__name__)
# # # cors = CORS(app)
# # app.config['CORS_HEADERS'] = 'Content-Type'


# @app.route('/matchups', methods=['GET'])
# def matchups():
#     response = jsonify(message="Simple server is running")

#     # Enable Access-Control-Allow-Origin
#     response.headers.add("Access-Control-Allow-Origin", "*")
#     print(response.headers)
#     return response

#     # response.headers.add("Access-Control-Allow-Origin", "*")

#     return 'hoi'

#     player = request.args.get('player')
    
#     response = jsonify({"order_id": 123, "status": "shipped"})
#     response.headers.add("Access-Control-Allow-Origin", "*")
#     return response

#     # res = handle_player_request(player)
#     # res.
#     # return handle_player_request(player)
#     # # print(request.args.get('player'))
#     # return player


if __name__== "__main__":
    app.run(debug=True)
