from pvrecorder import PvRecorder

recorder = PvRecorder(device_index=-1, frame_length=512)
recorder.start()

def record():
    try:
        audio = recorder.read()
        return audio
    except Exception as e:
        print(f"Module: recorder.py/record ERROR: {e}")
