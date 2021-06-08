import unittest

def is_on_age(age):
    if age >= 18:
        return True
    else:
        return False

class CajaCristalTest(unittest.TestCase):
    def test_is_on_age(self):
        result = is_on_age(21)

        self.assertEqual(result, True)

    def test_is_under_age(self):
        result = is_on_age(17)

        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
