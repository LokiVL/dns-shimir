import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from typing import List
from statistics import mean
from ping3 import ping
from tqdm import tqdm

'''
This file was created to storage utilities functions 
and libraries used in dns-shimir.
'''

def clearScreen():
    os.system('cls')

def printTitle(title):
    print("\n====== {} ======\n".format(title))