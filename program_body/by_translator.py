from googletrans import Translator
from urllib.request import urlopen


class Root_Translate:

    def translate_my_text(self, **Kwargs):
        """Responsible for translating typed text / Responsável por traduzir texto digitado"""
        translator = Translator()

        try:
            if self.connection_is_activated():
                result = translator.translate(text=Kwargs['typed_text'].get(1.0, Kwargs['end_tk']), src=Kwargs['language_01'].get(), dest=Kwargs['language_02'].get())
                Kwargs['att_show_translation']['state'] = Kwargs['normal_tk']
                Kwargs['att_show_translation'].delete(1.0, Kwargs['end_tk'])
                Kwargs['att_show_translation'].insert(Kwargs['end_tk'], chars=result.text)
                Kwargs['att_show_translation']['state'] = Kwargs['disabled_tk']
            else:
                Kwargs['mb_tk'].showerror(title='No internet connection', message='Connect to the internet and try again.', icon='error')
        except IndexError:
                pass
        

    def connection_is_activated(self):
        """ check if the internet is activa / verifica se a internet está ativa"""
        try:
            urlopen(url='https://translate.google.com/', timeout=3)
            return True
        except:
            return False