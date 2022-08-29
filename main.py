from program_body.interface import My_Interface


languages = ['auto','afrikaans','albanian','amharic','arabic','armenian','azerbaijani','basque', 'belarusian', 'bengali','xhosa',
            'bosnian','bulgarian','chinese (simplified)','chinese (traditional)','catalan','cebuano','chichewa','corsican','yiddish',
            'croatian','czech','danish','dutch','english','esperanto','estonian', 'filipino','finnish','french','frisian','yoruba',
            'galician','georgian', 'german','greek', 'gujarati','haitian creole','hausa','hawaiian','hebrew','hebrew','hindi','zulu'
            'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian','irish',  'italian', 'japanese','javanese', 'kannada','yoruba', 
            'kazakh', 'khmer', 'korean', 'kurdish (kurmanji)', 'kyrgyz','lao',  'latin',  'latvian', 'lithuanian',  'luxembourgish', 
            'macedonian','malagasy','malay','malayalam','maltese','maori','marathi', 'mongolian', 'myanmar (burmese)', 'nepali', 
            'norwegian', 'odia', 'portuguese', 'pashto', 'persian', 'polish', 'punjabi', 'romanian', 'russian', 'samoan', 'scots',
            'gaelic', 'serbian', 'sesotho', 'shona','sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 
            'swahili','swedish','tajik','tamil','telugu','thai','turkish','ukrainian','urdu','uyghur','uzbek','vietnamese','welsh',]


# Main Program 

"""Next Version:
1 - transfer languages to a file, 
2 - button to listen to translation
3 - Implement emoticons in messagebox"""


my_program = My_Interface(languages)
my_program.root.mainloop()





# the end :D