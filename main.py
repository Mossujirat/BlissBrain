import mainoffline
import mainonline
import socket
import time
from playsound import playsound
REMOTE_SERVER = "www.google.com"

def is_connected():
    try:
        host = socket.gethostbyname(REMOTE_SERVER)
        socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False

if __name__ == '__main__':
    time.sleep(5)
    while True:
        while is_connected():
            print("Online speech recognition")
            try:
                playsound('sound/Alarming/dong.wav')
                mainonline.main()
            except:
                pass
        while not is_connected():
            print("Offline speech recognition")
            try:
                mainoffline.main()
            except:
                pass


