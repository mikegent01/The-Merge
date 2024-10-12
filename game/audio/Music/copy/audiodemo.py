from pydub import AudioSegment
import random

# Load the audio files
audio_files = ['1.mp3', '2.mp3', '3.wav', '4.mp3', '5.mp3', '6.wav']
audio_segments = [AudioSegment.from_file(file) for file in audio_files]

# Set the duration of the final audio file
final_duration = 60 * 1000  # 1 minute in milliseconds

# Create an empty audio segment
final_audio = AudioSegment.silent(duration=final_duration)

# Randomly select a segment from one audio file and add it to the final audio
selected_file = random.choice(audio_segments)
start_time = random.randint(0, len(selected_file) - 1)
end_time = min(start_time + final_duration, len(selected_file))
final_audio = selected_file[start_time:end_time]

# Export the final audio file
final_audio.export('final_audio.mp3', format='mp3')
