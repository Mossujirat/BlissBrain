from __future__ import division
from Training.features import mfcc
import scipy.io.wavfile as wav
import numpy as np

#words = ['apple', 'banana', 'kiwi', 'lime', 'orange']
#words = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10']
words = ['001', '002', '003', '004', '005', '006', '007', '008', '009']


for x in range(len(words)):
	fileString = words[x]+"_mfcc"
	data = []
	for i in range(10): # number of person
		for j in range(4): # number of uttrance
			(rate,sig) = wav.read("training_sets/"+ str(i+1) + "/"+ words[x] + str(j+1) + ".wav")
			print("Reading: " + words[x] + "-" + str(i+1) + "-" + str(j+1) + ".wav")
			duration = len(sig)/rate
			mfcc_feat = mfcc(sig,rate,winlen=duration/20,winstep=duration/20)
			s = mfcc_feat[:20]
			st = []
			for elem in s:
				st.extend(elem)
		
			st /= np.max(np.abs(st),axis=0)
			data.append(st)
			print (st)
		
	with open("mfccData/" + fileString+ ".npy", 'wb') as outfile:
   		np.save(outfile, data)




