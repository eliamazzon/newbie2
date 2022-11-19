#!/usr/bin/env python3

from hotword_detector import detector 

#CONFIGURATION PARAMETERS
ACCESS_KEY = 'Zu669csCgbvTaWn0PlJQMl7gh52UA7InfS3m61avjhmoXTCtrf/6wQ==' 
KEYWORDS_PATHS = ['keywords/hey_newbie_linux_v2_1_0.ppn',
          'keywords/Okay-Newbie_en_linux_v2_1_0.ppn']

if detector(KEYWORDS_PATHS, ACCESS_KEY) == True:
    print("Online and Ready")
