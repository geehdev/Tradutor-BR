
class Reset_Option:

    def reset_for_default(self, **Kwargs):
        """Responsible for restoring program configuration. / 
        Responsável por restaurar a configuração do programa."""

        Kwargs['change_colors'].parser.set('colors', 'window_colors', '#4B0082')
        Kwargs['change_colors'].parser.set('colors', 'buttons_colors', '#7B68EE')

        with open('program_body\my_confing.ini', 'w') as file:
            Kwargs['change_colors'].parser.write(file)

        Kwargs['root_tk'].config(background='#4B0082')
        Kwargs['att_icon_alt']['background'] = '#4B0082'

        Kwargs['btn_clear']['bg'] = '#7B68EE'
        Kwargs['btn_translate']['bg'] = '#7B68EE'
        Kwargs['btn_copy_text']['bg'] = '#7B68EE'
        Kwargs['btn_copy_translation']['bg'] = '#7B68EE'
        