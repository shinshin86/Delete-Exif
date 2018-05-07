# Delete-Exif
Delete a Exif at JPEG file.


[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](./LICENSE)
------
## Install

    git clone https://github.com/shinshin86/Delete-Exif.git

## Install library

	pip install pillow
	
	# web only
	pip install flask
	pip install -U flask-cors

### And using React/Redux etc...

```bash
cd Delete-Exif/delete_exif_web/frontend
yarn # or "npm install"
```



## How to use - command line

1. Put a target JPEG file in the ``delete_exif_cli/work`` directory.

2. Run to python script!

   ```bash
   cd Delete-Exif/delete_exif_cli
   python delete_exif_cli.py
   ```

3. Image files(Erased a exif data) stored a "delete_exif_cli/result" directory by Python script.


## How to use (web)

Running Backend server

	cd Delete-Exif/delete_exif_web/backend
	python delete_exif_web.py

Running Frontend's local server

```bash
cd Delete-Exif/delete_exif_web/frontend
yarn run start # npm run start
```

**Browser access to "localhost:3000"**



## Concurrent Start (web)

```bash
cd Delete-Exif/delete_exif_web/
./start.sh
```

**Browser access to "localhost:3000"**