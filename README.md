# Delete-Exif
Delete a Exif at JPEG file.


[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](./LICENSE)
------
## Install

    git clone https://github.com/shinshin86/Delete-Exif.git


## Install library

	pip install pillow

### web only

	pip install flask

And Using library

* [jQuery](https://jquery.com/)
* [Bootstrap](https://getbootstrap.com/)
* [Font Awesome](http://fontawesome.io/)
* [DropzoneJS](http://www.dropzonejs.com/)


## How to use - command line

1. Put a target JPEG file in the ``delete_exif_cli/work`` directory.
2. Run to python script!

		cd Delete-Exif/delete_exif_cli
    	python delete_exif_cli.py

3. Image files(Erased a exif data) stored a "delete_exif_cli/result" directory by Python script.


## How to use (web) - [TODO] working progress

	cd Delete-Exif/delete_exif_web
	python delete_exif_web.py
	
Browser access to "localhost:3000"
