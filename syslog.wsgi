#!/bin/python3

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/syslog")

from syslog_app import app as application
