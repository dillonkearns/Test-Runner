#! /usr/bin/python

import os
import glob
import subprocess
import re

RUN_COMMAND = "scala notJS "
TEST_SUFFIX = ".not"
OUTPUT_SUFFIX = ".out"
TEST_DIR = "testSuite"

MESSAGE_EXPECTED = "EXPECTED"
MESSAGE_BUT_GOT = "BUT GOT"

def sort_nicely(l):
  """
  Sort the given list in the way that humans expect.
  source: http://www.codinghorror.com/blog/2007/12/sorting-for-humans-natural-sort-order.html
  """
  convert = lambda text: int(text) if text.isdigit() else text
  alphanum_key = lambda key:[convert(c) for c in re.split('([0-9]+)', key)]
  l.sort(key=alphanum_key)

def testAll():
    testOutputPairNames = []

    for testFile in glob.glob(os.path.join(TEST_DIR, "*" + OUTPUT_SUFFIX)):
        testOutputPairNames.append(re.sub(OUTPUT_SUFFIX, "", testFile))

    sort_nicely(testOutputPairNames)
    testFiles = [os.path.abspath(name + TEST_SUFFIX) for name in testOutputPairNames]
    outputFiles = [os.path.abspath(name + OUTPUT_SUFFIX) for name in testOutputPairNames]

    for testFileName, testOutputFile in zip(testFiles, outputFiles):
        expectedOutput = open(testOutputFile).read()
        actualOutput = subprocess.check_output(RUN_COMMAND + "'" + testFileName + "'" + '; exit 0',
                                               stderr=subprocess.STDOUT, shell=True)

        def areEqual(expected, actual):
          # only compare the first line of expected and actual if the output expects
          # an error (since stack traces won't match)
            if re.search('cs162\..*', expected):
                expected = expected.splitlines()[0]
                actual = actual.splitlines()[0]
            assert expected == actual, "\n\n%s\n%s\n\n%s\n%s\n\n" % (MESSAGE_EXPECTED, expected, MESSAGE_BUT_GOT, actual)

        areEqual.description = os.path.basename(testFileName)
        yield areEqual, expectedOutput, actualOutput
