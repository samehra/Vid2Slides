from Code import download_video, capture_slides, preview_images

def main(args):
  # Step 1: Download the video
  video_path = download_video(args.video_url)
  
  # Step 2: Capture slides from the video in the output_folder
  capture_slides(video_path, args.output_folder, args.max_frame_count, args.ssim_threshold, args.histogram_threshold, args.time_gap, args.verbose)
  
  # Step 3: Preview the captured slides
  preview_images(args.output_folder, image_count=args.preview_count)

  if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Capture slides from a YouTube video.")
    
    # Add the video URL argument
    parser.add_argument('video_url', type=str, help="URL of the YouTube video")
    
    # Optional arguments with default values
    parser.add_argument('--ssim_threshold', type=float, default=0.9, help="SSIM threshold for slide detection")
    parser.add_argument('--histogram_threshold', type=float, default=0.7, help="Histogram threshold for slide detection")
    parser.add_argument('--time_gap', type=int, default=50, help="Time gap between frames to compare")
    parser.add_argument('--max_frame_count', type=int, default=10000, help="Maximum number of slides to capture")
    parser.add_argument('--output_folder', type=str, default='slides', help="Folder to save captured slides")
    parser.add_argument('--verbose', type=bool, default='False', help="Print the count of slides and % of frames parsed")
    parser.add_argument('--preview_count', type=int, default=100, help="Number of slides to preview")

    args = parser.parse_args()

    # Call the main function with parsed arguments
    main(args)
