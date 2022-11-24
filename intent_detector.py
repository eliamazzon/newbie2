#!/usr/bin/env python3

import pvrhino
import pyaudio
import struct
from pvrecorder import PvRecorder

ACCESS_KEY = 'Zu669csCgbvTaWn0PlJQMl7gh52UA7InfS3m61avjhmoXTCtrf/6wQ==' 
context_path = 'contexts/Newbie-Music_en_linux_v2_1_0.rhn'





def int_detector(context,a_key):
    try:
        
        rhino = None
        recorder = None
        wav_file = None
        
        #initiate rhino 
        rhino = pvrhino.create(
        access_key = a_key,
        context_path = context,
        endpoint_duration_sec = 0.7
        )        
        
        recorder = PvRecorder(device_index=-1, 
                              frame_length=rhino.frame_length)
        recorder.start()
        
        #print(rhino.context_info)
        
        
        print("Using device: %s" % recorder.selected_device)
        print("Listening...")
        print()
    
        
        while True:
                pcm = recorder.read()

                if wav_file is not None:
                    wav_file.writeframes(struct.pack("h" * len(pcm), *pcm))

                is_finalized = rhino.process(pcm)
                if is_finalized:
                    inference = rhino.get_inference()
                    if inference.is_understood:
                        print('{')
                        print("  intent : '%s'" % inference.intent)
                        print('  slots : {')
                        for slot, value in inference.slots.items():
                            print("    %s : '%s'" % (slot, value))
                        print('  }')
                        print('}\n')
                        
                        break
                    else:
                        #print("Didn't understand the command.\n")       
                
        return inference
                
    except Exception as e:
        print(f"ERROR: {e}")
    
    
