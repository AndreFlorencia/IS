import xmlrpc.client

print("connecting to server...")
server = xmlrpc.client.ServerProxy('http://0.0.0.0:9000')

while True:
    print("1-Transformar csv para xml")
    print("2-Listar base de dados")
    print("3-Query ficheiros")
    opcao=input("Selecione a opção")
    if(opcao==1):
        print("Converter Ficheiro em xml")
        path = "rpc-client/airports-extended.csv"
        data = server.converterXML(path)
        f = open("estacao.xml", "w")
        f.write(data)
        f.close()
        if server.validarXML("estacao.xml", "validator.xsd"):
            print('Esquema Valido! :)')
            server.importarFicheiro(data,input("Nome do Ficheiro"))

        else:
            print('Esquema incorreto :(')

    elif(opcao==2):
        server.listarXML()
    elif(opcao==3):
        print("1-query1")
        print("2-query2")
        print("3-query3")
        opcao1=input("Selecione a opcao")
        ficheiro=0
        while ficheiro !=1 or ficheiro!=2:
            print("Query ficheiro singular ou Query para todos os ficheiros")
            ficheiro=input("1-Opcao singular \n 2-Opcao plural ")
        if(opcao1==1):
            server.query1(ficheiro)
        elif(opcao1==2):
            server.query2(ficheiro)
        elif(opcao1==3):
            server.query3(ficheiro)
    else:
        print("Opcao Inválida")