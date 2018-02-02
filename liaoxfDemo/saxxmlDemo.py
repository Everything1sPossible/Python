from xml.parsers.expat import ParserCreate
from xml.sax.handler import ContentHandler
from xml.sax import make_parser


class DefaultSaxHandler(object):

    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)


xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''
handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)
"""
============================================================================
"""
print("============================================================================")


class MovieHandler(ContentHandler):
    def __init__(self):
        self.inTitle = False
        self.mapping = {}

    def startElement(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def characters(self, data):
        print('sax:char_data: %s' % data)

    def endElement(self, name):
        print('sax:end_element: %s' % name)


parser = make_parser()
handler = MovieHandler()
parser.setContentHandler(handler)
parser.parse('movies.xml')