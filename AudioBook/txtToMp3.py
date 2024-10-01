import pyttsx3
fname = input('Enter the pdf file name with the path: ')
speaker = pyttsx3.init()


# .pdf to .mp3

# import PyPDF2
# startp = int(input("Which pages do you wanna listen?: "))
# endp = int(input("Give the end page: "))
# book = open(fname, 'rb')
# pdfReader = PyPDF2.PdfReader(book)
# pages = len(pdfReader.pages)

# for num in range(startp, endp):
#     page = pdfReader.pages[num]
#     text = page.extract_text()
#     # speaker.say(text)
#     speaker.save_to_file(text, 'C:\Users\Nazmul\Documents\jtest.mp3')
#     speaker.runAndWait()



# Text file (.txt) to speech (.mp3)

with open(fname, 'r', encoding='utf-8') as file:
        txt = file.read()
rate = speaker.getProperty('rate')
speaker.setProperty('rate', rate-20)
speaker.save_to_file(txt, 'test.mp3')
speaker.runAndWait()

#speed_test
# rate = speaker.getProperty('rate')
# print(rate)
# speaker.setProperty('rate', rate-20)
# speaker.say('The quick brown fox jumped over the lazy dog.')
# speaker.runAndWait()
