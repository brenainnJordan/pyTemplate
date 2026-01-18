import sys

from Qt import QtWidgets

from .. import testBase

class QtTestCase(testBase.TestCase):
    def setUp(self):
        super(QtTestCase, self).setUp()

        self.q_app = QtWidgets.QApplication(sys.argv)
