# from tkinter import colorchooser
from configparser import ConfigParser


class Change_Colors:
        def __init__(self):
                self.parser = ConfigParser()
                self.file_data = self.parser.read(filenames='program_body\my_confing.ini') 

                self.wind_color = self.parser.get('colors', 'window_colors')
                self.butt_color = self.parser.get('colors', 'buttons_colors')


        def window_color(self, **Kwargs):
                """Change tkinter window background, alt icon background. Finally, save the new color in my_config. /  
                        Altera background da janela tkinter, background do ícone alt. Por fim, salva a nova cor no my_confing."""
                try:
                        new_color = Kwargs['askcolor_tk']()[1]
                        
                        Kwargs['root_tk'].config(background=new_color)
                        Kwargs['att_icon_alt']['background'] = new_color

                        self.parser.set('colors', 'window_colors', new_color)

                        with open('program_body\my_confing.ini', 'w') as file:
                                self.parser.write(file)

                except TypeError:
                        pass


        def color_buttoes(self, **Kwargs):
                """Change the background of the tkinter buttons widgets, finally, save the new color in my_config. /
                   Altera background dos widgets botões tkinter, por fim, salva a nova cor no my_confing."""
                try:
                        new_color = Kwargs['askcolor_tk']()[1]

                        Kwargs['btn_clear']['bg'] = new_color
                        Kwargs['btn_translate']['bg'] = new_color
                        Kwargs['btn_my_text']['bg'] = new_color
                        Kwargs['btn_translation']['bg'] = new_color

                        self.parser.set('colors', 'buttons_colors', new_color)

                        with open('program_body\my_confing.ini', 'w') as file:
                                self.parser.write(file)
                except TypeError:
                        pass
