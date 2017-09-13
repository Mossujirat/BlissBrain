import BlissAnn
from record import record_to_file
import time
import Activity as Activity
from playsound import playsound
import socket
BlissCommand = False
REMOTE_SERVER = "www.google.com"

def is_connected():
    try:
        host = socket.gethostbyname(REMOTE_SERVER)
        socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False

def listen():
    filename = "test_files/test.wav"
    while True:
        try:
            record_to_file(filename)
            break
        except (RuntimeError, TypeError, NameError, AttributeError, FileNotFoundError):
            print("Error!!!!")
    return filename

def process(filename):
    # Feed into ANN
    testNet = BlissAnn.testInit()
    inputArray = BlissAnn.extractFeature(filename)
    print(len(inputArray))
    outStr, indexMax = BlissAnn.feedToNetwork(inputArray,testNet)
    return outStr, indexMax

def command_f1(cnum): # Change command to hotword = Bliss
    # find command
    if cnum == 0:
        print("You said Bliss")
        playsound('sound/alarming/ding.wav')
        BlissCommand = True
    else:
        print("Said again")
        BlissCommand = False
    return BlissCommand

def command_f2(cnum): # Change command_f2 to greeting mode
    # find command
    if cnum == 1:
        print("You said sawandee")
        Activity.first()
        BlissCommand = True
    elif cnum == 2:
        print("Matching card")
        Activity.second()
        BlissCommand = True
    elif cnum == 3:
        print("Activity")
        Activity.third()
        BlissCommand = True
    elif cnum == 4:
        print("Healthy Question")
        Activity.fourth()
        BlissCommand = True
    elif cnum == 5:
        print("Quiz")
        Activity.fifth()
        BlissCommand = True
    elif cnum == 6:
        print("Goodbye")
        Activity.sixth()
        BlissCommand = False
    elif cnum == 7:
        print("Number Question")
        Activity.seventh()
        BlissCommand = True
    elif cnum == 8:
        print("Remember Question")
        Activity.eighth()
        BlissCommand = True
    else:
        BlissCommand = False
    return BlissCommand

def main():
    while True:
        print("Listening for Hotword")
        filename = listen()
        if not is_connected():
            break
        outStr, indexMax = process(filename)
        BlissCommand = command_f1(indexMax)
        while BlissCommand:
            print("Start command")
            filename = listen()
            outStr, indexMax = process(filename)
            BlissCommand = command_f2(indexMax)
            time.sleep(2)
if __name__ == "__main__":
    main()
