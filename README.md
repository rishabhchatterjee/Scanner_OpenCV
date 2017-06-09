# Scanner_OpenCV

Can scan documents / bills / cheques etc. The Prereq is OpenCV 3.1 and Python 2.7. Learnt how to do this from a course by Adrian at Pyimagesearch. The guy is a legend. 
Also, I am using Adrian's library imutils which can be installed by 

$ pip install imutils 

# Method 

So this script uses two main things : edge detection and four point transform. 
Edge Detection : Luckily, openCV has a builtin function which helps in finding contours. We are using that for edge detection. The only neg point is that our assumption is that we will be given an imag with 4 edges (like in normal scanning docs) which openCV fails to detect exactly 4 edges at times. In order to prevent this, ensure that the backround is different from teh color of paper etc you want to scan.
Four Point transform : This is needed because most of the time the image to scan is NOT a bird's eye view, ie, it is tilted and stuff. The four point transform (in transform.py) uses builtin openCV functions to detect the 4 corner edges in clockwise sequence starting from Top Left and returns the coordinates. We then resize the image using Adrian's imageutil API to make the scanned image straight, resize it, etc.

# Making it Run

The way to call call this is 

$ python scan.py --image path/to/image

Ensure that both the files are in same directory

# Closing
Note : The main idea behind the code is from Pyimagesearch (taking a course online rn), I have simply implemented and edited the code at places (the original crashes due to updates in openCV version, python versions etc) and built upon pre existing code. No intent for commercial use, if you do use it be sure to cite Pyimagesearch and me accordingly.


:))
