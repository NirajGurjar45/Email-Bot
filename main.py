import smtplib
import speech_recognition as sr
import pyttsx3
from  email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('Listening....')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('gurjarniraj467@gmail.com', 'Pass@niraj1')
    email = EmailMessage()
    email['From'] = 'gurjarniraj467@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)






email_list = {
    'niraj': 'nirajgurjar4444@gmail.com',
    'kaushal': 'kaushalpatil02019@gmail.com',
    'sumit': 'sumit@gmail.com',
    'pramod': 'pramod.gurjar@gmail.com',
    'vedant': 'vedant@gmail.com',
    'bhushan': 'bhushan@gmail.com',
}




def get_email_info():
    talk('To Whom you want to send email, Sir?')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email, Sir?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Hey lazy Dude, Your Email is Sent!!')
    talk('Do You Want To Send More Email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()

get_email_info()