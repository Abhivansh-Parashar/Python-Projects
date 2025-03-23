import pyttsx3
import PyPDF2
def pdf_to_audio(pdf_path,ouptut_audio):
    try:
        with open(pdf_path,'rb') as pdf_file:
            reader=PyPDF2.PdfReader(pdf_file)
            text=""

            for page in reader.pages:
                text+=page.extract_text()+"\n"
            
            if not text.strip():
                print("The pdf file is empty")
                return
            
            engine=pyttsx3.init()
            engine.save_to_file(text,ouptut_audio)
            engine.runAndWait()
            print("The audio file has been created successfully")
    except Exception as e:
        print("An error occurred: ",e)

pdf_to_audio(input("Enter the path of the pdf file: "),input("Enter the name of the output audio file: "))