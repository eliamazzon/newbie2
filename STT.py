import pvcheetah
import pyaudio
import struct

cheetah = pvcheetah.create(access_key='Zu669csCgbvTaWn0PlJQMl7gh52UA7InfS3m61avjhmoXTCtrf/6wQ==')


pa = pyaudio.PyAudio() #initiate pyaudio to record audio
audio_stream = pa.open( #define and format audio_stream
                            rate=cheetah.sample_rate,
                            channels=1,
                            format=pyaudio.paInt16,
                            input=True,
                            frames_per_buffer=cheetah.frame_length)
    
while True:
    print("looping")
    pcm = audio_stream.read(cheetah.frame_length)
    pcm = struct.unpack_from("h" * cheetah.frame_length, pcm)
    partial_transcript, is_endpoint = cheetah.process(pcm)
    if is_endpoint:
        final_transcript = cheetah.flush()
        
cheetah.delete();
    
