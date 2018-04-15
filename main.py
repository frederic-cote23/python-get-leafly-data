import extract_link
import json

def createUrlList(url_file, all_url):
    with open(url_file, 'w') as f:
        f.write(json.dumps(all_url))

url_file = 'extract/url_list.json'

all_url = extract_link.extract_hyperlink_from_rip('raw/all_strains.html')

createUrlList(url_file, all_url)