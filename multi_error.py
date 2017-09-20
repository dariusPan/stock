import sys, unittest
from datetime import datetime

class TestCase(unittest.TestCase):

    def setUp(self):
        some_code

    def test_case(self):
        blah-blah-blah

    def tearDown(self):
        if sys.exc_info()[0]:  # Returns the info of exception being handled
            fail_url = self.driver.current_url
            print fail_url
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
            self.driver.get_screenshot_as_file('/path/to/file/%s.png' % now) # my tests work in parallel, so I need uniqe file names
            fail_screenshot_url = 'http://debugtool/screenshots/%s.png' % now
            print fail_screenshot_url
        self.driver.quit()
