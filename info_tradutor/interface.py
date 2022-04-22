from tkinter import Tk, PhotoImage, Menu, Text, Label, Button, messagebox, END
from tkinter.colorchooser import askcolor
from tkinter.ttk import Combobox
from funcoes import *

# programa principal - deve iniciar esse arquivo para o programa iniciarr
# programa principal - deve iniciar esse arquivo para o programa iniciarr

root = Tk()
root.title('Tradutor BR')
root.geometry('320x680+450+5')
root.resizable(False, False) # ATENÇÃO - NO MOMENTO NÃO SERÁ POSSÍVEL EXPANDIR.

Label(root, text='Digite Algo', background='#00CED1', anchor='center').place(x=5, y=35, width=310, height=22)

digite_algo = Text(root, background='#dde', font=('Courier', 10), state='normal')
digite_algo.place(x=5, y=55, width=310, height=200)

icone_jane = PhotoImage(file='icones\iconbrasil.png') 
root.iconphoto(False, icone_jane)

icon_alterar = PhotoImage(file='icones\iconAlt.png')
lab_icon_alterar = Label(root, width=20, image=icon_alterar, background=config_cor_janela)
lab_icon_alterar.place(x=149, y=257)

opc_idiomas_01 = Combobox(root, values=languages, background='#00CED1' )
opc_idiomas_01.place(x=5, y=256, width=141, height=22)
opc_idiomas_01.set('auto')

opc_idiomas_02 = Combobox(root, values=languages, background='#fcb103')
opc_idiomas_02.place(x=176, y=256, width=139, height=22)
opc_idiomas_02.set('portuguese')

traducao = Text(root, background='#dde', font=('Courier', 10), state='disabled')
traducao.place(x=5, y=307, width=310, height=322)

limpar_btn = Button(root, text='Limpar Tudo', background=config_cor_botoes,  anchor='center', command=lambda: limparTudo(digite_algo, traducao, END))
btn_traduzir = Button(root, text='Traduzir', background=config_cor_botoes, anchor='center', command=lambda: xtraduzir(digite_algo, opc_idiomas_01, opc_idiomas_02, traducao, messagebox, END))
btn_copiar_01 = Button(root, text='Copiar Texto Digitado', background=config_cor_botoes, anchor='center', command=lambda: copiar_01(root, digite_algo, END))
btn_copiar_02 = Button(root, text='Copiar Texto Traduzido', background=config_cor_botoes, anchor='center', command=lambda: copiar_02(root))

limpar_btn.place(x=5, y=7, width=310 , height=20)
btn_traduzir.place(x=5, y=282, width=310, height=22)
btn_copiar_01.place(x=5, y=635 , width=150 , height=20)
btn_copiar_02.place(x=166 , y=635 , width=150 , height=20)

barraDeMenu = Menu(root, foreground='#7CFC00')
menuArquivo = Menu(barraDeMenu, tearoff=0)

barraDeMenu.add_cascade(labe='Seção', menu=menuArquivo)
menuArquivo.add_command(label='Sair', activebackground='#d43215', activeforeground='#ffffff', command=lambda: xMessagebox_sair(root, messagebox))

opc_editar = Menu(barraDeMenu, tearoff=0)
barraDeMenu.add_cascade(label='Editar', menu=opc_editar)

opc_editar.add_command(label='Cor de Fundo', activebackground='#8f9b9c', activeforeground='#fbff08', command=lambda: alterar_cor_janela(askcolor, root, lab_icon_alterar))
opc_editar.add_command(label='Cor dos botões', activebackground='#8f9b9c', activeforeground='#6bff08', command=lambda: alterar_cor_btn(askcolor, limpar_btn, btn_traduzir, btn_copiar_01, btn_copiar_02))
opc_editar.add_command(label='Restaurar configuração', activebackground='#8f9b9c', activeforeground='#73086c', command=lambda: restuarar_config(root, lab_icon_alterar, limpar_btn, btn_traduzir, btn_copiar_01, btn_copiar_02))

root.config(menu=barraDeMenu, background=config_cor_janela)
root.mainloop()
