from googletrans import Translator

ceviri = Translator()

cumle = "Hi I am Emre"

ornek = ceviri.translate(cumle,src="en", dest="tr",)
print(ornek.text)



