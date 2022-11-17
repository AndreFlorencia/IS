import psycopg2


def query1(ficheiro):
    try:
        connection = psycopg2.connect(user="is",
                                      password="is",
                                      host="localhost",
                                      port="5432",
                                      database="is")
        if(ficheiro==2):
            cursor = connection.cursor()
            cursor.execute("SELECT unnest(xpath('//Estacao/Nome/text()',xml)) from imported_documents")

            print("Nomes das estações:")
            result = cursor.fetchall()
            print(result)
            for estacao in result:
                print(f" > {result}")
        else:
            cursor = connection.cursor()
            nome=input("Nome do ficheiro \n")

            postgres_insert_query = """SELECT unnest(xpath('//Estacao/Nome/text()',xml)) from imported_documents where %s=file_name"""
            record_to_insert = (nome)
            cursor.execute(postgres_insert_query, record_to_insert)
            print("Nomes das estações:")
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