# What does it do?

Converts a [Sitemap XML](http://www.sitemaps.org/) file to a [.htaccess](http://httpd.apache.org/docs/current/howto/htaccess.html) compatible file with HTTP 301 redirect rules.

It's is an easy way to move all the content described in a [Sitemap XML](http://www.sitemaps.org/) file to a new location without any complex additional configuration. Using [HTTP 301 redirect](http://en.wikipedia.org/wiki/HTTP_301) is the proper way to inform users and crawler bots that a resource has moved permanently.

## Usage

	sitemapMover.py --destinationDomain destionationDomain sitemapFilename htaccessTempFilename

* __--destinationDomain__ The destination domain for the URLs (eg. the.destination-domain.com)
* __sitemapFilename__       The Google Sitemap XML file to use as source
* __htaccessTempFilename__  The .htaccess compatible file to be generated with HTTP 301 rules corresponding to the sitemap's URLs. _Any existing file with the same name will be overwriten!_


## License
It is very easy, feel free to do whatever you want with it. If something bad happens you are on your own and I don't take any responsibility/liability.

The legal mumbo jumbo is a standard [MIT License](http://en.wikipedia.org/wiki/MIT_License).

Copyright (C) 2011 by Miguel Eduardo Gil Biraud

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.