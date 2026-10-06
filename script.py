import os
import whisper

print("Loading Whisper model into CPU...")
model = whisper.load_model("base")  # 'base' or 'small' prevents CPU timeout crashes

calls_dir = "./Calls"
transcripts_dir = "./Transcripts"
os.makedirs(transcripts_dir, exist_ok=True)

if not os.path.exists(calls_dir) or not os.listdir(calls_dir):
    print("No audio files found to process.")
    exit(0)

for filename in os.listdir(calls_dir):
    if filename.endswith((".mp3", ".wav", ".m4a", ".mp4")):
        file_path = os.path.join(calls_dir, filename)
        print(f"Transcribing {filename}...")

        # Transcribe audio
        result = model.transcribe(file_path)

        # Save text file
        txt_filename = os.path.splitext(filename)[0] + ".txt"
        txt_path = os.path.join(transcripts_dir, txt_filename)

        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(result["text"])
            
        print(f"Success: Created transcript for {filename}")

print("Batch processing complete!")
