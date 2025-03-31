import numpy as np
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import matplotlib.pyplot as plt
from collections import Counter

# Load the image - replace with your image path
image_path = r"Change_for_an_absolute_path_to_your_image_location"
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Could not load image from {image_path}")
else:
    # Detect objects in the image
    boxes, labels, _ = cv.detect_common_objects(image)
    
    # Draw bounding boxes on the image
    output = draw_bbox(image, boxes, labels, None)
    
    # Convert BGR (OpenCV format) to RGB for matplotlib
    output_rgb = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
    
    # Display the image with bounding boxes
    plt.figure(figsize=(10, 8))
    plt.imshow(output_rgb)
    plt.axis('off')
    plt.title('Detected Objects')
    plt.show()
    
    # Count occurrences of each object type
    if not labels:
        print("No objects detected in the image.")
    else:
        # Use Counter to count occurrences of each object type
        object_counts = Counter(labels)
        
        # Print results
        print("Detected objects:")
        for object_name, count in object_counts.items():
            print(f"- {object_name}: {count}")
        
        print(f"\nTotal objects detected: {len(labels)}")
        print(f"Unique object types: {len(object_counts)}")
