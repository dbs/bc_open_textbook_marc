#!/usr/bin/env python3

from lxml import etree

ns = {'marc': 'http://www.loc.gov/MARC21/slim'}
tree = etree.parse('bccampus_rda.xml')
root = tree.getroot()
for eight in root.findall('.//marc:datafield[@tag="856"]', ns):
    nine = etree.SubElement(eight, 'subfield', code='9')
    nine.text = 'LUSYS'
    y = etree.SubElement(eight, 'subfield', code='y')
    y.text = 'Available online / Disponible en ligne'
tree.write('osul.xml')
