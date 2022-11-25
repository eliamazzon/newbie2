import os
import time

def interpreter(command):
    if command.intent == "PlaySong":
        os.popen("playerctl play")
        os.popen("/usr/lib/brave-browser/brave --profile-directory=Default --app-id=pjibgclleladliembfgfagdaldikeohf")
        
    
