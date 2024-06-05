import os
import wave
import audioop
import sounddevice as sd
import wavio
from google.cloud import speech_v1p1beta1 as speech

# Set Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\kshit\\OneDrive\\Documents\\google credentials\\mimetic-algebra-424706-t3-eebee26cbd3c.json"

def record_audio(filename, duration, fs):
    print("Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    wavio.write(filename, recording, fs, sampwidth=2)
    print("Recording finished.")

def convert_to_mono(input_path, output_path):
    with wave.open(input_path, 'rb') as infile:
        params = list(infile.getparams())
        params[0] = 1  # nchannels set to 1
        with wave.open(output_path, 'wb') as outfile:
            outfile.setparams(tuple(params))
            frames = infile.readframes(infile.getnframes())
            mono_frames = audioop.tomono(frames, infile.getsampwidth(), 1, 1)
            outfile.writeframes(mono_frames)

def transcribe_audio(audio_path):
    try:
        client = speech.SpeechClient()

        with open(audio_path, "rb") as audio_file:
            content = audio_file.read()

        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=48000,
            language_code="en-US",
        )

        response = client.recognize(config=config, audio=audio)

        if not response.results:
            print("No transcription results returned.")
            return None

        for result in response.results:
            print("Transcript: {}".format(result.alternatives[0].transcript))
            return result.alternatives[0].transcript

    except Exception as e:
        print(f"Error during transcription: {e}")
        return None

