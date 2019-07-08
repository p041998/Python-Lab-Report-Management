#import all important packages
import imutils
import cv2
import numpy as np
import argparse
from skimage.filters import threshold_local


def order_points(pts):
    rect=np.zeros((4,2),dtype="float32")
    s=pts.sum(axis=1)
    rect[0]=pts[np.argmin(s)]
    rect[2]=pts[np.argmax(s)]
    diff=np.diff(pts,axis=1)
    rect[1]=pts[np.argmin(diff)]
    rect[3]=pts[np.argmax(diff)]
    return rect

def four_point_transform(image,pts):
    rect=order_points(pts)
    (tl,tr,br,bl)=rect
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))
    dst = np.array(
        [[0, 0],
        [maxWidth - 1, 0],
         [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype = "float32")
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    return warped
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",help = "Path to the image to be scanned")
args = vars(ap.parse_args())
image = cv2.imread(r"C:\Users\admin\Desktop\python\report1.jpg")
ratio = image.shape[0] / 500.0
orig = image.copy()
image = imutils.resize(image, height = 500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(gray, 75, 200)
print("STEP 1: Edge Detection")
cv2.imshow("Image", image)
cv2.imshow("Edged", edged)
cv2.waitKey(0)
cv2.destroyAllWindows()
cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key = cv2.contourArea, reverse=True)[:5]
for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    if len(approx) == 4:
        screenCnt = approx
        break
print("STEP 2: Find contours of paper")
cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 3)
cv2.imshow("Outline", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
warped = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)
warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
T = threshold_local(warped, 11, offset = 10, method = "gaussian")
warped = (warped > T).astype("uint8") * 255
print("STEP 3: Apply perspective transform ")
cv2.imshow("Original", imutils.resize(orig, height = 650))
cv2.imshow("Scanned", imutils.resize(warped, height = 650))
cv2.imwrite(r"C:\Users\admin\Desktop\python\4Copy.jpg",warped);
cv2.waitKey(0)
imS = cv2.resize(warped, (1350, 1150))
cv2.imshow("output",imS)
cv2.imwrite(r'C:\Users\admin\Desktop\python\Output Image.jpg', imS)
cv2.waitKey(0)

#image to string conversion
from PIL import Image
import PIL.Image

from pytesseract import image_to_string
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
TESSDATA_PREFIX = 'C:/Program Files(x86)/Tesseract-OCR'
output=pytesseract.image_to_string(PIL.Image.open('Output Image.png').convert("RGB"),lang='eng')
myfile=open(r"C:\Users\admin\Desktop\python\demo3.txt",'w')
myfile.write(output)
myfile.close()
f=open(r"C:\Users\admin\Desktop\python\demo3.txt",'rt')
print(f.read())