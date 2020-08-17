import cv2
import sys
from sklearn.externals import joblib

model = joblib.load('mnist.model')

img = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img , (28, 28))
x = img/255.0
x = x.reshape(-1)
print(model.predict([x]))