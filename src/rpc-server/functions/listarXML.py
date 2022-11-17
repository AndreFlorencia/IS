import psycopg2
def listarXML():
    try:
        connection = psycopg2.connect(user="is",
                                      password="is",
                                      host="localhost",
                                      port="5432",
                                      database="is")

        cursor = connection.cursor()
        cursor.execute("SELECT file_name from imported_documents")

        print("Nomes dos ficheiros:")
        result = cursor.fetchall()
        print(result)
        for estacao in result:
            print(f" > {result}")
    except (Exception, psycopg2.Error) as error:
        print("Failed to fetch data", error)

    finally:

        if connection:
            cursor.close()
            connection.close()