```python
# speech_to_text_converter.py

"""
This script converts speech to text using the SpeechRecognition library.  It handles various audio sources and provides error handling for common issues.
"""

import speech_recognition as sr
import os

def speech_to_text(audio_source=None):
    """
    Converts speech to text.

    Args:
        audio_source (str, optional): Path to an audio file. If None, uses the default microphone. Defaults to None.

    Returns:
        str: The transcribed text, or None if an error occurred.
    """
    r = sr.Recognizer()

    try:
        if audio_source:
            if not os.path.exists(audio_source):
                raise FileNotFoundError(f"Audio file not found: {audio_source}")
            with sr.AudioFile(audio_source) as source:
                audio = r.record(source)
        else:
            with sr.Microphone() as source:
                print("Say something!")
                audio = r.listen(source)

        text = r.recognize_google(audio)  #Using Google Speech Recognition
        return text

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None
    except FileNotFoundError as e:
        print(e)
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


if __name__ == "__main__":
    audio_file = input("Enter the path to an audio file (leave blank to use microphone): ")
    
    transcribed_text = speech_to_text(audio_file)

    if transcribed_text:
        print("Transcribed Text:")
        print(transcribed_text)
```

To use this code:

1. **Install SpeechRecognition:**  `pip install SpeechRecognition`
2. **Run the script:** `python speech_to_text_converter.py`
3. **Enter audio file path (optional):** If you have an audio file (.wav, .flac, etc.), provide its path. Otherwise, press Enter to use your microphone.

The script will then transcribe the audio and print the resulting text.  Error handling is included to catch common issues like network problems, audio file not found, and speech recognition failures.  Remember that the accuracy depends on the quality of the audio and the clarity of speech.
