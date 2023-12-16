import speech_recognition as sr
import pyttsx3
import webbrowser

def recognize_speech(recognizer, microphone):
    with microphone as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def open_browser():
    webbrowser.open("https://www.google.com")

def open_youtube():
    webbrowser.open("https://www.youtube.com")

def open_google_meet():
    webbrowser.open("https://meet.google.com")

def process_command(command):
    if "hello" in command.lower():
        return "Hello! How can I assist you today?"
    elif "open browser" in command.lower():
        open_browser()
        return "Opening the web browser."
    elif "open youtube" in command.lower():
        open_youtube()
        return "Opening YouTube."
    elif "open google meet" in command.lower():
        open_google_meet()
        return "Opening Google Meet."
    elif "what is your name" in command.lower():
        return "I am your personal assistant. You can call me Jarvis."
    elif "stop listening" in command.lower():
        return "Goodbye!"
    else:
        return "I'm not sure how to respond to that."

if __name__ == "__main__":
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    speak_text("Hello! I am your personal assistant. How can I help you today?")

    while True:
        user_input = recognize_speech(recognizer, microphone)
        if user_input:
            response = process_command(user_input)
            speak_text(response)

            # Check if the user wants to stop listening
            if "stop listening" in user_input.lower():
                break
