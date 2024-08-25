from your_script_name import download_video, capture_slides, preview_images

def main(url):
  # Step 1: Download the video
  video_path = download_video(url)
  
  # Step 2: Capture slides from the video
  capture_slides(video_path, verbose=True)
  
  # Step 3: Preview the captured slides
  preview_images('slides', image_count=100)
