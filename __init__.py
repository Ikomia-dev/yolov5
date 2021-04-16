import sys
import os

# Ugly: add yolov5 root folder to allow torch to find models.yolo while loading .pt models
sys.path.insert(0, os.path.dirname(__file__))