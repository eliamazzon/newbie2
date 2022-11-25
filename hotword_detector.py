#!/usr/bin/env python3
import pvporcupine
import struct
from recorder import record




def detector(keywords,a_key):
    try:
        #initiate porcupine 
        porcupine = pvporcupine.create(
        access_key = a_key,
        keyword_paths = keywords
        )

        while True: #endless detector loop
            pcm = record()
            #print(porcupine.frame_length)
            keyword_index = porcupine.process(pcm)

            if keyword_index >= 0:
                break
            
        return True
                
    except Exception as e:
        print(f"Module: hotword_detector.py/detector ERROR: {e}")
        
    finally:
        if porcupine is not None:
            porcupine.delete()
        
