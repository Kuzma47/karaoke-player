import unittest

from config import *
from modules.script import calculate_line_timing,\
    automatic_method, add_timings, real_time_method


class ConfigTesting(unittest.TestCase):
    def test_colors_are_correct(self):
        m = [BACKGROUND_COLOR, BUTTON_COLOR, BUTTON_TEXT_COLOR,
             MAIN_TEXT_COLOR, KARAOKE_TEXT_COLOR]
        for color in m:
            self.assertTrue(len(color) == 7 and color[0] == '#')


class TextModuleTesting(unittest.TestCase):
    def test_real_time(self):
        self.assertRaises(Exception, real_time_method, '123.txt', '-')

    def test_adding_timings(self):
        lines = ['A B C\n', 'D E F']
        tact = 10
        self.assertEqual(add_timings(lines, tact),
                         ['A:2.5; B:2.5; C:2.5;\n',
                          'D:3.3333333333333335; '
                          'E:3.3333333333333335; '
                          'F:3.3333333333333335;\n'])

    def test_automatic_method(self):
        self.assertRaises(Exception, automatic_method, 'none', 50, 10)

    def test_calculating_timing(self):
        line = 'A B C D'
        line_time = 4
        self.assertEqual(calculate_line_timing(line, line_time),
                         'A:1.0; B:1.0; C:1.0; D:1.0; \n')


if __name__ == '__main__':
    unittest.main()
