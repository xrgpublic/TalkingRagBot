from pathlib import Path
from openai import OpenAI
client = OpenAI(api_key='sk-proj-93EKV7Mr9m38etwQF1r3T3BlbkFJJKXULVM6vfdBacO64MVE')

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="Today is a wonderful day to build something people love!"
)

response.stream_to_file(speech_file_path)