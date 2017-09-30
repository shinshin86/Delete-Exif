# -*- coding: utf-8 -*-
from PIL import Image
from PIL.ExifTags import TAGS
import os
import uuid
from flask import Flask, request
from flask import render_template, jsonify
from werkzeug import secure_filename


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    filename = secure_filename(f.filename)
    (fn, ext) = os.path.splitext(filename)
    tmp_file_name = uuid.uuid1().hex + ext
    input_path = os.path.join("static", "tmp", tmp_file_name)
    print("upload file :", input_path)
    f.save(input_path)
    res = delete_exif(input_path)
    if res is not False:
        return jsonify({"filename": f.filename,
                        "result": res})


def delete_exif(file):
    file_extension = os.path.splitext(file)

    target_file_extension = [".jpeg", ".jpe", ".jpg", ".JPEG"]
    if file_extension[1] in target_file_extension:
        ret = {}
        inFileName  = file
        outFileName = file

        infile = Image.open(inFileName)
        try:
            info = infile._getexif()

            if(info == None):
                print("This file does not process : " + file)
                return "false"

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

            return "true"
        except:
            print("=== ERROR => This file cannot be processed!! ===")
            print("FILE NAME : " + file)
            print("================================================")
            return "false"

    else:
        print("This file is not supported : " + file)
        return "false"


if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 3000)), debug=True)
