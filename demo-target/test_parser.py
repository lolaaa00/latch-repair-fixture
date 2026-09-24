import unittest
from parser import parse_csv


class ParserTests(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(parse_csv('name,value\nalice,one\n'), [['name', 'value'], ['alice', 'one']])

    def test_quoted_lf(self):
        self.assertEqual(parse_csv('name,value\nalice,"one\ntwo"\n'), [['name', 'value'], ['alice', 'one\ntwo']])

    def test_quoted_crlf(self):
        self.assertEqual(parse_csv('name,value\r\nalice,"one\r\ntwo"\r\n'), [['name', 'value'], ['alice', 'one\r\ntwo']])


if __name__ == '__main__':
    unittest.main()
