# Vid2Slides

## Video Slide Capture

This project provides a Python script to capture slides from a YouTube video by detecting significant frame changes. It is useful for extracting keyframes from videos, particularly when they consist of slide-based presentations.

## Features
- Downloads video from YouTube.
- Captures significant frames based on Structural Similarity Index (SSIM) and histogram differences.
- Previews captured slides.

## Requirements
Install the dependencies using:
```bash
pip install -r requirements.txt
```

## Usage
1. Download a YouTube Video:
```
download_video('https://www.youtube.com/watch?v=VIDEO_ID')
```

2. Capture Slides:
```
capture_slides('video.mp4')
```

3. Preview Captured Slides:
```
preview_images('slides')
```

## How to run
```
python main.py '<youtube_video_url>' --verbose
```
Sometimes Youtube might flag it as a 'bot' when run using a python ide. I have also included a .ipynb file in examples/sample_1.ipynb which can be executed in Google Colab and runs without any error.
