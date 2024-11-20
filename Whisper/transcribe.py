import whisper

# Load the Whisper model (base model is a good starting point for accuracy and speed)
model = whisper.load_model("base")

# Transcribe the audio
result = model.transcribe(r"C:\Users\quokka\Documents\Engineering Fun\Python100\Whisper\explanation.m4a")

# Print the transcription
print(result["text"])

with open("transcription.txt", "w") as file:
    file.write(result["text"])