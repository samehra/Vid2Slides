import cv2
import numpy as np
from pytubefix import YouTube
import os
from skimage.metrics import structural_similarity as compare_ssim
import shutil
import matplotlib.pyplot as plt
from PIL import Image

# Step 1: Download the video from YouTube
def download_video(youtube_url, output_path='video.mp4'):
    yt = YouTube(youtube_url)
    ys = yt.streams.get_highest_resolution()
    ys.download(filename=output_path)
    print(f"Downloaded video: {output_path}")
    return output_path

# Step 2: Capture slides based on frame differences with a time gap
def capture_slides(video_path, output_folder='slides', max_frame_count = 10000, ssim_threshold=0.9, histogram_threshold=0.7, time_gap=50, verbose=False):
    if os.path.exists(output_folder):
      shutil.rmtree(output_folder) # delete the existing folder if it exists
    os.makedirs(output_folder)

    # if not os.path.exists(output_folder):
    #     os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)

    # Get total number of frames
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    prev_frame = None
    slide_count = 0
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        frame_count += 1

        if not ret:
            break

        # Introduce time gap by skipping frames
        if frame_count % time_gap != 0:
            continue

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

        if prev_frame is None:
            prev_frame = gray_frame
            continue

        # Calculate SSIM between current and previous frames
        ssim_score, _ = compare_ssim(prev_frame, gray_frame, full=True)

        # Calculate histogram difference
        prev_hist = cv2.calcHist([prev_frame], [0], None, [256], [0, 256])
        curr_hist = cv2.calcHist([gray_frame], [0], None, [256], [0, 256])
        hist_diff = cv2.compareHist(prev_hist, curr_hist, cv2.HISTCMP_CORREL)

        # If significant difference in both SSIM and histogram, save the frame
        if ssim_score < ssim_threshold or hist_diff < histogram_threshold:
            slide_count += 1
            slide_filename = os.path.join(output_folder, f"slide_{str(slide_count).zfill(4)}.jpg")
            cv2.imwrite(slide_filename, frame)

            # Calculate and display progress
            if verbose:
              progress_percentage = (frame_count / total_frames) * 100
              print(f"Slides Captured: {slide_count} | Progress: {progress_percentage:.1f}%")

        
        prev_frame = gray_frame
    
        if slide_count >= max_frame_count:
          break

    cap.release()
    cv2.destroyAllWindows()


def preview_images(image_folder, image_count=100, columns=5):
    # Get a list of image files in the folder
    image_files = [os.path.join(image_folder, f) for f in sorted(os.listdir(image_folder)) if f.endswith('.jpg')]

    # Limit to the first `image_count` images
    image_files = image_files[:image_count]

    # Calculate the number of rows
    rows = (len(image_files)+columns-1) // columns

    figsize = (20, 2.5*rows)
    # Create a figure to hold the grid of images
    fig, axes = plt.subplots(rows, columns, figsize=figsize)

    # Flatten axes array for easy iteration
    axes = axes.flatten()

    for i, img_path in enumerate(image_files):
        # Open and display each image
        img = Image.open(img_path)
        axes[i].imshow(img)
        axes[i].axis('off')  # Hide the axes

    # Hide any remaining empty subplots
    for j in range(i + 1, len(axes)):
        axes[j].axis('off')

    # Show the grid of images
    plt.tight_layout()
    plt.show()
