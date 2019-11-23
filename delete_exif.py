# -*- coding: utf-8 -*-
from PIL import Image
from PIL.ExifTags import TAGS
import os
import glob

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
WORK_DIR = 'work'
RESULT_DIR = 'result'

# Get all of the image files that exist under the "work" directoly.
fileList = [r.split('/')[-1] for r in glob.glob(os.path.join(CURRENT_PATH, WORK_DIR,'*'))]
print("=== TARGET FILE LIST => ", fileList)

# Delete a Exif data
for file in fileList:
    file_extension = os.path.splitext(file)

    target_file_extension = [".jpeg", ".jpe", ".jpg", ".JPEG"]
    if file_extension[1] in target_file_extension:
        ret = {}
        inFileName = os.path.join(CURRENT_PATH, WORK_DIR, file)
        outFileName = os.path.join(CURRENT_PATH, RESULT_DIR, file)

        infile = Image.open(inFileName)
        try:
            info = infile._getexif()

            if(info == None):
                print("This file does not process : " + file)
                continue

            for tag, value in info.items():
                decoded = TAGS.get(tag, tag)
                ret[decoded] = value
            ret['XResolution'] = 0
            ret['WhiteBalance'] = 0
            ret['ResolutionUnit'] = 0
            ret['SubsecTimeOriginal'] = 0
            ret['Model'] = 0
            ret['Orientation'] = 0
            ret['DateTimeDigitized'] = 0
            ret['ExposureMode'] = 0
            ret['DateTime'] = 0
            ret['YResolution'] = 0
            ret['Make'] = 0
            ret['ComponentsConfiguration'] = 0
            ret['ApertureValue'] = 0
            ret['ColorSpace'] = 0
            ret['ExposureProgram'] = 0
            ret['FNumber'] = 0
            ret['ShutterSpeedValue'] = 0
            ret['MeteringMode'] = 0
            ret['LensModel'] = 0
            ret['LensMake'] = 0
            ret['ExifVersion'] = 0
            ret['FlashPixVersion'] = 0
            ret['FocalLength'] = 0
            ret['ExposureTime'] = 0
            ret['SensingMethod'] = 0
            ret['MakerNote'] = 0
            ret['ExifOffset'] = 0
            ret['SubjectLocation'] = 0
            ret['FocalLengthIn35mmFilm'] = 0
            ret['Software'] = 0
            ret['Flash'] = 0
            ret['ISOSpeedRatings'] = 0
            ret['SubsecTimeDigitized'] = 0

            infile.save(outFileName)
            infile.close()
            print("=== SUCCESS => ", outFileName)
        except:
            print("=== ERROR => This file cannot be processed!! ===")
            print("FILE NAME : " + file)
            print("================================================")


    else:
        print("This file is not supported : " + file)

