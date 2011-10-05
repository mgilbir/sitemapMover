#!/usr/bin/env python

# sitemapMover: Converts Google Sitemap XML to .htaccess 301 redirect rules
# Copyright (C) 2011 by Miguel Eduardo Gil Biraud
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from xml.dom import minidom
import argparse
import sys
import math
from urlparse import urlparse


def extractUrls(xmlData):
	dom = minidom.parseString(xmlData)
	urls = []
	for node in dom.getElementsByTagName('loc'):
		urls.append(node.firstChild.data)

	return urls

def initializeHtaccessRule():
	rule = "Options +FollowSymLinks \nRewriteEngine on \n"	
	return rule

def createHtaccessRule(newBaseUrl, url):
	urlData = urlparse(url)

	escapedNetloc = urlData.netloc.replace( ".", "\\.")
	rule = "RewriteCond %%{HTTP_HOST} ^%(netloc)s$ [NC]\n" % {"netloc": escapedNetloc}
	rule = "RewriteCond %%{REQUEST_URI} ^%(path)s$ [NC]\n" % {"path": urlData.path}
	rule = rule + "RewriteRule .* http://%(redirect)s [R=301,NC,L]\n" % {"redirect": newBaseUrl+urlData.path}

	return rule

if __name__=='__main__':
	parser = argparse.ArgumentParser(description='Convert a sitemap.xml to a list of .htaccess HTTP 301 rules to effectively move a site to a new (sub)domain',
		usage='%(prog)s --destinationDomain destinationDomain sitemapFilename htaccessTempFilename')
	parser.add_argument('--destinationDomain', type=str, required=True, help="The destination domain for the URLs (eg. my.destination-domain.com)")

	parser.add_argument('sitemapFilename', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help="The Google Sitemap XML file to use as source")
	parser.add_argument('htaccessTempFilename', nargs='?', type=argparse.FileType('w'), help="The .htaccess compatible file to be generated with HTTP 301 rules corresponding to the sitemap's URLs")

	try:
		args = parser.parse_args()
	except IOError, msg:
		parser.error(str(msg))


	xmlData = args.sitemapFilename.read();

	args.htaccessTempFilename.write(initializeHtaccessRule())

	urlList = extractUrls(xmlData)
	totalUrlCount = len(urlList)

	print "There are {0} URLs to process".format(totalUrlCount)

	for url in extractUrls(xmlData):
		rule = createHtaccessRule(args.destinationDomain, url)
		args.htaccessTempFilename.write(rule)

	args.sitemapFilename.close()
	args.htaccessTempFilename.close()
