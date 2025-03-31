# Object Detection Using OpenCV and CVLib

## Overview
This script performs object detection on an input image using the **CVLib** library and OpenCV. It identifies common objects in the image, draws bounding boxes around them, and provides a count of detected object types.

## Features
- Loads an image and detects objects using `cvlib`.
- Draws bounding boxes around detected objects.
- Displays the processed image using `matplotlib`.
- Prints a summary of detected objects with their counts.

## Requirements
Ensure you have the following dependencies installed before running the script:

```bash
pip install numpy opencv-python cvlib matplotlib
```

## Usage
1. **Modify the image path** in the script:
   ```python
   image_path = r"Change_for_an_absolute_path_to_your_image_location"
   ```
   Replace it with the absolute path to your image.

2. **Run the script**:
   ```bash
   python object_detection.py
   ```

## Output
- A processed image with bounding boxes around detected objects.
- A printed summary of detected objects, their count, and unique types.
- Example output:
  ```
  Detected objects:
  - person: 2
  - car: 1
  
  Total objects detected: 3
  Unique object types: 2
  ```

## Notes
- If no objects are detected, the script will print `No objects detected in the image.`
- Ensure the image path is correct to avoid loading errors.

## License
This project is open-source and free to use for educational and research purposes.

