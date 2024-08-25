from code import download_video, capture_slides, preview_images

def main(url):
  # Step 1: Download the video
  video_path = download_video(url)
  
  # Step 2: Capture slides from the video in the output_folder
  capture_slides(video_path, output_folder='slides', max_frame_count = 10000, ssim_threshold=0.9, histogram_threshold=0.7, time_gap=50, verbose=True)
  
  # Step 3: Preview the captured slides
  max_slides = 100
  preview_images('slides', image_count=max_slides)

  if __name__ == "__main__":
    main(url)
