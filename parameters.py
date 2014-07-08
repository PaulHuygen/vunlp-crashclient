#!/usr/bin/env python
# Parameters for vunlp package
# Written by installscript on di jul 30 15:02:31 CEST 2013
import os
VUNLPHOME = os.path.expanduser('~') + '/vunlp'
# DATABASE:
DBFILE = VUNLPHOME + "/vunlptextstore.db"
# Webservice host:
DEFAULT_URL = "http://nlp.labs.vu.nl/ws/"
# DEFAULT_URL = "http://localhost:8090"
LOCKFILE =  VUNLPHOME + "/lock/cronlock"
CRONLOGFILE = VUNLPHOME + "/log/cronlog"
# Supe-host: Access info
SUPER_HOSTNAME = "localhost"
SUPER_USER     = "paul"
SUPER_ROOT     = VUNLPHOME
# Super-host: Scripts
SUPER_UPLOADSCRIPT            = VUNLPHOME + "/bin/from_middle"
SUPER_DOWNLOADTEMPLATE        = VUNLPHOME + "/bin/to_middle {tray}"
SUPER_FILECOUNTINTRAYTEMPLATE = VUNLPHOME + "/bin/nrfiles {tray}"
SUPER_FILELISTTEMPLATE        = VUNLPHOME + "/bin/filelist {tray}"
# Super-host: Path to trays
SUPER_TRAYSPATH    = VUNLPHOME + "/trays"
# Test superhost: Access info
TSUPER_HOSTNAME = "localhost"
TSUPER_USER     = "paul"
TSUPER_ROOT     = VUNLPHOME
# Test superhost: Scripts
TSUPER_UPLOADSCRIPT            = VUNLPHOME + "/bin/from_middle"
TSUPER_DOWNLOADTEMPLATE        = VUNLPHOME + "/bin/to_middle {tray}"
TSUPER_FILECOUNTINTRAYTEMPLATE = VUNLPHOME + "/bin/nrfiles {tray}"
TSUPER_FILELISTTEMPLATE        = VUNLPHOME + "/bin/filelist {tray}"
TSUPER_EMPTY_TRAYS_SCRIPT      = VUNLPHOME + "/bin/emptytrays"
# Test super host: Paths
TSUPER_TRAYSPATH    = VUNLPHOME + "/trays"
#TSUPER_INTRAY      = ""
#TSUPER_PARSESTRAY  = ""
#TSUPER_LOGTRAY     = ""
#TSUPER_TIMEOUTTRAY = ""
