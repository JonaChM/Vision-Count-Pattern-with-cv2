
from pickle import APPEND
import numpy as np
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import matplotlib.pyplot as plt
from numpy.lib.polynomial import poly

image = cv2.imread(r"Change_for_an_absolute_path_to_your_image_location")
box, label, count = cv.detect_common_objects(image)
output = draw_bbox(image, box, label, count)
plt.imshow(output)
plt.show()

Element = str(set(label)).replace('{','').replace('}','').replace('\'','')
if Element == "set()":
    Element = "none"

Count_Of_Elements = label.count(Element)

print("The commonly recognized objects is/are " + Element + " and the count is " + str(Count_Of_Elements) )