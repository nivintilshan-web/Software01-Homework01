import mysql.connector
from geopy.distance import geodesic

def get_codes(icao, connection):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    cursor = connection.cursor()
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    cursor.close()
    return result

def distance(icao1, icao2, connection):
    pr1 = get_codes(icao1, connection)
    pr2 = get_codes(icao2, connection)

    if pr1 is None:
        print(f"❌ ICAO code '{icao1}' not found in database.")
        return
    if pr2 is None:
        print(f"❌ ICAO code '{icao2}' not found in database.")
        return

    distance_km = geodesic(pr1, pr2).km
    print(f"\nDistance between {icao1.upper()} and {icao2.upper()}: {distance_km:.2f} km")

def main():
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port='3306',
        database='new_flight',
        user='root',
        password='2025',
        autocommit=True
    )

    icao1 = input("Enter ICAO 1: ").strip().upper()
    icao2 = input("Enter ICAO 2: ").strip().upper()

    distance(icao1, icao2, connection)

    connection.close()

if __name__ == "__main__":
    main()
