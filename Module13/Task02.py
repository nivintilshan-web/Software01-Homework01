from flask import Flask, Response
import json
import mysql.connector

app = Flask(__name__)


def get_airport_info(icao_code):
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='flight_game',
            user='root',
            password='2025',
            autocommit=True
        )

        sql = "SELECT ident, name, municipality FROM airport WHERE ident = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (icao_code.upper(),))
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        if result:
            return {
                "ICAO": result[0],
                "Name": result[1],
                "Location": result[2]
            }
        else:
            return None

    except mysql.connector.Error:
        return None


@app.route('/airport/<icao_code>')
def get_airport(icao_code):
    try:
        if len(icao_code) != 4 or not icao_code.isalpha():
            error_response = {
                "ICAO": icao_code,
                "error": "Invalid ICAO code format. Must be 4 letters.",
                "status": 400
            }
            json_response = json.dumps(error_response)
            return Response(response=json_response, status=400, mimetype="application/json")

        airport_info = get_airport_info(icao_code)

        if airport_info:
            return airport_info
        else:
            error_response = {
                "ICAO": icao_code,
                "error": "Airport not found",
                "status": 404
            }
            json_response = json.dumps(error_response)
            return Response(response=json_response, status=404, mimetype="application/json")

    except Exception:
        error_response = {
            "ICAO": icao_code,
            "error": "Internal server error",
            "status": 500
        }
        json_response = json.dumps(error_response)
        return Response(response=json_response, status=500, mimetype="application/json")


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