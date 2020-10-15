# How to run

Install OpenCV for the "import cv2" code to work.

``` 
pip install opencv-python
``` 
Clone the repository.
``` 
git clone git@github.com:SHUYAN99/TemplateMatchingForAtariGame.git
``` 
Run the Python code.
``` 
python template_match.py
``` 
The program outputs the a lists of coordinates stating where are the vehicle boundaries given colors as signals, and marks them with bounding boxes. 

[[28, 33, 35, 39], [44, 122, 51, 128], [60, 57, 67, 63], [76, 86, 83, 93], [92, 16, 99, 21], [108, 140, 115, 145], [124, 68, 131, 75], [140, 98, 147, 104], [156, 33, 163, 39], [172, 122, 179, 128], [96, 44, 101, 49]]
##### BEFORE
![alt text](https://github.com/SHUYAN99/TemplateMatchingForAtariGame/blob/master/RZ_2464601_4625.png?raw=true)

##### AFTER
![alt text](https://github.com/SHUYAN99/TemplateMatchingForAtariGame/blob/master/RESULT_4625.png?raw=true)



# Data source
Data is at: https://zenodo.org/record/2603190#.XXpzEnUrK90

The demo picture is from: https://zenodo.org/record/2603190/files/55_RZ_2464601_Aug-11-10-18-09.tar.bz2?download=1.tar.bz2 \
There are 17286 screenshots of the Freeway game in this tar, with which the program written could be used to "box" the vehicles.
