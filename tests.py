"""Unit tests for the Img2Ascii HTTP service.

Use flask_testing for better unit testing structure.

"""

import unittest
import requests
from flask_testing import LiveServerTestCase
from img2ascii import app


class Img2AsciiTest(LiveServerTestCase):
    """Tests for Img2Ascii endpoint."""

    def create_app(self):
        """Create the testing flask app instance."""
        app.config['TESTING'] = True
        # Default port is 8000
        app.config['LIVESERVER_PORT'] = 8000
        # Default timeout is 5 seconds
        app.config['LIVESERVER_TIMEOUT'] = 5
        return app

    def test_server_is_up_and_running(self):
        """Test / to see if the server is up and running."""
        print(self.get_server_url())
        response = requests.get(self.get_server_url())
        self.assertEqual(response.status_code, 200)

    def test_upload_endpoint(self):
        """Test the img2ascii live service."""
        with open('fruits.png', 'rb') as fin:
            files = {'file': fin}
            response = requests.post(self.get_server_url() + "/upload",
                                     files=files)
            self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
