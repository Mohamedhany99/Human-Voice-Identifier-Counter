import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import time
#constants
CHUNK=1024*4
FORMAT = pyaudio.paInt16
CHANNELS=1
RATE=44100
#the second figure for the spectrum
fig, (ax,ax2) = plt.subplots(2,figsize=(15,8))

#class of pyaudio library
p = pyaudio.PyAudio()

#get data from microphone
stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
    )
#graph object

#fig, ax=plt.subplots() # the first figure
#the tone analyser line drawing
x= np.arange(0,2*CHUNK,2)
line, = ax.plot(x,np.random.rand(CHUNK),'-',lw=2)
#the x-axis for the spectrum and line
x_fft= np.linspace(0,RATE,CHUNK)
line_fft, = ax2.semilogx(x_fft,np.random.rand(CHUNK),'-',lw=2)

#formatting the axis`s the tone analyser
ax.set_title('Audio Waveform')
ax.set_xlabel('samples')
ax.set_ylabel('volume')
ax.set_ylim(0,255)
ax.set_xlim(0,CHUNK)
plt.setp(ax , xticks=[0, CHUNK, 2 * CHUNK], yticks=[0, 128, 255])
#formatting the figure of the spectrum analyser
ax2.set_xlim(20, RATE/2)
#measuring frame rate
frame_count=0
start_time=time.time()
while True:
    data=stream.read(CHUNK)
    data_int = np.array(struct.unpack(str(2*CHUNK) + 'B', data),dtype='b')[::2]+ 128
    data_np = np.array(data_int,dtype='b')[::2]+127
    line.set_ydata(data_np)
    y_fft=fft(data_int)
    line_fft.set_ydata(np.abs(y_fft[0:CHUNK])/(128*CHUNK))
    print("frame count = ",frame_count)
    ax2.clear()
    ax2.plot(data_np)
    ax.clear()
    ax.plot(data_int)#np.random.randn(100) for picking random values for the freq
    plt.pause(0.001)
    frame_count+=1
class spectrum:
    def drawingspectrum():
        while True: 
            data=stream.read(CHUNK)
            data_int = np.array(str(2*CHUNK) + 'B', data)
            data_np = np.array(data_int,dtype='b')[::2]+128
            line.set_ydata(data_np)
            y_fft=fft(data_int)
            line_fft.set_ydata(np.abs(y_fft[0:CHUNK])*2/(256*CHUNK))
            ax2.clear()
            a.plot(data_int)#np.random.randn(100) for picking random values for the freq
            plt.pause(0.001)
