import json
import os
import sys
import unittest
from heuristic_test import HeuristicTests


# task = sys.argv[1]
testLoad = unittest.TestLoader()
suite = unittest.TestSuite(testLoad.loadTestsFromTestCase(HeuristicTests))
with open(os.devnull, "w") as f:
    runner = unittest.TextTestRunner(verbosity=0)
    result = runner.run(suite)
    if len(result.errors) == 0 and len(result.failures) == 0:
        print('{"verdict": "Ok", output: "Все тесты прошли успешно"}')
    if len(result.errors) != 0:
        print(
            f'{{"verdict": "RuntimeError", "output": "ERROR: {json.dumps(str(result.errors[0][0]))} \\n {json.dumps(str(result.errors[0][1]))}"}}')
    elif len(result.failures) != 0:
        # print(f'{{"verdict": "RuntimeError", "output": "FAIL: {json.dumps(str(result.failures[0][0]))} \\n {json.dumps(str(result.failures[0][1]))}"}}')
        print(f'{{"verdict": "RuntimeError", "output": "FAIL: {result.failures[0][0]} \\n' + result.failures[0][
                                                                                                     1].replace('\\', r"\\").replace('"', r"\'") + "}")
# print(result.failures)
# for fail in result.failures:
#     print(fail)
