#!/usr/bin/env python3

from hotword_detector import detector 
from intent_detector import int_detector
from intent_interpreter import interpreter

#CONFIGURATION PARAMETERS
ACCESS_KEY = 'Zu669csCgbvTaWn0PlJQMl7gh52UA7InfS3m61avjhmoXTCtrf/6wQ==' 
KEYWORDS_PATHS = ['keywords/hey_newbie_linux_v2_1_0.ppn',
          'keywords/Okay-Newbie_en_linux_v2_1_0.ppn']

context_path = 'contexts/Newbie-Music_en_linux_v2_1_0.rhn'

    
while True:
    if detector(KEYWORDS_PATHS, ACCESS_KEY) == True:
        print("How can I help u sir?")
        command = int_detector(context_path,ACCESS_KEY)
        print(command.intent)
        interpreter(command)
        
        
        
    
