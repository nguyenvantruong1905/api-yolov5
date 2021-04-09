from flask import Flask,jsonify
from flask_restful import Api, Resource
from detect import RealTimeAPI
import argparse
import time
from pathlib import Path

import cv2
import torch
import torch.backends.cudnn as cudnn
from numpy import random

from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages
from utils.general import check_img_size, check_requirements, check_imshow, non_max_suppression, apply_classifier, \
    scale_coords, xyxy2xywh, strip_optimizer, set_logging, increment_path
from utils.plots import plot_one_box
from utils.torch_utils import select_device, load_classifier, time_synchronized

app = Flask(__name__)
api = Api(app)

api.add_resource(RealTimeAPI, '/api')

if __name__ == "__main__":
  app.run(host='127.0.0.1')