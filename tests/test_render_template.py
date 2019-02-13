import unittest
from conf import render_template

class TestRenderTemplate(unittest.TestCase):
  def test_happy(self):
    # Test the happy case
    d = {
        'username': 'abc',
        'password': 'cdefg'
        }
    rendered = render_template('tests/data/test_template1.yml', d)
    expected = "user: abc\npass: cdefg\n"
    self.assertEqual(rendered, expected)
