from picovoice import Picovoice

a_key = 'Zu669csCgbvTaWn0PlJQMl7gh52UA7InfS3m61avjhmoXTCtrf/6wQ=='
keyword_path = 'keywords/hey_newbie_linux_v2_1_0.ppn'
context_path = 'contexts/Newbie-Music_en_linux_v2_1_0.rhn'

def wake_word_callback():
    print("wake word detected")
    
def inference_callback(inference):
    print(inference.is_understood)
    if inference.is_understood:
        print(inference.intent)
        for k, v in inference.slots.items():
            print(f"{k} : {v}")

pv = Picovoice(
    access_key=a_key,
    keyword_path=keyword_path,
    wake_word_callback=wake_word_callback,
    context_path=context_path,
    inference_callback=inference_callback)

from pvrecorder import PvRecorder
# `-1` is the default input audio device.
recorder = PvRecorder(device_index=-1)
recorder.start()

pcm = recorder.read()
pv.process(pcm)

rhino_demo_mic --access_key 'Zu669csCgbvTaWn0PlJQMl7gh52UA7InfS3m61avjhmoXTCtrf/6wQ==' --context_path 'contexts/Newbie-Music_en_linux_v2_1_0.rhn'
