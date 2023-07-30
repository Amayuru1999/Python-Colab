import random
import os
from pathlib import Path

# Define paths to image folders
image_path = '/content/images/all'
train_path = '/content/images/train'
val_path = '/content/images/validation'
test_path = '/content/images/test'

# Get list of all images
file_list = list(Path(image_path).glob('*.*'))
file_num = len(file_list)
print('Total images: %d' % file_num)

# Determine number of files to move to each folder
train_percent = 0.8  # 80% of the files go to train
val_percent = 0.1    # 10% go to validation
test_percent = 0.1   # 10% go to test
train_num = int(file_num * train_percent)
val_num = int(file_num * val_percent)
test_num = file_num - train_num - val_num
print('Images moving to train: %d' % train_num)
print('Images moving to validation: %d' % val_num)
print('Images moving to test: %d' % test_num)

# Randomly shuffle the file list
random.shuffle(file_list)

# Create directories if they don't exist
os.makedirs(train_path, exist_ok=True)
os.makedirs(val_path, exist_ok=True)
os.makedirs(test_path, exist_ok=True)

# Move files to the train folder
for i in range(train_num):
    move_me = file_list.pop()
    os.rename(move_me, os.path.join(train_path, move_me.name))

# Move files to validation folder
for i in range(val_num):
    move_me = file_list.pop()
    os.rename(move_me, os.path.join(val_path, move_me.name))

# Move remaining files to test folder
for i in range(test_num):
    move_me = file_list.pop()
    os.rename(move_me, os.path.join(test_path, move_me.name))
