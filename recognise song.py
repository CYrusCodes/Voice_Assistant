from ast import main
#import ShazamAPI
from ShazamAPI import Shazam
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
def record():
    freq = 44100

    # Recording duration
    duration = 10

    # Start recorder with the given values
    # of duration and sample frequency
    recording = sd.rec(int(duration * freq),
                    samplerate=freq, channels=2)
    print("working on it................")

    # Record audio for the given number of seconds
    sd.wait()
    # This will convert the NumPy array to an audio
    # file with the given sampling frequency
    write("recording0.wav", freq, recording)
    #print("found....\n")

    
def recog():
    mp3_file_content_to_recognize = open(r'C:\Users\Subham Dey\recording0.wav', 'rb').read()
    shazam = Shazam(mp3_file_content_to_recognize)
    recognize_generator = shazam.recognizeSong()
    #recognize_generator = shazam.recognizeSong()
    try:
        name=next(recognize_generator)[1]['track']['share']['subject']
        #if(len(name)!=0):
        print(name) # current offset & shazam response to recognize requests
    except:
        print("could not find")

record()
recog()