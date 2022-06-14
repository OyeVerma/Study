from googletrans import Translator, LANGUAGES

t = Translator()
h = t.translate('This is apple', 'hi')
print(h)