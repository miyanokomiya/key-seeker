from unittest import TestCase
from . import seeker


class TestJsonModule(TestCase):
    """ seekerテスト """

    def test_seek_key(self):
        """ seek_keyのテスト """

        test_patterns = [
                (
                    ['{',
                     '  "a": "aaa"',
                     '}',
                     ],
                    1, 'a'),
                (
                    ['{',
                     '  "a": "aaa"',
                     '  "b": "bbb"',
                     '}',
                     ],
                    2, 'b'),
                (
                    ['{',
                     '  "a": "aaa"',
                     '  "b": {',
                     '    "c": "ccc"',
                     '  }',
                     '}',
                     ],
                    3, 'b.c'),
                (
                    ['{',
                     '  "b": {',
                     '    "c": "ccc"',
                     '  }',
                     '  "d": {',
                     '    "f": "fff"',
                     '  }',
                     '  "a": "aaa"',
                     '}',
                     ],
                    5, 'd.f'),
                (
                    ['// abcd: abcd',
                     '{',
                     '',
                     '  "a": "a:a:a"',
                     '  "b": {',
                     '  }',
                     "  'd': {",
                     '    "f": "fff"',
                     '    "g": "ggg"',
                     '  }',
                     '}',
                     ],
                    9, 'd.g'),
                ]

        for lines, index, result in test_patterns:
            with self.subTest(lines=lines, index=index, result=result):
                self.assertEqual(seeker.seek_key(lines, index), result)
