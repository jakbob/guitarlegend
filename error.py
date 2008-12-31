# -*- coding: utf-8 -*-
#
# error.py
#
# Defines functions for error handling and logging.
#
# (c) Jonne Mickelin 2008

import sys
import logging
from logging import debug, info, warning, error, critical

import options

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename=options.__appname__ + '.log',
                    filemode='w')

# The bail_out command is given separate from the logging functions, 
# in order to give the option to continue running even though an
# error occurred.

def bail_out(err):
    """Print an error in a user friendly manner and exit the program.

    Arguments:
    err -- Not None means that an exception ocurred, 
           which will be re-raised in debug mode."""

    if options.DEBUG and err is not None:
        raise # Ignore the pretty output
    else:
        message = "An error occurred. See the log file (%s) for details.\n" % (options.__appname__ + ".log")
        sys.stderr.write(message)
        sys.exit(1)
