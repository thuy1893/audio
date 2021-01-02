import pyttsx3
import PyPDF2
book = open("oop.pdf", "rb") #the rb is for reading as a binary book

pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
print(pages) # to check how many pages there are in the pdf file

speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
for voice in voices:
	if voice.languages[0] == b'\x05en-uk-rp':
		speaker.setProperty('voice', voice.id)
speaker.setProperty('rate', 160)

page = pdfreader.getPage(0) #to ask it to read from a certain page, for example here, from page 8 (started at 0)
#extract the text from the above:
text = page.extractText()
speaker.say(text)
speaker.runAndWait()
