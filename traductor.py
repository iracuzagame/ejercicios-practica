from translate import Translator

traductor = Translator(from_lang='ES', to_lang='EN')

txt = input('Que quieres traducir?: ')
res = traductor.translate(txt)
print(res)