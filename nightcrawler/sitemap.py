#!/bin/env python
# -*- coding: utf-8 -*-

# Author: Grzegorz Szczudlik
# Date: 03.03.19 14:38

from nightcrawler import logger

from bs4 import BeautifulSoup


class SitemapGenerator(object):
    log = logger.getLogger('sitemap.SitemapGenerator')
    namespace = "http://www.sitemaps.org/schemas/sitemap/0.9"

    def generate(self, result_set, fd):
        self.log.debug("Generating sitemap")
        xml = BeautifulSoup(features="lxml-xml")
        urlset = xml.new_tag("urlset", xmlns=self.namespace)

        for result in result_set:
            url = self.__generate_entry(xml, result)
            urlset.append(url)
            xml.append(urlset)

        self.log.debug("Writing map to disk")
        fd.write(xml.prettify())

        self.log.debug("Sitemap generated")

    def __generate_entry(self, soup, item):
        self.log.debug("Generatig entry for %s" % item.url)
        url = soup.new_tag("url")

        loc = soup.new_tag("loc")
        loc.string = item.url
        url.append(loc)

        if item.last_modified:
            last = soup.new_tag("lastmod")
            last.string = item.last_modified.isoformat(timespec='seconds')
            url.append(last)

        return url
