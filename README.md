## What it does

Runs commands on test files and compares the output to the expected output files (for testing homework). More specifically:

For each output file (files with the extension specified by the constant `OUTPUT_SUFFIX`), test output against the output of the corresponding test input file (with extension `TEST_SUFFIX`) being run with the `RUN_COMMAND`.

## Required Libraries

You will need the following installed to run this script:

<pre>
python
nose (a python testing framework)
</pre>

For colorized output, install the nose plugin yanc:

<pre>
pip install yanc
</pre>

## How to run it

Change the following constants at the top as needed:

<pre>
RUN_COMMAND
TEST_DIR
</pre>

Run the script with:

<pre>
nosetests -v test_runner.py
</pre>

Or better, if you have yanc installed:

<pre>
nosetests -v --with-yanc test_runner.py
</pre>

<br />

## Copyright and licence

Copyright (C) 2012 Dillon Kearns

Released under the MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
