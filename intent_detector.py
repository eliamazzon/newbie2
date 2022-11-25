#!/usr/bin/env python3

import pvrhino
from recorder import record


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
        
        #print(rhino.context_info)
        
        print("Listening...")
        print()
    
        
        while True:
                pcm = record()

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
                        print("Didn't understand the command.\n")    
                        break
                
        return inference
                
    except Exception as e:
        print(f"ERROR: {e}")
    
    
