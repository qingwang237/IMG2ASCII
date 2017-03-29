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

The three major components for building this service are:

**Flask**    The micro web framework, mature and perfect for "micro services"

**Pillow**   The Python image library, very mature and the go-to choice for common image processing tasks

**Numpy**    The Python numerical library, very mature and most powerful

There are no other dependencies for this service. However, for testing and demostration,
the following tools are chosen:

**Flask-testing**    Nice Flask testing extensions and make testing easier

**Requests**  Very mature Python HTTP library and easy to use

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
'/upload' when the service is up. For example::

   curl -i -X POST -H "Content-Type: multipart/form-data" -F "file=@fruits.png" http://localhost:8000/upload
