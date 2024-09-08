import pdfplumber as pp
from gtts import gTTS

# extract text from pdf
pdf_text = ""

with pp.open("tuesdays with morrie.pdf") as pdf:
    print("Initiating Extraction...")
    # loop through individual pages
    for page in pdf.pages: 
        pdf_text += page.extract_text()

try: 
    print("Initiating Conversion...")
    # convert extracted text to speech
    tts = gTTS(text=pdf_text, lang='en')
    tts.save('tuesdays_w_m.mp3')
    print("Audio file successfully saved")

except Exception as e: 
    print(f"An error occured: {e}")