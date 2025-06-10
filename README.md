# ReelGenAI

ReelGenAI is an AI-powered Flask application that allows users to upload images and provide a text description. The app generates personalized video reels by converting the description to audio using ElevenLabs TTS and stitching the images and audio together using ffmpeg.

## Features

- Upload multiple images to create a video reel.
- Enter a text description to be converted to voiceover using ElevenLabs TTS.
- Automatic video generation with ffmpeg.
- Gallery to view generated reels.

## Setup Instructions

1. **Clone the repository**

2. **Install dependencies**
   ```sh
   pip install flask werkzeug elevenlabs

3. **Set your ElevenLabs API key**

   Edit config.py and set your API key.

4. **Run the Flask App**
   python main.py

5. **Start the Background Process for reel Generation**
   python generate_process.py

6. **Open your browser**
    Visit http://localhost:5000

   ## Usage
1. Go to /create to upload images and enter a description.
   
2. Generated reels will appear in the /gallery
