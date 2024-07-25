from interfacecria import gui_cria
from interfaceatt import gui_att
from customtkinter import *
from tkcalendar import Calendar
import datetime
from mongodb import verifica_banco_de_dados


tela_de_entrada = CTk()
tela_de_entrada.title('Planejador')
tela_de_entrada.geometry("600x300")

def pega_data():
    aux = 0
    dia = ""
    mes = ""
    ano = ""

    data = calendario.get_date()
    for i in data:  
        if i != '/' and aux == 0:
            mes += i
        elif i != '/' and aux == 1:
            dia += i
        elif i != '/' and aux == 2:
            ano += i
        else:
            aux += 1
        
    data = dia + '/' + mes + '/' + ano

    if verifica_banco_de_dados(data):
        tela_de_entrada.destroy()
        gui_cria(data)

    else:
        tela_de_entrada.destroy()
        gui_att(data)

calendario = Calendar(tela_de_entrada, selectmode = "day", year = datetime.date.today().year, month = datetime.date.today().month)
calendario.pack(fill = "both")

botao = CTkButton(tela_de_entrada, text = "Escolha uma data", command = pega_data)
botao.pack(pady = 20)

tela_de_entrada.mainloop()

