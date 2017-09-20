import os
from shutil import copyfile


all_subdirs = [d for d in os.listdir('C:\Users\Darius\Desktop\Flytrex')]
filter_subdirs = []

for f in all_subdirs:
    if f.find('.') == -1:
        filter_subdirs.append(f)

latest_subdir = max(filter_subdirs)

copyfile('#directories', 'adsfaldjf')