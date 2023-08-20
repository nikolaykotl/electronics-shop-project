from src.item import Item
class MixinLang:

    def change_lang(self):
        if self.language == 'EN':
            return 'RU'
        elif self.language == 'RU':
            return 'EN'

class Keyboard(MixinLang, Item):

    def __init__(self, name, price, quantity, language ='EN'):
        super().__init__(name, price, quantity)
        self.__language = language

    def change_lang(self):
        self.__language = super().change_lang()
        return self

    @property
    def language(self):
        return self.__language

    def __str__(self):
       return f'{self.name}'
