#!/usr/bin/python

import logging
import argparse
import os
import os.path
import re

from datetime import datetime
from datetime import timedelta

BasePOSIXTime = datetime(1970, 1, 1)
def GetPOSIXTimestamp(dateTimeObj):
    return int((dateTimeObj - BasePOSIXTime) / timedelta(seconds = 1))

def ListPhotos():
    return

def main():    
    parser = argparse.ArgumentParser(description = 'Flickr RESTful APIs Client')
    parser.add_argument('option', nargs='?', default='list', choices=['list'])
    parser.add_argument('-v', '--verbose', help='verbose messages', action='store_true', dest='verbose')

    args = parser.parse_args()

    CurrentDebugLevel = logging.INFO
    if args.verbose: CurrentDebugLevel = logging.DEBUG
    
    logging.basicConfig(level=CurrentDebugLevel, datefmt='%Y.%m.%d %H:%M:%S', format='%(asctime)s %(message)s')
    logging.debug(args)

    #now = datetime.utcnow()
    now = datetime.now()
    logging.info('Start working ... Now={}[{}]'.format(now.isoformat(), GetPOSIXTimestamp(now)))

    option = args.option.lower()

    if option == 'list':
        ListPhotos()
    else:
        parser.print_help()
        return

if __name__ == '__main__': main()

