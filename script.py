import os
import whisper

print("--- Starting Transcript Job ---")
calls_dir = "./Calls"
transcripts_dir = "./Transcripts"
os.makedirs(transcripts_dir, exist_ok=True)

# Safety check for the folder structure
if not os.path.exists(calls_dir):
    print("Error: Local 'Calls' directory does not exist.")
    exit(0)

# Pull all matching audio files (handling both lowercase and uppercase extensions)
audio_files = [f for f in os.listdir(calls_dir) if f.lower().endswith((".mp3", ".wav", ".m4a", ".mp4"))]
print(f"Found {len(audio_files)} audio file(s) inside the local folder to process.")

if len(audio_files) == 0:
    print("Exiting: No audio files available to process.")
    exit(0)

print("Loading Whisper model into CPU...")
model = whisper.load_model("base")  

for filename in audio_files:
    file_path = os.path.join(calls_dir, filename)
    print(f"Processing: {filename}...")

    # Transcribe the audio file
    result = model.transcribe(file_path)

    # Correct string handling to create the transcript text file
    base_name, _ = os.path.splitext(filename)
    txt_filename = base_name + ".txt"
    txt_path = os.path.join(transcripts_dir, txt_filename)

    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(result["text"])
        
    print(f"Success: Created transcript file '{txt_filename}'")

print("--- Job Finished Successfully! ---")
