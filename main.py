from translate import Translator

translator = Translator(to_lang='French')

#translation = translator.translate("Hello, how are you?")

sentence = input("Enter your sentence: ")

translation = translator.translate(sentence)

print(translation)