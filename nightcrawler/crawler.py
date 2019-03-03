#!/bin/env python
# -*- coding: utf-8 -*-

# Author: Grzegorz Szczudlik
# Date: 02.03.19 18:21

import argparse
import re
import sys

from nightcrawler import logger
from nightcrawler.request import PageCrawler


def url_validator(url):
    result = re.search('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+/.*', url)
    if not result:
        raise argparse.ArgumentTypeError('Invalid URL provided: %s' %url)
    return url


def main():
    parser = argparse.ArgumentParser(description="Crawler that recursively search for links on sites")
    # parser.add_argument("--output", "-o", default=sys.stdout,
    #                     help="Path to the file to store the output (default: STDOUT)")
    parser.add_argument("--debug", "-d", dest="level", action='store_const', default=logger.WARN, const=logger.DEBUG,
                        help="Be more verbose over what the script is doing")
    parser.add_argument("URL", nargs=1, type=url_validator, help="URL to start crawling from")

    args = parser.parse_args(sys.argv[1:])
    log = logger.getLogger('')
    log.setLevel(args.level)

    for url in args.URL:
        pc = PageCrawler(url)
        pc.process()


if __name__ == "__main__":
    main()
