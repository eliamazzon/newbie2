#!/usr/bin/env python3
import pvporcupine
import pyaudio
import struct

porcupine = None
pa = None
audio_stream = None

try:
    porcupine = pvporcupine.create(
    access_key='Zu669csCgbvTaWn0PlJQMl7gh52UA7InfS3m61avjhmoXTCtrf/6wQ==',
    keyword_paths=['keywords/hey_newbie_linux_v2_1_0.ppn',
                   'keywords/Okay-Newbie_en_linux_v2_1_0.ppn']
    )


    pa = pyaudio.PyAudio()

    audio_stream = pa.open(
                        rate=porcupine.sample_rate,
                        channels=1,
                        format=pyaudio.paInt16,
                        input=True,
                        frames_per_buffer=porcupine.frame_length)

    while True:
        pcm = audio_stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        keyword_index = porcupine.process(pcm)

        if keyword_index >= 0:
            print("Hotword Detected")
            
except Exception as e:
    print(f"ERROR: {e}")
    
finally:
    if porcupine is not None:
        porcupine.delete()

    if audio_stream is not None:
        audio_stream.close()

    if pa is not None:
            pa.terminate()
