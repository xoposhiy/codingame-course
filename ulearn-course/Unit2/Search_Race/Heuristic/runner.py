import json
import os
import sys
import unittest


def run(test_class):
    testLoad = unittest.TestLoader()
    suite = unittest.TestSuite(testLoad.loadTestsFromTestCase(test_class))
    with open(os.devnull, "w") as f:
        runner = unittest.TextTestRunner(f, verbosity=1)
        result = runner.run(suite)
        if len(result.errors) == 0 and len(result.failures) == 0:
            print('{"verdict": "Ok", "output": "Все тесты прошли успешно"}')
            exit(0)
        if len(result.errors) != 0:
            print(f'{{"verdict": "RuntimeError", "output": "ERROR: {result.errors[0][0]} \\n' + result.errors[0][1].replace('"', r"\'") + "\"}")
        elif len(result.failures) != 0:
            print(f'{{"verdict": "RuntimeError", "output": "FAIL: {result.failures[0][0]} \\n' + result.failures[0][1].replace('"', r"\'") + "\"}")


if __name__ == '__main__':
    module = sys.argv[1]
    task = sys.argv[2]
    m = __import__(module)
    run(getattr(m, task))