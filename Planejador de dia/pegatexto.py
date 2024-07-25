from customtkinter import *
import mongodb

def get_text(texto1,texto2,texto3,texto4,texto5,texto6,texto7,texto8,texto9,texto10,
    texto11,texto12,texto13,texto14,texto15,texto16,texto17,texto18,texto19,texto20,
    texto21,texto22,texto23,texto24,data,insere_ou_att):
        
    textos = {}
    textos["Data"] = data
    textos["01:00"] = texto1.get(1.0, END).replace("\n","")
    textos["02:00"] = texto2.get(1.0, END).replace("\n","")
    textos["03:00"] = texto3.get(1.0, END).replace("\n","")
    textos["04:00"] = texto4.get(1.0, END).replace("\n","")
    textos["05:00"] = texto5.get(1.0, END).replace("\n","")
    textos["06:00"] = texto6.get(1.0, END).replace("\n","")
    textos["07:00"] = texto7.get(1.0, END).replace("\n","")
    textos["08:00"] = texto8.get(1.0, END).replace("\n","")
    textos["09:00"] = texto9.get(1.0, END).replace("\n","")
    textos["10:00"] = texto10.get(1.0, END).replace("\n","")
    textos["11:00"] = texto11.get(1.0, END).replace("\n","")
    textos["12:00"] = texto12.get(1.0, END).replace("\n","")
    textos["13:00"] = texto13.get(1.0, END).replace("\n","")
    textos["14:00"] = texto14.get(1.0, END).replace("\n","")
    textos["15:00"] = texto15.get(1.0, END).replace("\n","")
    textos["16:00"] = texto16.get(1.0, END).replace("\n","")
    textos["17:00"] = texto17.get(1.0, END).replace("\n","")
    textos["18:00"] = texto18.get(1.0, END).replace("\n","")
    textos["19:00"] = texto19.get(1.0, END).replace("\n","")
    textos["20:00"] = texto20.get(1.0, END).replace("\n","")
    textos["21:00"] = texto21.get(1.0, END).replace("\n","")
    textos["22:00"] = texto22.get(1.0, END).replace("\n","")
    textos["23:00"] = texto23.get(1.0, END).replace("\n","")
    textos["24:00"] = texto24.get(1.0, END).replace("\n","")

    if insere_ou_att:
        mongodb.atualisa_banco_de_dados(textos,data)
    else:
        mongodb.insere_banco_de_dados(textos)
    
