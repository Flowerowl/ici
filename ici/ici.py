#!/usr/bin/env python
#encoding:utf-8
from __future__ import print_function, unicode_literals

import re
import sys
import getopt
import logging
from xml.dom import minidom
from collections import namedtuple
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

from termcolor import colored


KEY = 'E0F0D336AF47D3797C68372A869BDBC5'
URL = 'http://dict-co.iciba.com/api/dictionary.php'
TAG = namedtuple('TAG', 'value color')
TAG_DICT = {
    'ps': TAG('[%s]', 'green'),
    'fy': TAG('%s', 'green'),
    'orig': TAG('ex. %s', 'blue'),
    'trans': TAG('    %s', 'cyan'),
    'pos': TAG('%s'.ljust(12), 'green'),
    'acceptation': TAG('%s', 'yellow')
}


logger = logging.getLogger(__name__)


def get_response(words):
    try:
        response = urlopen(URL + '?key=' + KEY + '&w=' + words)
    except Exception:
        logger.error('哎哟,好像出错了')
        return
    return response


def read_xml(xml):
    dom = minidom.parse(xml)
    return dom.documentElement


def show(node):
    if not node.hasChildNodes():
        if node.nodeType == node.TEXT_NODE and node.data != '\n':
            tag_name = node.parentNode.tagName
            content = node.data.replace('\n', '')
            if tag_name in TAG_DICT.keys():
                tag = TAG_DICT[tag_name]
                print (colored(tag.value % content, tag.color))
    else:
        for e in node.childNodes:
            show(e)


def main():
    try:
        options, args = getopt.getopt(sys.argv[1:], ["help"])
    except getopt.GetoptError as e:
        pass

    match = re.findall(r'[\w.]+', " ".join(args).lower())
    words = "_".join(match)
    response = get_response(words)
    if not response:
        return
    root = read_xml(response)
    show(root)


if __name__ == '__main__':
    main()
