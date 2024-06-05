from flask import Flask, render_template, request, redirect, url_for
from questions import ask_question
from voice_to_text import record_audio, convert_to_mono, transcribe_audio
from sentiment import analyze_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    prompt = "Ask a question about generative AI."
    question = ask_question(prompt)
    return render_template('chat.html', question=question)

@app.route('/record', methods=['POST'])
def record():
    fs = 48000  # Sample rate
    duration = 10  # Duration of recording in seconds
    recorded_audio_path = "static/recording.wav"
    mono_audio_path = "static/recording_mono.wav"

    # Record audio from microphone
    record_audio(recorded_audio_path, duration, fs)

    # Convert the recorded stereo audio to mono
    convert_to_mono(recorded_audio_path, mono_audio_path)

    # Transcribe the mono audio
    transcription = transcribe_audio(mono_audio_path)
    analysis = analyze_response(transcription)
    
    return render_template('chat.html', question=None, transcription=transcription, analysis=analysis)

if __name__ == '__main__':
    app.run(debug=True)
