#!/usr/bin/env python3
import pvporcupine
import pyaudio
import struct





def detector(keywords,a_key):
    try:
        #initiate porcupine 
        porcupine = pvporcupine.create(
        access_key = a_key,
        keyword_paths = keywords
        )
        pa = pyaudio.PyAudio() #initiate pyaudio to record audio

        audio_stream = pa.open( #define and format audio_stream
                            rate=porcupine.sample_rate,
                            channels=1,
                            format=pyaudio.paInt16,
                            input=True,
                            frames_per_buffer=porcupine.frame_length)
        print(porcupine.sample_rate)


        while True: #endless detector loop
            pcm = audio_stream.read(porcupine.frame_length)
            #print(porcupine.frame_length)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            keyword_index = porcupine.process(pcm)

            if keyword_index >= 0:
                break
            
        return True
                
    except Exception as e:
        print(f"ERROR: {e}")
        
    finally:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if pa is not None:
                pa.terminate()
