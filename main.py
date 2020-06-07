from selectorlib import Extractor
import json
import sys
import urllib.request

website = sys.argv[1]
extractor_file = sys.argv[2]

# get the webpage
with urllib.request.urlopen(website) as resource:
    # read the page content
    html = resource.read().decode(resource.headers.get_content_charset())

    # load the selectorlib file
    # search for selectorlib chrome extensions and
    # read some example to see how to create one of the file needed to get the results
    e = Extractor.from_yaml_file(extractor_file)

    # print output that can be parsed by interfaces,
    # later should be saved in a file called something like "<website>_<timestamp>.json"
    # and used to then calculate statistics
    print(json.dumps(e.extract(html), indent=4))
