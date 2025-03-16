import os
from TTS.api import TTS

# Define the current working directory
current_dir = os.getcwd()

# Path to the sample speaker WAV file
speaker_wav = os.path.join(current_dir, "speaker", "my_voice.wav")

# Check if the speaker WAV file exists
if not os.path.exists(speaker_wav):
    raise FileNotFoundError(f"Speaker file not found: {speaker_wav}. Please place the file in the correct directory.")

# Read text from an input file
text_file = os.path.join(current_dir, "input.txt")
if not os.path.exists(text_file):
    raise FileNotFoundError(f"Text file not found: {text_file}. Please create an 'input.txt' file in the current directory.")

with open(text_file, "r", encoding="utf-8") as file:
    text = file.read().strip()

# Define output WAV file path
output_wav = os.path.join(current_dir, "output.wav")

# Load XTTS v2 model from Hugging Face
tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=True).to("cuda")

# Generate speech from the input text using the speaker's voice
tts.tts_to_file(text=text, speaker_wav=speaker_wav, language="en", file_path=output_wav)

print(f"Audio file has been saved at: {output_wav}")
