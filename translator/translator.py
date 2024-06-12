
import googletrans
from googletrans import Translator
import pandas as pd


class textTranslator():
    
    def __init__(self,text,language = 'cn'):
        self.text = text
        self.language = language
        self.__translate_test()
        
    
    def __translate_test(self):
        translator = Translator()
        self.text = translator.translate(self.text, self.language).text
    
    def get_text(self):
        return self.text

class ExcelFile():
    def __init__(self):
        self.country_languages = googletrans.LANGUAGES
        self.fileName = self.country_languages.items()
        self.country_names = self.country_languages.values()
        self.country_shortNames = self.country_languages.keys()
        # self.excel_file = pd.read_excel(self.fileName)
        self.__excel_file()

    def __excel_file(self):
        
        for name in self.country_names:
            print(name)
    def get_country_names(self):
        return self.country_languages

def main():
    country_names = ExcelFile().get_country_names()
    text = input("Enter the text here: ")
    language = input("Enter the language from above here: ")
    try:
        # shortName = language
        for key, value in country_names.items():

            if language.lower() == value.lower():
                shortName = key
    except:
        print("\nKindly, the language from below list of languages\n")
        for name in country_names.values():
            print(name)
        main()

    text_translator = textTranslator(text, shortName)
    translated_text = text_translator.get_text()
    print(f"\nThe translated text is \n{translated_text}")

if __name__ == '__main__':
    main()


