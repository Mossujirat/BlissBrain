import numpy as np
import scipy.io.wavfile as wav
from Training.features import mfcc
from Network import TestingNetwork
import time

def testInit():
    #Setup Neural Network
    f1 = open("Training/network/network_words.npy", "rb")
    weights  = np.load(f1)
    testNet = TestingNetwork((260, 50, 50, 9), weights)
    return testNet

def extractFeature(soundfile):
	# Get MFCC Feature Array
	(rate,sig) = wav.read(soundfile)
	duration = len(sig)/rate;
	mfcc_feat = mfcc(sig,rate,winlen=duration/20,winstep=duration/20)
	print ("MFCC Feature Length: " + str(len(mfcc_feat)))
	s = mfcc_feat[:20]
	st = []
	for elem in s:
		st.extend(elem)
	st /= np.max(np.abs(st),axis=0)
	inputArray = np.array([st])
	return inputArray

def feedToNetwork(inputArray,testNet):
	#Input MFCC Array to Network
    outputArray = testNet.forwardProc(inputArray)

	#if the maximum value in the output is less than
	#the threshold the system does not recognize the sound
	#the user spoke
    indexMax = outputArray.argmax(axis = 1)[0]
    print (outputArray)

	#Mapping each index to their corresponding meaning
    outStr = None

    if indexMax == 0:
        outStr  = "1"
    elif indexMax == 1:
        outStr  = "2"
    elif indexMax == 2:
        outStr  = "3"
    elif indexMax == 3:
        outStr  = "4"
    elif indexMax == 4:
        outStr  = "5"
    elif indexMax == 5:
        outStr  = "6"
    elif indexMax == 6:
        outStr  = "7"
    elif indexMax == 7:
        outStr  = "8"
    elif indexMax == 8:
        outStr  = "9"
    print ("Detected: Sound" + outStr)
    return outStr, indexMax

if __name__ == "__main__":
	start = time.time()
	testNet = testInit()
	inputArray = extractFeature("test_files/TSound2_2.wav")
	feedToNetwork(inputArray,testNet)
	end = time.time()
	print("time = ",end-start)
