from flask import Flask, render_template, jsonify
import random
import json

app = Flask(__name__)
PORT = 3500


@app.route("/", methods=["GET", "POST"])
def startpy():

    result = {

        "Greetings": "Tactlabs welcomes you"
    }

    return render_template("index.html")




@app.route("/data", methods=["GET"])
def read_json():


    
    year_list = ['2020', '2021', '2022', '2023', '2024']

    dollars = [14, 17, 21, 24, 30]
    average = [7, 8.5, 10.5, 12, 15]
                

    result_dict = {
        'year': year_list,
        'title': 'AI in IT services - Forecast ',
        'subtitle': 'Source: IDC 2021',
        'amount': dollars,
        'avg': average
    }

    return jsonify(result_dict)

    


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
