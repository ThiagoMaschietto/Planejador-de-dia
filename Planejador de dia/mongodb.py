import pymongo

def insere_banco_de_dados(textos):
    conect = pymongo.MongoClient("")

    db = conect.get_database("")
    colecao = db.get_collection("")
    
    colecao.insert_one(textos)

def atualisa_banco_de_dados(textos,data):
    conect = pymongo.MongoClient("")

    db = conect.get_database("")
    colecao = db.get_collection("")
    
    colecao.delete_one({"Data": data})
    colecao.insert_one(textos)

def verifica_banco_de_dados(data):
    data_dict = {}
    data_dict["Data"] = data
    conect = pymongo.MongoClient("")

    db = conect.get_database("")
    colecao = db.get_collection("")

    
    if list(colecao.find(data_dict)) == []:
        return True

def recupera_dados(data,hora):
    data_dict = {}
    data_dict["Data"] = data
    conect = pymongo.MongoClient("")

    db = conect.get_database("")
    colecao = db.get_collection("")

    lista = list(colecao.find(data_dict))

    data_dict = {}

    for i in range(len(lista)):
        data_dict = lista[i]

    return data_dict[hora]


    
    