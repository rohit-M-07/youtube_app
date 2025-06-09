from crewai.tools import BaseTool
<<<<<<< HEAD
import subprocess
import os
import glob

from openai import OpenAI


import glob
import wave
import contextlib
import soundfile as sf
import numpy as np
from scipy.io import wavfile

from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()

client = OpenAI()



class YouTubeCaptionAudioTool(BaseTool):
    name: str = "YouTube_Caption_Downloader"
    description: str = (
        "Downloads English captions from the given YouTube URL "
    )
    state: any = Field(default=None)
    audio_filename: str = Field(default=None)
    transcript_filename: str= Field(default=None)
    chat_id: any= Field(default=None)

    def __init__(self,state):
        super().__init__(state=state,chat_id=id)
        self.state=state
        self.chat_id=id
        self.audio_filename= self.state.get(self.chat_id,"downloaded_audio_path")
        self.transcript_filename=str(Path(self.state.get(self.chat_id,"Blog_output")).parent/"transcript.txt")
        self.state.set(self.chat_id,"transcript_path",self.transcript_filename)

    def get_wav_duration(self,file_path):
=======
from pydantic import Field
from pathlib import Path
from dotenv import load_dotenv
import subprocess
import os
import glob
import wave
import contextlib
import soundfile as sf
from scipy.io import wavfile
from openai import OpenAI

load_dotenv()
client = OpenAI()

class YouTubeCaptionAudioTool(BaseTool):
    name: str = "YouTube_Caption_Downloader"
    description: str = "Downloads and transcribes audio from a YouTube URL."

    state: any = Field(default=None)
    audio_filename: str = Field(default=None)
    transcript_filename: str = Field(default=None)
    chat_id: any = Field(default=None)

    def __init__(self, state, id):
        super().__init__(state=state, chat_id=id)
        self.state = state
        self.chat_id = id
        self.audio_filename = self.state.get(self.chat_id, "downloaded_audio_path")
        self.transcript_filename = str(Path(self.state.get(self.chat_id, "main_path")).parent / 'outputs' / f"{self.chat_id}"/"transcript.txt")
        self.state.set(self.chat_id, "transcript_path", self.transcript_filename)

    def get_wav_duration(self, file_path):
>>>>>>> 4d23f7e (working-code)
        with contextlib.closing(wave.open(file_path, 'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            return frames / float(rate)

<<<<<<< HEAD
    def chunk_audio(self,audio_path, chunk_length_sec=60):
=======
    def chunk_audio(self, audio_path, chunk_length_sec=60):
>>>>>>> 4d23f7e (working-code)
        sample_rate, data = wavfile.read(audio_path)
        total_samples = data.shape[0]
        chunk_size = sample_rate * chunk_length_sec

        chunks = []
        for start in range(0, total_samples, chunk_size):
            end = min(start + chunk_size, total_samples)
            chunk_data = data[start:end]
<<<<<<< HEAD
            chunk_path = str( Path(self.audio_filename)/ "chunk_" / f"{len(chunks)}.wav" )
            sf.write(chunk_path, chunk_data, sample_rate)
=======
            chunk_path = str(Path(self.audio_filename) / f"chunk_{len(chunks)}.wav")
            sf.write(chunk_path, chunk_data, sample_rate)
            print(f"Saved chunk: {chunk_path}, samples: {len(chunk_data)}")
>>>>>>> 4d23f7e (working-code)
            chunks.append(chunk_path)
        return chunks

    def _run(self, url: str) -> str:
<<<<<<< HEAD
        
        try:
            os.makedirs(self.audio_filename, exist_ok=True)

            # Output filename template with .wav extension
            output_template = os.path.join(self.audio_filename, "%(title).200s.%(ext)s")

            # Run yt-dlp to download and convert audio to WAV
            subprocess.run([
                "yt-dlp",
                "-x",  # extract audio
                "--audio-format", "wav",  # convert to .wav
                "-o", output_template,  # output path template
                url
            ], check=True)


        except subprocess.CalledProcessError as e:
            return f"Failed to download captions or audio: {e}"


        print("Generating Transcription")

    #Get the first .wav file in the directory
        audio_path = str(glob.glob(os.path.join(self.audio_filename, "*.wav"))[0])

        # Chunk the audio file into 60s segments
        chunks = self.chunk_audio(audio_path, chunk_length_sec=60)

        # Transcribe each chunk
        full_transcription = ""
        for i, chunk_path in enumerate(chunks):
            print(f"Transcribing chunk {i+1}/{len(chunks)}")
            with open(chunk_path, "rb") as audio_file:
                transcription = client.audio.transcriptions.create(
                    model="whisper-1", 
                    file=audio_file
                )
                full_transcription += transcription.text + " "

        
        with open(self.transcript_filename,'w',encoding='utf-8') as f:
            f.write(full_transcription)

        print(f"Transcription: {full_transcription}")

        return full_transcription
=======
        try:
            os.makedirs(self.audio_filename, exist_ok=True)

            # Skip if .wav file already exists
            existing_wav = glob.glob(os.path.join(self.audio_filename, "*.wav"))
            if existing_wav:
                print("Audio already downloaded. Skipping download.")
                audio_path = existing_wav[0]
            else:
                print("Downloading audio...")
                output_template = os.path.join(self.audio_filename, "%(title).200s.%(ext)s")
                subprocess.run([
                    "yt-dlp",
                    "-x", "--audio-format", "wav",
                    "-o", output_template,
                    url
                ], check=True)
                audio_path = glob.glob(os.path.join(self.audio_filename, "*.wav"))[0]

            print("Audio downloaded. Starting chunking...")
            chunks = self.chunk_audio(audio_path, chunk_length_sec=60)
            print(f"{len(chunks)} chunks created.")

            full_transcription = ""
            for i, chunk_path in enumerate(chunks):
                print(f"Transcribing chunk {i+1}/{len(chunks)}: {chunk_path}")
                try:
                    with open(chunk_path, "rb") as audio_file:
                        transcription = client.audio.transcriptions.create(
                            model="whisper-1",
                            file=audio_file
                        )
                        full_transcription += transcription.text + " "
                except Exception as e:
                    print(f"Error transcribing chunk {i+1}: {e}")

            with open(self.transcript_filename, 'w', encoding='utf-8') as f:
                f.write(full_transcription)

            print("Transcription complete.")
            print(full_transcription)
            return full_transcription

        except subprocess.CalledProcessError as e:
            return f"Audio download failed: {e}"
        except Exception as e:
            return f"Tool failed: {e}"
>>>>>>> 4d23f7e (working-code)
