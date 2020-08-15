import pyaudio
import wave
#CHUNK = 9216 1024
CHUNK = 16384
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 48000#44100
#time = 30
#WAVE_OUTPUT_FILENAME = "newMZH.wav"

p = pyaudio.PyAudio()


#print(p.get_device_info_by_index(0)['defaultSampleRate'])
class recorder:
    def recording(filename,time):
        stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)      
        print("* recording")
        frames = []
        for i in range(0, int(RATE / CHUNK * time)):
            data = stream.read(CHUNK)#,exception_on_overflow = False
            frames.append(data)
        
        print("* done recording")
        stream.stop_stream()
        stream.close()
#        p.terminate()
        
        wf = wave.open(filename+".wav", 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
