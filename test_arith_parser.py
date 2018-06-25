from arith_parser import ArithParser
import unittest

class TestArithParser(unittest.TestCase):
    def test_in_to_post1(self):
        parser = ArithParser()
        infix = 'A+B*C'
        self.assertEqual(parser.in_to_post(infix), 'ABC*+')

    def test_in_to_post2(self):
        parser = ArithParser()
        infix = 'A*(B+C)'
        self.assertEqual(parser.in_to_post(infix), 'ABC+*')

    def test_in_to_post3(self):
        parser = ArithParser()
        infix = '2*(3+4)'
        self.assertEqual(parser.in_to_post(infix), '234+*')

    def test_in_to_post4(self):
        parser = ArithParser()
        infix = '(4+5)/(6*7)'
        self.assertEqual(parser.in_to_post(infix), '45+67*/')

    def test_post_to_result1(self):
        parser = ArithParser()
        postfix = '234+*'
        self.assertEqual(parser.post_to_result(postfix), 14)

    def test_post_to_result2(self):
        parser = ArithParser()
        postfix = '84/67+*'
        self.assertEqual(parser.post_to_result(postfix), 26)

    def test_post_to_result3(self):
        parser = ArithParser()
        postfix = '927+/64-+'
        self.assertEqual(parser.post_to_result(postfix), 3)

    def test_parse1(self):
        parser = ArithParser()
        input = '2*(3+4/2)'
        self.assertEqual(parser.parse(input), 10)

    def test_parse2(self):
        parser = ArithParser()
        input = '(4-1)*(3/1/3)'
        self.assertEqual(parser.parse(input), 3)


    def test_parse3(self):
        parser = ArithParser()
        input = '(7+9/3)/(2/1*5)'
        self.assertEqual(parser.parse(input), 1)

if __name__ == '__main__':
    unittest.main()
