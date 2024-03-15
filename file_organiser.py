import os
import shutil

# Define the source and destination paths
source_path = os.path.expanduser('~/Downloads')
destination_path = os.path.expanduser('~/Documents/Pictures')

# Ensure the destination directory exists
os.makedirs(destination_path, exist_ok=True)

# Define common image file extensions
image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')

# Move the image files
for filename in os.listdir(source_path):
    if filename.endswith(image_extensions):
        source_file = os.path.join(source_path, filename)
        destination_file = os.path.join(destination_path, filename)
        shutil.move(source_file, destination_file)
        print(f'Moved: {filename}')
