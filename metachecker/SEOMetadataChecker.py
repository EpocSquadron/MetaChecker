from bs4 import BeautifulSoup


class NoHeadDataException(Exception):
    pass


class SEOMetadataChecker(BeautifulSoup):

    tests = {}

    def __init__(self, args):
        # Parent constructor
        BeautifulSoup.__init__(self, args)

        # Throw exception if we have no head data to inspect
        if self.head is None:
            raise NoHeadDataException('No head data found')

    def register_tests(self, test_dict):

        try:
            for key, value in test_dict.items():
                self.register_test(key, value)

        except Exception as e:
            print('Error registering tests: ', e)

    def register_test(self, test_name, test):

        self.tests[test_name] = test

    def test_all(self):

        try:
            for test_name in self.tests.keys():
                print(
                    'Check for',
                    test_name,
                    'resulted in',
                    self.test(test_name)
                )

        except Exception as e:
            print('Error running all tests: ', e)

    def test(self, test_name):

        try:
            if self.tests[test_name](self.head):
                return True
        except Exception:
            pass

        return False
