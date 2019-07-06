# Python-Lab-Report-Management

The project is related to medical report management. Where image of the report is given as input and extract important data and store it into database.


**Software packs need**

- Anaconda 3 (Tool comes with most of the required python packages along with python3 & spyder IDE)

- Tesseract Engine (Must need to be installed)


**Python packages needed**
- OpenCv
- Numpy
- Imutils
- Argparse
- Skimage
- PIL
- Pytesseract

**About Project**
- As the name of the project Lab report management we are trying to devlope software which is useful for storing medical details of patients. This Software actually convert images(jpg,png) into text file.
- And then from this text file extract important data(Doctor name,Lab name,etc.)

**Phases**


**Phase 1- Developed Scanner using OpenCv**

- Building a scanner with OpenCV can be accomplished in just three simple steps:

  Step 1: Detect edges.

  Step 2: Use the edges in the image to find the contour (outline) representing the piece of paper being scanned.

  Step 3: Apply a perspective transform to obtain the top-down view of the document.
  
- Step 1: Detect edges


![edge detect](https://user-images.githubusercontent.com/51942846/60758475-bc55e480-a034-11e9-9cd4-eff05cee4d46.PNG)


- Step 2: Find Outline


[
![outline](https://user-images.githubusercontent.com/51942846/60758530-85340300-a035-11e9-8fcf-af3a7c2005da.PNG)
](url)


- Step 3: Apply a perspective transform to obtain the top-down view of the document.








