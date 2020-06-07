from selectorlib import Extractor
import json
import sys
import urllib.request
import requests_html

website = sys.argv[1]
extractor_file = sys.argv[2]

# read the page content
with requests_html.HTMLSession() as session:
    r = session.get(website)
    js = r.html.render(timeout=0)
    html = r.html.html

    # load the selectorlib file
    # search for selectorlib chrome extensions and
    # read some example to see how to create one of the file needed to get the results
    e = Extractor.from_yaml_file(extractor_file)

    # print output that can be parsed by interfaces,
    # later should be saved in a file called something like "<website>_<timestamp>.json"
    # and used to then calculate statistics
    print(json.dumps(e.extract(html), indent=4))
