from flask import Flask, Response
import json
import math

app = Flask(__name__)


def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True


@app.route('/prime_number/<number>')
def check_prime(number):
    try:
        num = int(number)

        prime_check = is_prime(num)

        response = {
            "Number": num,
            "isPrime": prime_check
        }

        return response

    except ValueError:
        error_response = {
            "Number": number,
            "isPrime": False,
            "error": "Invalid number format",
            "status": 400
        }
        json_response = json.dumps(error_response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response


@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
