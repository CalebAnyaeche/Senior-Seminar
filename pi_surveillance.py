# import packages 
from pyimagesearch.tempimage import TempImage
from picamera.array import PiRGBArray
from picamera import PiCamera
import argparse
import warnings
import json

# construct the argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--conf", required=True,
        help="path to the JSON configuration file")
args = vars(ap.parse_args())
 
# filter warnings and load the configuration
warnings.filterwarnings("ignore")
conf = json.load(open(args["conf"]))

