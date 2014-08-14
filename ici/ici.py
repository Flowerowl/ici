#!/usr/bin/env python
#encoding:utf-8
import sys
import urllib2
import getopt
from xml.dom import minidom

from termcolor import colored


KEY = 'E0F0D336AF47D3797C68372A869BDBC5'
URL = 'http://dict-co.iciba.com/api/dictionary.php'


def get_response(word):
    return urllib2.urlopen(URL + '?key=' + KEY + '&w=' + word)


def read_xml(xml):
    dom = minidom.parse(xml)
    return dom.documentElement

def show(node):
    if not node.hasChildNodes():
        if node.nodeType == node.TEXT_NODE and node.data != '\n':
            tag_name = node.parentNode.tagName
            content = node.data.replace('\n', '')
            if tag_name == 'ps':
                print colored('[' + content + ']', 'green')
            if tag_name == 'orig':
                print colored('ex. ' + content, 'blue')
            if tag_name == 'trans':
                print colored('    ' + content, 'cyan')
            if tag_name == 'pos':
                print colored(content, 'green').ljust(12),
            if tag_name == 'acceptation':
                print colored(content, 'yellow')
    else:
        for e in node.childNodes:
            show(e)


def main():
    try:
        options, args = getopt.getopt(sys.argv[1:], ["help"])
    except getopt.GetoptError as e:
        pass

    word = " ".join(args)
    root = read_xml(get_response(word))
    show(root)


if __name__ == '__main__':
    main()
