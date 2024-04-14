from PyPDF2 import PdfReader 
import pyttsx3


# open the pdf file get the given page text.
reader = PdfReader(r"D:\10_PYTHON PROJECTS\PDF-READER\test2.pdf")
page = reader.pages[4]
text = page.extract_text()

# read the text.
engin = pyttsx3.init()

# save the audio file.
engin.save_to_file("test", "test.mp3")

# change the voice.
voices = engin.getProperty("voices")
engin.setProperty("voice",voices[1].id)
engin.say(text)

# run the code.
engin.runAndWait()