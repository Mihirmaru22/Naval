# data ingestion component is used to load and preprocess data for the application
# the main aim is to read data from various sources and make it available for further processing

import os
import sys
from src.exception import customException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
 