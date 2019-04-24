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
                    8, 'd.g'),
                ]

        for lines, index, result in test_patterns:
            with self.subTest(lines=lines, index=index, result=result):
                self.assertEqual(seeker.seek_key(lines, index), result)

    def test_dig_key(self):
        """ dig_keyのテスト """

        test_patterns = [
                (
                    ['{',
                     '  "a": "aaa"',
                     '}',
                     ],
                    'a', [1, 2, 'a']),
                (
                    ['{',
                     '  "a": "aaa"',
                     '  "b": "bbb"',
                     '}',
                     ],
                    'b', [2, 2, 'b']),
                (
                    ['{',
                     '  "a": "aaa"',
                     '  "b": {',
                     '    "c": "ccc"',
                     '  }',
                     '}',
                     ],
                    'b.c', [3, 4, 'b.c']),
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
                    'd.f', [5, 4, 'd.f']),
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
                    'd.g', [8, 4, 'd.g']),
                (
                    ['{',
                     '  "a": "a:a:a"',
                     "  'd': {",
                     '    "f": "fff"',
                     '    "g": "ggg"',
                     '  }',
                     '}',
                     ],
                    'd.h', [2, 2, 'd']),
                ]

        for lines, key, result in test_patterns:
            with self.subTest(lines=lines, key=key, result=result):
                self.assertEqual(seeker.dig_key(lines, key), result)
