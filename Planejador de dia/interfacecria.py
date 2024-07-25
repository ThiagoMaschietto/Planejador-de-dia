from customtkinter import *
from pegatexto import get_text

def gui_cria(data):

    janela = CTk()
    janela.title("Planejador")
    janela.geometry("1200x750")
    janela.resizable(True,True)

    data_label = CTkLabel(janela, padx = 100, pady = 30)
    data_label.configure(text = f"{data}")
    data_label.grid(row = 0, column = 4)

    hora1 = CTkLabel(janela, padx = 100, pady = 30)
    hora1.configure(text = "01:00")
    hora1.grid(row = 0, column = 0)
    texto1 = CTkTextbox(janela,height = 10,width = 350, pady = 10)
    texto1.grid(row = 0, column = 1)

    hora2 = CTkLabel(janela, pady = 30)
    hora2.configure(text = "02:00")
    hora2.grid(row = 1, column = 0)
    texto2 = CTkTextbox(janela,height = 10,width = 350, pady = 10)
    texto2.grid(row = 1, column = 1)

    hora3 = CTkLabel(janela, pady = 30)
    hora3.configure(text = "03:00")
    hora3.grid(row = 2, column = 0)
    texto3 = CTkTextbox(janela,height = 10,width = 350, pady = 10)
    texto3.grid(row = 2, column = 1)

    hora4 = CTkLabel(janela, pady = 30)
    hora4.configure(text = "04:00")
    hora4.grid(row = 3, column = 0)
    texto4 = CTkTextbox(janela,height = 10,width = 350, pady = 10)
    texto4.grid(row = 3, column = 1)

    hora5 = CTkLabel(janela, pady = 30)
    hora5.configure(text = "05:00")
    hora5.grid(row = 4, column = 0)
    texto5 = CTkTextbox(janela,height = 10,width = 350, pady = 10)
    texto5.grid(row = 4, column = 1)

    hora6 = CTkLabel(janela, pady = 30)
    hora6.configure(text = "06:00")
    hora6.grid(row = 5, column = 0)
    texto6 = CTkTextbox(janela,height = 10,width = 350, pady = 10)
    texto6.grid(row = 5, column = 1)

    hora7 = CTkLabel(janela, pady = 30)
    hora7.configure(text = "07:00")
    hora7.grid(row = 6, column = 0)
    texto7 = CTkTextbox(janela,height = 10,width = 350, pady = 10)
    texto7.grid(row = 6, column = 1)

    hora8 = CTkLabel(janela, pady = 30)
    hora8.configure(text = "08:00")
    hora8.grid(row = 7, column = 0)
    texto8 = CTkTextbox(janela,height = 10,width = 350, pady = 10)
    texto8.grid(row = 7, column = 1)

    hora9 = CTkLabel(janela, pady = 30)
    hora9.configure(text = "09:00")
    hora9.grid(row = 8, column = 0)
    texto9 = CTkTextbox(janela,height = 10,width = 350, pady = 10)
    texto9.grid(row = 8, column = 1)

    hora10 = CTkLabel(janela, pady = 30)
    hora10.configure(text = "10:00")
    hora10.grid(row = 9, column = 0)
    texto10 = CTkTextbox(janela,height = 10,width = 350, pady = 10)
    texto10.grid(row = 9, column = 1)

    hora11 = CTkLabel(janela, pady = 30)
    hora11.configure(text = "11:00")
    hora11.grid(row = 10, column = 0)
    texto11 = CTkTextbox(janela,height = 10,width = 350, pady = 10)
    texto11.grid(row = 10, column = 1)

    hora12 = CTkLabel(janela, pady = 30)
    hora12.configure(text = "12:00")
    hora12.grid(row = 11, column = 0)
    texto12 = CTkTextbox(janela,height = 10,width = 350, pady = 10)
    texto12.grid(row = 11, column = 1)

    hora13 = CTkLabel(janela, padx = 100, pady = 30)
    hora13.configure(text = "13:00")
    hora13.grid(row = 0, column = 2)
    texto13 = CTkTextbox(janela,height = 10,width = 350, pady = 10)
    texto13.grid(row = 0, column = 3)

    hora14 = CTkLabel(janela, pady = 30)
    hora14.configure(text = "14:00")
    hora14.grid(row = 1, column = 2)
    texto14 = CTkTextbox(janela,height = 10,width = 350, pady = 10)
    texto14.grid(row = 1, column = 3)

    hora15 = CTkLabel(janela, pady = 30)
    hora15.configure(text = "15:00")
    hora15.grid(row = 2, column = 2)
    texto15 = CTkTextbox(janela,height = 10,width = 350, pady = 10)
    texto15.grid(row = 2, column = 3)

    hora16 = CTkLabel(janela, pady = 30)
    hora16.configure(text = "16:00")
    hora16.grid(row = 3, column = 2)
    texto16 = CTkTextbox(janela,height = 10,width = 350, pady = 10)
    texto16.grid(row = 3, column = 3)

    hora17 = CTkLabel(janela, pady = 30)
    hora17.configure(text = "17:00")
    hora17.grid(row = 4, column = 2)
    texto17 = CTkTextbox(janela,height = 10,width = 350, pady = 10)
    texto17.grid(row = 4, column = 3)

    hora18 = CTkLabel(janela, pady = 30)
    hora18.configure(text = "18:00")
    hora18.grid(row = 5, column = 2)
    texto18 = CTkTextbox(janela,height = 10,width = 350, pady = 10)
    texto18.grid(row = 5, column = 3)

    hora19 = CTkLabel(janela, pady = 30)
    hora19.configure(text = "19:00")
    hora19.grid(row = 6, column = 2)
    texto19 = CTkTextbox(janela,height = 10,width = 350, pady = 10)
    texto19.grid(row = 6, column = 3)

    hora20 = CTkLabel(janela, pady = 30)
    hora20.configure(text = "20:00")
    hora20.grid(row = 7, column = 2)
    texto20 = CTkTextbox(janela,height = 10,width = 350, pady = 10)
    texto20.grid(row = 7, column = 3)

    hora21 = CTkLabel(janela, pady = 30)
    hora21.configure(text = "21:00")
    hora21.grid(row = 8, column = 2)
    texto21 = CTkTextbox(janela,height = 10,width = 350, pady = 10)
    texto21.grid(row = 8, column = 3)

    hora22 = CTkLabel(janela, pady = 30)
    hora22.configure(text = "22:00")
    hora22.grid(row = 9, column = 2)
    texto22 = CTkTextbox(janela,height = 10,width = 350, pady = 10)
    texto22.grid(row = 9, column = 3)

    hora23 = CTkLabel(janela, pady = 30)
    hora23.configure(text = "23:00")
    hora23.grid(row = 10, column = 2)
    texto23 = CTkTextbox(janela,height = 10,width = 350, pady = 10)
    texto23.grid(row = 10, column = 3)

    hora24 = CTkLabel(janela, pady = 30)
    hora24.configure(text = "24:00")
    hora24.grid(row = 11, column = 2)
    texto24 = CTkTextbox(janela,height = 10,width = 350, pady = 10)
    texto24.grid(row = 11, column = 3)

    botao_salvar = CTkButton(janela, text = "Salvar Mundanças", command = lambda: get_text(
        texto1,texto2,texto3,texto4,texto5,texto6,texto7,texto8,texto9,texto10,texto11,
        texto12,texto13,texto14,texto15,texto16,texto17,texto18,texto19,texto20,texto21,
        texto22,texto23,texto24,data,False))

    botao_salvar.grid(row = 12, column = 2, pady = 30)

    def fechar():
        janela.destroy()
        exit()

    botao_voltar = CTkButton(janela, text = "Fechar", command = lambda: fechar())
    botao_voltar.grid(row = 12, column = 0, pady = 30)

    janela.mainloop()

