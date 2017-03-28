==========================================================
Image to ASCII HTTP Service
==========================================================

Overview
========

It's a small http serivce built upon Flask, Pillow and Numpy.
It converts images (png/jpg/bmp) to their ASCII version.

To use the service, user should POST their binary image file to '/upload'
and the converted image will be returned as JSON.

To get a basic feeling of its function, user can go to the project folder
and run the demo as (change the url if the http service is not running locally)::

   python demo.py

The returned result is in JSON::

   {
   "data":[[row1], [row2], ..],

   "message": "Image converted.",

   "status": 200
   }

each row in the 'data' can be considered one row of pixels of the converted image.

The three major components of building this service are:

**Flask**    The micro web framework

**Pillow**   The Python image library

**Numpy**    The Python numerical library

There are no other dependencies for this service.

Project Files
=============
**img2ascii.py**    The main Flask app.

**img_converter.py**  Converter function from image to ascii

**demo.py**  demonstration of the function

**tests.py**  Tests

**requirements.txt**  Python package dependencies

**fruits.png and Lenna.png**  Two sample images for testing and demo

Build  and Test
============================================
To set up the development, in the folder of the project, run::

    virtualenv --python=/usr/bin/python3 env

then activate the new environment by::

    source env/bin/activate

after this, install all the dependencies by run::

    pip install -r requirements.txt

then it's done.

To run the app locally, you can do like this::

    python img2ascii.py

To test the app, just run::

    python tests.py

To test the app manually and get a demo of the function, just run::

    python demo.py

or you can use your favorite command line tools such as curl or httpie to test
/upload when the service is up.
