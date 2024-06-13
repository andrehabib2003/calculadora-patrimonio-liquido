from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk

# Cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde 1
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = "#e06636"  # profit
co6 = "#038cfc"  # azul
co7 = "#3fbfb9"  # verde 2
co8 = "#263238"  # verde 3
co9 = "#e9edf5"  # verde 4
co10 = "#6e8faf"
co11 = "#f2f4f2"

# Criando janela
window = Tk()
window.title("Calculadora de patrimônio liquído")
window.geometry("380x500")
window.configure(background=co1)
window.resizable(width=False, height=False)

style = ttk.Style(window)
style.theme_use("clam")

# Frames
frameUp = Frame(window, width=380, height=50, bg=co1)
frameUp.grid(row=0, column=0, columnspan=2)

frameResult = Frame(window, width=380, height=50, bg=co3)
frameResult.grid(row=1, column=0, columnspan=2, pady=0)

frameDown = Frame(window, width=380, height=400, bg=co1)
frameDown.grid(row=2, column=0, columnspan=2, pady=10)

# Divisão do frameDown
frameAssets = Frame(frameDown, width=180, height=380, bg=co9)  # Ativos
frameAssets.grid(row=0, column=0, padx=2.5)

frameLiabilities = Frame(frameDown, width=180, height=380, bg=co9)  # Passivos
frameLiabilities.grid(row=0, column=1, padx=2.5)

# Logo
app_img = Image.open('patrimonio.png')
app_img = app_img.resize((50, 50))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameUp, image=app_img, width=900, compound=LEFT, padx=5, anchor=NW, bg=co1, fg=co4)
app_logo.place(x=5, y=0)

app_title = Label(frameUp, text="Patrimônio Líquido", width=900, compound=CENTER, padx=5, anchor=NW, font="Arial 14", bg=co1, fg=co4)
app_title.place(x=105, y=15)


# Função Patrimônio liquído
def calculate():
    # Ativos
    asset_1 = e_realty_value.get()
    asset_2 = e_savings_value.get()
    asset_3 = e_vehicle_value.get()
    asset_4 = e_investments_value.get()
    asset_5 = e_otherAssets_value.get()

    # Passivos
    liability_1 = e_mortgage_value.get()
    liability_2 = e_loans_value.get()
    liability_3 = e_financing_value.get()
    liability_4 = e_otherDebts_value.get()

    if asset_1 == "" or asset_2 == "" or asset_3 == "" or asset_4 == "" or asset_5 == "" or liability_1 == "" or liability_2 == "" or liability_3 == "" or liability_4 == "":
        print("Entrada inválida. Verifique se deixou algum campo vazio.")
        return
    else:
        Total_assets = float(asset_1) + float(asset_2) + float(asset_3) + float(asset_4) + float(asset_5)
        Total_liabilities = float(liability_1) + float(liability_2) + float(liability_3) + float(liability_4)

        net_worth = Total_assets - Total_liabilities

        l_result['text'] = 'R${:,.2f}'.format(net_worth)


# Entrada de ativos
l_name = Label(frameAssets, text="Ativos", padx=10, width=35, height=1, anchor=NW, font="Verdana 11", bg=co2, fg=co1)
l_name.place(x=0, y=0)

# Valor de imóveis
l_name = Label(frameAssets, text="Imóveis", anchor=E, font="Verdana 9", bg=co9, fg=co0)
l_name.place(x=10, y=40)

e_realty_value = Entry(frameAssets, width=15, font="Ivy 12", justify="center", relief="solid")
e_realty_value.place(x=10, y=65)

# Valor de poupança
l_name = Label(frameAssets, text="Valor em poupanças", anchor=E, font="Verdana 9", bg=co9, fg=co0)
l_name.place(x=10, y=100)

e_savings_value = Entry(frameAssets, width=15, font="Ivy 12", justify="center", relief="solid")
e_savings_value.place(x=10, y=125)

# Valor de veículos
l_name = Label(frameAssets, text="Veículos", anchor=E, font="Verdana 9", bg=co9, fg=co0)
l_name.place(x=10, y=160)

e_vehicle_value = Entry(frameAssets, width=15, font="Ivy 12", justify="center", relief="solid")
e_vehicle_value.place(x=10, y=185)

# Valor de investimentos
l_name = Label(frameAssets, text="Investimentos", anchor=E, font="Verdana 9", bg=co9, fg=co0)
l_name.place(x=10, y=220)

e_investments_value = Entry(frameAssets, width=15, font="Ivy 12", justify="center", relief="solid")
e_investments_value.place(x=10, y=245)

# Valor de outros ativos
l_name = Label(frameAssets, text="Outros ativos", anchor=E, font="Verdana 9", bg=co9, fg=co0)
l_name.place(x=10, y=280)

e_otherAssets_value = Entry(frameAssets, width=15, font="Ivy 12", justify="center", relief="solid")
e_otherAssets_value.place(x=10, y=305)


# Entrada de passivos
l_name = Label(frameLiabilities, text="Passivos", padx=10, width=35, height=1, anchor=NW, font="Verdana 11", bg=co5, fg=co1)
l_name.place(x=0, y=0)

# Valor de hipoteca
l_name = Label(frameLiabilities, text="Hipoteca", anchor=E, font="Verdana 9", bg=co9, fg=co0)
l_name.place(x=10, y=40)

e_mortgage_value = Entry(frameLiabilities, width=15, font="Ivy 12", justify="center", relief="solid")
e_mortgage_value.place(x=10, y=65)

# Valor de empréstimos
l_name = Label(frameLiabilities, text="Empréstimos", anchor=E, font="Verdana 9", bg=co9, fg=co0)
l_name.place(x=10, y=100)

e_loans_value = Entry(frameLiabilities, width=15, font="Ivy 12", justify="center", relief="solid")
e_loans_value.place(x=10, y=125)

# Valor de financiamentos
l_name = Label(frameLiabilities, text="Financiamentos", anchor=E, font="Verdana 9", bg=co9, fg=co0)
l_name.place(x=10, y=160)

e_financing_value = Entry(frameLiabilities, width=15, font="Ivy 12", justify="center", relief="solid")
e_financing_value.place(x=10, y=185)

# Valor de outras dívidas
l_name = Label(frameLiabilities, text="Outras dívidas", anchor=E, font="Verdana 9", bg=co9, fg=co0)
l_name.place(x=10, y=220)

e_otherDebts_value = Entry(frameLiabilities, width=15, font="Ivy 12", justify="center", relief="solid")
e_otherDebts_value.place(x=10, y=245)

# Resultado
l_result = Label(frameResult, text='R${:,.2f}'.format(00), padx=10, width=15, anchor=NE, font="Verdana 25 bold", bg=co3, fg=co1)
l_result.place(x=0, y=7)

button_calculate = Button(frameLiabilities, command=calculate, text="Calcular", padx=10, width=12, anchor=CENTER, font="Ivy 12 bold", bg=co1, fg=co0)
button_calculate.place(x=10, y=300)


# Programa
window.mainloop()
