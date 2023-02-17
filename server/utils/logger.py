'''
Author: Frank Chu
Date: 2023-02-13 21:12:31
LastEditors: Frank Chu
LastEditTime: 2023-02-16 19:01:30
FilePath: /SmartSpeaker/code/utils/logger.py
Description: 

Copyright (c) 2023 by ${git_name}, All Rights Reserved. 
'''
import logging

# Create and configure logger
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

# Creating an object
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

