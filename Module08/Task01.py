import mysql.connector

def airport_name(icao, connection):
    sql = """
        SELECT airport.name, country.name 
        FROM airport 
        JOIN country ON airport.iso_country = country.iso_country 
        WHERE airport.ident = %s
    """

    cursor = connection.cursor()
    cursor.execute(sql, (icao,))
    result = cursor.fetchall()

    if result:
        for row in result:
            print(f"Airport name is {row[0]} and country name is {row[1]}")
    else:
        print("No airport found with that ICAO code.")

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

    icao = input("Enter ICAO code: ").strip().upper()
    airport_name(icao, connection)

    connection.close()


if __name__ == "__main__":
    main()
