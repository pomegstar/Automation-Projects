import pyttsx3
import PyPDF2
#fname = input('Enter the txt file name with the path: ')
speaker = pyttsx3.init()

# # pdf to speech
fname = input('Enter the pdf file name with the path: ')
startp = int(input("Give the start page number: "))
endp = int(input("Give the end page number: "))
book = open(fname, 'rb')
pdfReader = PyPDF2.PdfReader(book)
pages = len(pdfReader.pages)

for num in range(startp, endp):
    page = pdfReader.pages[num]
    text = page.extract_text()
    # speaker.say(text)
    rate = speaker.getProperty('rate')
    speaker.setProperty('rate', rate-20)
    speaker.save_to_file(text, r'E:\Nazmul\Music\pdfTest.mp3')
    speaker.runAndWait()
print(f'Successfully converted from PDF to speech')


# # Text file (.txt) to speech (.mp3)

# with open(fname, 'r', encoding='utf-8') as file:
#         txt = file.read()
# rate = speaker.getProperty('rate')
# speaker.setProperty('rate', rate-20)
# speaker.save_to_file(txt, r'E:\Nazmul\Music\txtTest.mp3')
# speaker.runAndWait()
# print(f'Successfully converted from text to speech')

#speed_test
# rate = speaker.getProperty('rate')
# print(rate)
# speaker.setProperty('rate', rate-20)
# speaker.say('The quick brown fox jumped over the lazy dog.')
# speaker.runAndWait()
