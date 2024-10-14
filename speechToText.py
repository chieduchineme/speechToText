import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.AudioFile('your_audio_file.wav') as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said: " + text)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None

# Example of using a recorded file instead of real-time microphone input
profile_text = speech_to_text()
