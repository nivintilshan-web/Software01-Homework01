import mysql.connector

def country_name(country_code, connection):
    sql = "SELECT name FROM country WHERE iso_country = %s"
    cursor = connection.cursor()
    cursor.execute(sql, (country_code,))
    result = cursor.fetchone()

    if result:
        print(f"{result[0]} has:")
    else:
        print("Invalid country code.")

    cursor.close()


def count_airports_by_type(country_code, airport_type, connection):
    sql = """
        SELECT airport.type, COUNT(*)
        FROM airport
        WHERE airport.iso_country = %s AND airport.type = %s
        GROUP BY airport.type
    """

    cursor = connection.cursor()
    cursor.execute(sql, (country_code, airport_type))
    result = cursor.fetchone()

    if result:
        print(f"{result[0]}: {result[1]}")
    else:
        print(f"{airport_type}: 0")

    cursor.close()


def main():
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port='3306',
        database='new_flight',
        user='root',
        password='2025',
        autocommit=True
    )

    country_code = input("Enter ISO country code (e.g. FI, US, LK): ").strip().upper()

    country_name(country_code, connection)

    count_airports_by_type(country_code, 'small_airport', connection)
    count_airports_by_type(country_code, 'medium_airport', connection)
    count_airports_by_type(country_code, 'large_airport', connection)
    count_airports_by_type(country_code, 'heliport', connection)

    connection.close()


if __name__ == "__main__":
    main()
