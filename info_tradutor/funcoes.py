
from googletrans import Translator
from urllib import request
from configparser import ConfigParser

google_trans = Translator()

analisador = ConfigParser()
analisador.read('info_tradutor/config.ini')

config_cor_janela = analisador.get('cores', 'cor_janela')
config_cor_botoes = analisador.get('cores', 'cor_botoes')


languages = ['auto', 'afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali', 'bosnian', 'bulgarian', 'chinese (simplified)', 'chinese (traditional)', 'catalan', 'cebuano', 
            'chichewa', 'corsican', 'croatian', 'czech', 'danish', 'dutch', 'english', 'esperanto', 'estonian', 'filipino', 'finnish', 'french', 'frisian', 'galician','georgian', 'german','greek', 'gujarati','haitian creole', 
            'hausa', 'hawaiian', 'hebrew',  'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish',  'italian', 'japanese','javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'kurdish (kurmanji)', 
            'kyrgyz',  'lao',  'latin',  'latvian', 'lithuanian',  'luxembourgish',  'macedonian', 'malagasy', 'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)', 'nepali', 'norwegian', 'odia', 
            'portuguese', 'pashto', 'persian', 'polish', 'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona','sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 
            'swedish', 'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'ukrainian', 'urdu', 'uyghur', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu']


def xtraduzir(var_digite_algo, var_opc_idiomas_01, var_opc_idiomas_02, var_traducao, mesagebox_tk, END_tk):
    """ responsável por traduzir o texto digitado, retorna a tradução """
    global result
    texto_digitado = var_digite_algo.get(1.0, END_tk)
    nativo_idioma = var_opc_idiomas_01.get()
    destino_idioma = var_opc_idiomas_02.get()

    try:
        request.urlopen(url='https://translate.google.com/', timeout=5)
    except:
        mesagebox_tk.showerror(title='Tradutor BR', message='Você está sem internet. ')

    try: # responsável por traduzir o texto digitado, dest = texto traduzido / src = identifica o idioma de origem
        result = google_trans.translate(text=texto_digitado, dest=destino_idioma, src=nativo_idioma)
    except:
        return

    var_traducao['state'] = 'normal' 
    var_traducao.delete(1.0, END_tk)
    var_traducao.insert(END_tk, result.text)
    var_traducao['state'] = 'disabled'


def xMessagebox_sair(var_root, mesagebox_tk):
    """retorna uma mensagem de alerta ao apertar o botão de sair, localizado na barra de menu"""
    msgbox = mesagebox_tk.askyesno(title='Tradutor BR', message='Tem certeza que deseja sair?')
    if msgbox == True:
        var_root.quit()


def copiar_01(var_root, var_digite_algo, END_tk):
    """copia o texto digitado para área de transferência - CTRL+C"""
    var_root.clipboard_clear()
    var_root.clipboard_append(var_digite_algo.get(1.0, END_tk))


def copiar_02(var_root):
    """copia a tradução para área de transferência - CTRL+C"""
    try:
        var_root.clipboard_clear()
        var_root.clipboard_append(result.text)
    except:
        return


def limparTudo(var_digite_algo, var_traducao, END_tk):
    """responsável por limpar os textos."""
    var_digite_algo.delete(1.0, END_tk)
    var_traducao['state'] = 'normal'
    var_traducao.delete(1.0, END_tk)
    var_traducao['state'] = 'disable'


def alterar_cor_janela(askcolor_tk, var_root, var_lab_icon_alterar):
    """Responsável pro alterar a cor da janela tkinter, salva a nova cor no arquivo config. """
    try:
        id_cor = askcolor_tk()[1]
        
        var_root.config(background=id_cor)
        var_lab_icon_alterar['background'] = id_cor

        analisador.set('cores', 'cor_janela', id_cor)

        with open('info_tradutor/config.ini', 'w') as file:
            analisador.write(file)     
    except TypeError:
        pass


def alterar_cor_btn(askcolor_tk, var_limpar_btn , var_btn_traduzir, btn_copiar_01, btn_copiar_02):
    """Responsável pro alterar a cor dos botões, salva a nova cor no arquivo config. """
    try:
        id_cor = askcolor_tk()[1]

        var_limpar_btn ['background'] = id_cor
        var_btn_traduzir['background'] = id_cor
        btn_copiar_01['background'] = id_cor
        btn_copiar_02['background'] = id_cor

        analisador.set('cores', 'cor_botoes', id_cor)

        with open('info_tradutor/config.ini', 'w') as file:
            analisador.write(file)
    except TypeError:
        pass


def restuarar_config(root_TK, var_lab_icon_alterar, var_limpar_btn, btn_traduzir, btn_copiar_01, btn_copiar_02):
    """Responsável por restaurar a configuração do programa."""
    analisador.set('cores', 'cor_janela', '#4B0082')
    analisador.set('cores', 'cor_botoes', '#7B68EE')

    with open('info_tradutor/config.ini', 'w') as file:
        analisador.write(file)

    root_TK.config(background='#4B0082')

    var_limpar_btn ['background'] = '#7B68EE'

    btn_traduzir['background'] = '#7B68EE'
    btn_copiar_01['background'] = '#7B68EE'
    btn_copiar_02['background'] = '#7B68EE'

    var_lab_icon_alterar['background'] = '#4B0082'