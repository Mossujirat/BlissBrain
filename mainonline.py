import speech_recognition as sr
from playsound import playsound
import thaiword as TH
import socket
import Activity

REMOTE_SERVER = "www.google.com"

def is_connected():
    try:
        host = socket.gethostbyname(REMOTE_SERVER)
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False

def calibrate_mic_energy_threshold():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

def google_snr(lang):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = r.listen(source, phrase_time_limit=2, timeout=10)
        except sr.WaitTimeoutError:
            pass

    try:
        Speech = str(r.recognize_google(audio, language=lang))
        print("You said " + Speech)
        CT = 1
    except sr.RequestError:   # check error
        print("Could not understand audio")
        Speech = False
        CT = 0
    except sr.WaitTimeoutError:
        print("Time Out")
        Speech = False
        CT = 0
    except sr.UnknownValueError:
        print("Unknown Value Error")
        Speech = False
        CT = 0
    except sr.HTTPError:
        print("HTTP Error")
        Speech = False
        CT = 0
    except UnboundLocalError:
        print("UnboundLocalError")
        Speech = False
        CT = 0
    return CT, Speech

def Blissword():
    Bliss = ["bleach", "please", "face", "best", "Bass", "list", "Beast", "Beats", "meat", "with", "bees", "bit", "beef", "beat", "waste"]
    return Bliss

def Hotword(Speech):
    BlissStart = False
    if Speech in Blissword():
        playsound('sound/Alarming/ding.wav')
        BlissStart = True
    return BlissStart

def Command(Speech):
    if Speech in TH.first():
        print("Hello")
        Activity.first()
    elif Speech in TH.second():
        print("Game matching")
        Activity.second()
    elif Speech in TH.third():
        print("Today, you have meeting")
    elif Speech in TH.fourth():
        print("Health question")
        Activity.fourth()
    elif Speech in TH.fifth():
        print("Quiz question")
        Activity.fifth()
    elif Speech in TH.sixth():
        print("Goodbye")
        Activity.sixth()
    elif Speech in TH.seventh():
        print("Number game")
        Activity.seventh()
    elif Speech in TH.eighth():
        print("Remember game")
        Activity.eighth()
    elif Speech in TH.cancel():
        print("cancel")

def Group(Speech):
    if Speech in TH.animal():
        group = 1
    elif Speech in TH.appliance():
        group = 2
    elif Speech in TH.toy():
        group = 3
    elif Speech in TH.fruit():
        group = 4
    elif Speech in TH.cancel():
        group = 0
    else:
        group = 5
    return group

def main():
    while True:
        CT, Speech = google_snr("en-EN")
        if CT == 0:
            print("Speech again")
            calibrate_mic_energy_threshold()
        BlissStart = Hotword(Speech)
        while BlissStart:
            CT, Speech = google_snr("th-TH")
            if CT == 0:
                print("Speech again")
            Command(Speech)

if __name__ == '__main__':
    while True:
        CT, Speech = google_snr("en-EN")
        if CT == 0:
            print("Speech again")
            calibrate_mic_energy_threshold()
        BlissStart = Hotword(Speech)
        while BlissStart:
            CT, Speech = google_snr("th-TH")
            if CT == 0:
                print("Speech again")
            Command(Speech)

