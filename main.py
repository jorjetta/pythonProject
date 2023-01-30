import unittest


def isPalindrome(string: str) -> bool:
    string_len = len(string)
    isPalindrom = True
    middle = string_len // 2
    for i in range(0, middle):
        firts = string[i]
        last = string[-i - 1]
        if firts == last:
            isPalindrom = True
        else:
            isPalindrom = False
            break
    return isPalindrom


# string = input("your text\n")
# result = isPalindrome(string)
# if result is True:
#     print("true")
# else:
#     print("false")


class MyTestCase(unittest.TestCase):
    def test(self):
        with self.assertRaises(Exception) as context:
            isPalindrome(187)

    def test_bad(self):
        assert isPalindrome("abvvdba") is False

    def test_good(self):
        assert isPalindrome("abba") is True

if __name__ == '__main__':
    unittest.main()