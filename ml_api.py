from flask import Flask, jsonify, request, render_template
import read_json


app = Flask(__name__)


@app.route("/")
def home():

    return render_template("home.html")


@app.route("/recommendations", methods = ['GET', 'POST'])
def recommend():
    if request.method == 'POST':
        json_data = request.get_json(force=True)
        program = json_data['program']
        k = json_data['k'] + 1
        recommendations = read_json.get_recommendations(program,
                                                        read_json.cosine_sim,
                                                        k)
    if request.method == 'GET':
        print(" This will simply return the top 5/10 most popular programs"
              " This will be implemented in later releases")
    return jsonify(recommendations)


if __name__ == "__main__":
    app.run(port=7070, threaded=True, debug=True)
