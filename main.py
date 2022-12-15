import pyttsx3
import PyPDF2

book= open('harry_potter_annd_the_sorcerers_stone.pdf', 'rb')
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfreader.getPage(8)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()

#reading whole book
# for num in range (8, 9):
#     page = pdfreader.getPage(8)
#     text = page.extractText()
#     speaker.say(text)
#     #speaker.say('Hello')
#     speaker.runAndWait()