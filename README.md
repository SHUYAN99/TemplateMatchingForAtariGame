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
The program will output the coordinates stating where are the vehicles, and mark them with bounding boxes.

# Data source
Data is at: https://zenodo.org/record/2603190#.XXpzEnUrK90
Get game name and trial ID in excel file;
download corresponding .tar.bz2 file from the list.
e.g., https://zenodo.org/record/2603190/files/55_RZ_2464601_Aug-11-10-18-09.tar.bz2?download=1

Agorithm should output 2 things:
objectID (arbitrary)
object position (x_upperleft,y_upperleft, x_lowerright, y_lowerright)
