import pyttsx3
import PyPDF2

book = open('Algorithms.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print("Number of pages of this book are", pages)




speaker = pyttsx3.init()
pageporbo = pdfReader.getPage(44)
text = pageporbo.extractText()
speaker.say(text)
speaker.runAndWait()