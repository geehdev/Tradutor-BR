from tkinter import ttk, messagebox as mb, Text
from tkinter import  *
from tkinter.colorchooser import askcolor

 
from program_body.parser_colors import Change_Colors 
from program_body.reset_config import Reset_Option
from program_body.by_translator import Root_Translate

# Main_Program - Constants
PROGRAM_TITLE = 'Tradutor BR'
DIMENSIONS_SCREEN = '320x680+450+5'

class My_Interface:
    def __init__(self, languages):
        self.root = Tk()

        self.languages = languages

        self.root.title(PROGRAM_TITLE)
        self.root.geometry(DIMENSIONS_SCREEN)
        self.root.resizable(False, False)

        self.change_colors = Change_Colors()
        self.reset_option = Reset_Option()
        self.root_translate = Root_Translate()

        self.root.config(background=self.change_colors.wind_color)
    
        self.start_icons()
        self.widget_text_label()
        self.widgets_buttons()
        self.widgets_combobox()
        self.widget_menu_bar()

    def start_icons(self):
        """Contains the Brazil flag icons and toggle. / Contém os ícones da bandeira do Brasil e alternar. """
        path_icon_brasil = PhotoImage(file='program_body\Icons\iconbrasil.png')
        self.path_icon_alt = PhotoImage(file='program_body\Icons\iconAlt.png')

        self.root.iconphoto(False, path_icon_brasil)

        self.label_icon_alt = Label(self.root, width=20, image=self.path_icon_alt, background=self.change_colors.wind_color)
        self.label_icon_alt.place(x=149, y=257)


    def copy_to_clipboard(self, option=True):
        """ Copy texts to clipboard / Copia textos para área de transferência \n
        Arg:
            True == Copy typed text \n
            False == Copy text Translated. """
        if option: 
            self.root.clipboard_clear()
            self.typed_text.clipboard_append(self.typed_text.get(1.0, END))
        else:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.show_translation.get(1.0, END))


    def clean_widgets(self):
        """ Clears text widgets, changing attribute state / Limpa os widgets de texto, alterando o estado dos atributos """
        self.typed_text.delete(1.0, END)
        self.show_translation['state'] = NORMAL
        self.show_translation.delete(1.0, END)
        self.show_translation['state'] = DISABLED


    def widgets_combobox(self):
        """Contains Combobox tkinter widgets."""

        self.language_01 = ttk.Combobox(self.root, values=self.languages)
        self.language_01.place(x=5, y=256, width=141, height=22)
        self.language_01.set('auto')

        self.language_02 = ttk.Combobox(self.root, values=self.languages)
        self.language_02.place(x=176, y=256, width=139, height=22)
        self.language_02.set('portuguese')


    def widget_text_label(self):
        """Contains Text and Label widgets. / Contém widgets Text e Label."""

        Label(self.root, text='Type Something', background='#00CED1', anchor=CENTER).place(x=5, y=35, width=310, height=22)
        
        self.typed_text = Text(self.root, background='#dde', font=('Courier', 10), state=NORMAL)
        self.typed_text.place(x=5, y=55, width=310, height=200)

        self.show_translation = Text(self.root, background='#dde', font=('Courier', 10), state=DISABLED)
        self.show_translation.place(x=5, y=307, width=310, height=322)
        

    def widgets_buttons(self):
        """Contains button widgets / Contém widgets botões"""

        self.btn_clean_all = Button(self.root, text='Clean All', bg=self.change_colors.butt_color, anchor=CENTER, command= self.clean_widgets)

        self.btn_translate = Button(self.root, text='Translate Text', bg=self.change_colors.butt_color, anchor=CENTER,
                            command=lambda: self.root_translate.translate_my_text(typed_text=self.typed_text, language_01=self.language_01, language_02=self.language_02,
                                                                                  end_tk=END, normal_tk=NORMAL, disabled_tk=DISABLED, mb_tk=mb, att_show_translation=self.show_translation)
                                    )
        
        self.btn_copy_text = Button(self.root, text='Copy Typed Text', bg=self.change_colors.butt_color, anchor=CENTER, command=lambda: self.copy_to_clipboard(option=True))
        
        self.btn_copy_tranlation = Button(self.root, text='Copy Translation', bg=self.change_colors.butt_color, anchor=CENTER, command=lambda: self.copy_to_clipboard(option=False))
    

        #button placement / posicionamento dos botãos
        self.btn_clean_all.place(x=5, y=7, width=310 , height=20)
        self.btn_translate.place(x=5, y=282, width=310, height=22)
        self.btn_copy_text.place(x=5, y=635 , width=150 , height=20)
        self.btn_copy_tranlation.place(x=166 , y=635 , width=150 , height=20)


    def widget_menu_bar(self):
        """Contain Menu widget / Contém widgets de Menu"""

        self.root_bar_menu = Menu(self.root, foreground='#7CFC00')

        menuArquivo = Menu(self.root_bar_menu, tearoff=0)
        
        self.root_bar_menu.add_cascade(labe='Section', menu=menuArquivo)

        menuArquivo.add_command(label='Exit', activebackground='#d43215', activeforeground='#ffffff', 
                                command=lambda: self.root.quit() if mb.askyesno(title='Close program ', message='Are you sure you want to close the program?') == True else '')

        my_options = Menu(self.root_bar_menu, tearoff=0)

        self.root_bar_menu.add_cascade(label='Edit', menu=my_options)

        my_options.add_command(label='Background Color', activebackground='#8f9b9c', activeforeground='#fbff08',
                            command=lambda: self.change_colors.window_color(askcolor_tk=askcolor, root_tk=self.root, att_icon_alt=self.label_icon_alt)
                            )

        my_options.add_command(label='Button Color', activebackground='#8f9b9c', activeforeground='#6bff08',
                            command=lambda: self.change_colors.color_buttoes(askcolor_tk=askcolor, btn_clear=self.btn_clean_all, btn_translate=self.btn_translate,
                                                                             btn_my_text=self.btn_copy_text, btn_translation=self.btn_copy_tranlation)
                            )


        my_options.add_command(label='Reset Config', activebackground='#8f9b9c', activeforeground='#73086c', 
                            command=lambda: self.reset_option.reset_for_default(change_colors=self.change_colors, root_tk=self.root, att_icon_alt=self.label_icon_alt,
                                                                                btn_clear=self.btn_clean_all, btn_translate=self.btn_translate, btn_copy_text=self.btn_copy_text,
                                                                                btn_copy_translation=self.btn_copy_tranlation)
                                )

        self.root.config(menu=self.root_bar_menu, background=self.change_colors.wind_color)
