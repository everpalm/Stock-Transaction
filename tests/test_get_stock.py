import pytest
import logging
#import sys
#import requests
#import codecs
#import json
import pandas as pd
from datetime import datetime
from stock.get_stock import MyStock as MS

#import matplotlib.pyplot as plt
from time import sleep

#sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TestMyStock():
    def test_get_data(self):
       logger.debug(f'this is a test')
       #list_df = MS.get_data('20161125')