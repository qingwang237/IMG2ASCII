"""The HTTP service for converting an image to its ASCII representation.

Implemented with Flask, Pillow and Numpy

"""
from flask import Flask, request, jsonify
from img_converter import img2ascii

# Flask application initilization
app = Flask(__name__)

# Define file extensions allowed for uploading/ limit to single image files
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'bmp'])


def is_image_file(filename):
    """Return True if the file is an image file."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/', methods=['GET'])
def index():
    """Home but does nothing except returning a prompt."""
    return "Img2Ascii HTTP Service. Post your image file to /upload"


@app.route('/upload', methods=['POST'])
def upload():
    """Image to ASCII art endpoint."""
    # Get uploaded file name
    file = request.files['file']
    # Check if the file is allowed based on file extensions
    if file and is_image_file(file.filename):
        converted_image = img2ascii(file)
        resp = jsonify(status=200, message="Image converted.",
                       data=converted_image)
        resp.status_code = 200
        return resp
    else:
        # Return invalid file format error as JSON
        resp = jsonify(status=400, message="Invalid file format.")
        resp.status_code = 400
        return resp


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True
    )
