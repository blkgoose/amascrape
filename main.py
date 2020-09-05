from selectorlib import Extractor
import json
import sys
import os.path

extractor_file = sys.argv[1]

try:
    in_file = sys.argv[2]
except:
    in_file = "/dev/stdin"

# read the page content
with open(in_file) as html:
    # load the selectorlib file
    # search for selectorlib chrome extensions and
    # read some example to see how to create one of the file needed to get the results
    e = Extractor.from_yaml_file(extractor_file)

    # print output that can be parsed by interfaces,
    # later should be saved in a file called something like "<website>_<timestamp>.json"
    # and used to then calculate statistics
    print(json.dumps(e.extract(html.read()), indent=4))
