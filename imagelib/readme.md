# Basic image processing 

1. OpenCV 
2. Scikit-image
3. PIL (Python Imaging Library)

Basic task such as downloading image from url, opening image file from local machine, reading image file from binary stream, resizing and saving can be done using above libraries apart from their special use cases.

## OpenCV

```python
import cv2

# download
r = request.get(url)
c = r.content # get content in binary format


# cv2 decodes array sequence in bgr format
image = cv2.imdecode(np.asarray(bytearray(c), dtype="uint8"))
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

cv2.imshow("window title", image)

cv2.resize(image, (hx, hy))

cv2.imwrite('filename.ext', image)

```

## Scikit-Image Library

```python
from skimage.transform import resize # various image transformation defs
from skimage.io import imread, imsave # i/o operation defs on image

# Read image as ndarray
image = imread(url)

# Write image to file 
imsave(image)

# Resize image
resize(image, (hx, hy))

```
