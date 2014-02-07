#!/usr/bin/env python
#encoding:utf-8
import sys
import urllib2
import getopt
from xml.dom import minidom


KEY = 'E0F0D336AF47D3797C68372A869BDBC5'
URL = 'http://dict-co.iciba.com/api/dictionary.php'

def get_response(word):
    response = urllib2.urlopen(URL + '?key=' + KEY + '&w=' + word)
    read_xml(response)

def read_xml(xml):
    dom = minidom.parse(xml)
    root = dom.documentElement
    show(root)

def show(node):
    if not node.hasChildNodes():
        if node.nodeType == node.TEXT_NODE:
            if node.data != '\n':
                print node.data.replace('\n', '')
    else:
        for e in node.childNodes:
            show(e)

def main():
    try:
        options, args = getopt.getopt(sys.argv[1:], ["help"])
    except getopt.GetoptError as e:
        pass

    word = " ".join(args)
    get_response(word)

if __name__ == '__main__':
    main()
