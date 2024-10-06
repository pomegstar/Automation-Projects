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




## Updated version (command line interface):---------------------------------------------------------------------------------------------------------------------------------------

# import pyttsx3
# import PyPDF2
# speaker = pyttsx3.init()

# # # pdf to speech
# def pdfToSpeech(fname, startp, endp, dpath):
#     book = open(fname, 'rb')
#     pdfReader = PyPDF2.PdfReader(book)
#     pages = len(pdfReader.pages)

#     for num in range(startp, endp):
#         page = pdfReader.pages[num]
#         text = page.extract_text()
#         # speaker.say(text)
#         rate = speaker.getProperty('rate')
#         speaker.setProperty('rate', rate-20)
#         speaker.save_to_file(text, dpath) # dpath = destination path
#         speaker.runAndWait()
#     return f'Successfully converted from PDF to speech'


# # # Text file (.txt) to speech (.mp3)
# def txtToSpeech(fname, dpath):
#     with open(fname, 'r', encoding='utf-8') as file:
#         txt = file.read()
#     rate = speaker.getProperty('rate')
#     speaker.setProperty('rate', rate-20)
#     speaker.save_to_file(txt, dpath)
#     speaker.runAndWait()
#     return f'Successfully converted from text to speech'

# # # Speed test
# def speed_test(volume=0):
#     rate = speaker.getProperty('rate')
#     speaker.setProperty('rate', rate+int(volume))
#     print(f"Current-speed: {rate+int(volume)}")
#     speaker.say('The quick brown fox jumped over the lazy dog.')
#     speaker.runAndWait()


# def main():
#     print('1. PDF to Speech\n2. Text to Speech\n3. Speed Test')
#     choice = int(input('Enter your choice: '))
#     if choice == 1:
#         fname = input('Enter the pdf file name with the path: ')
#         startp = int(input("Give the start page number: "))
#         endp = int(input("Give the end page number: "))
#         dpath = input('Enter the destination path with the file name: ')
#         print(pdfToSpeech(fname, startp, endp, dpath))
#     elif choice == 2:
#         fname = input('Enter the txt file name with the path: ')
#         dpath = input('Enter the destination path with the file name: ')
#         print(txtToSpeech(fname, dpath))
#     elif choice == 3:
#         volume = input("Enter the volume ('+' or '-' integer): ")
#         speed_test(volume)
#     else:
#         print('Invalid choice!')


# if __name__ == '__main__':
#     main()
