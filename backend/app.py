from main import handle_matchups
from calls import current_event_name
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
app.config['JSON_AS_ASCII'] = False


@app.route("/", defaults={'path': ''})
def serve(path):
    return send_from_directory(app.static_folder, 'index.html')


# @app.route("/getscores", methods=["GET"])
# def get_scores_endpoint():
#     return get_scores()['16-10-2022']


@app.route("/geteventname", methods=["GET"])
def get_eventname():
    app.config['JSON_AS_ASCII'] = False
    res = jsonify(current_event_name())
    res.headers.add("Access-Control-Allow-Origin", "*")
    return res


@app.route("/matchups", methods=["GET"])
def start():
    res = handle_matchups()
    app.logger.info(res)
    res = jsonify(res)

    res.headers.add("Access-Control-Allow-Origin", "*")
    return res


if __name__ == "__main__":
    app.run(debug=True)
