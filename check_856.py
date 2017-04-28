#!/usr/bin/env python3

from lxml import etree
import requests

ns = {'marc': 'http://www.loc.gov/MARC21/slim'}
tree = etree.parse('bccampus_rda.xml')
root = tree.getroot()
for record in root:
    title = record.find('.//marc:datafield[@tag="245"]/marc:subfield[@code="a"]', ns).text
    for url in record.findall('.//marc:datafield[@tag="856"]/marc:subfield[@code="u"]', ns):
        try:
            r = requests.head(url.text)
            if r.status_code != 200:
                print("%s %s %s" % (r.status_code, title, url.text))
        except Exception as inst:
            print("%s %s %s" % (inst, title, url.text))
