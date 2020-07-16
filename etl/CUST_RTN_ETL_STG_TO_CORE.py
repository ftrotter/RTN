#!/usr/bin/env python
# coding: utf-8

# In[ ]


#!/usr/bin/env python
# coding: utf-8


#############################################################
# Credentials
#############################################################
MyHost ='???'
MyUser ='???'
TempDB ='???'
SchemaName = "???"

#############################################################
# Libraries
#############################################################
#pip install ipython
#pip install --upgrade covid19dh
#pip install numpy --upgrade
#pip install requests
#pip3 install tabulate
#pip install xlrd
#pip3 install requests-html
#pip install html5lib

from IPython import get_ipython
from covid19dh import covid19
import pytz
import tweepy as tw
import pandas as pd
import numpy as np
from teradataml.dataframe.dataframe import DataFrame, in_schema
from teradataml.dataframe.copy_to import copy_to_sql
from teradataml.context.context import create_context, remove_context, get_connection, get_context
from teradataml.options.display import display
from teradataml.dataframe.fastload import fastload
#import tdconnect
import getpass
import datetime
from datetime import date
from datetime import datetime, timedelta
from datetime import datetime
from teradataml.context.context import *
con = create_context(host=MyHost, username=MyUser, password=getpass.getpass(), temp_database_name=TempDB, logmech='LDAP')

#############################################################
# Stage to Core Loads
#############################################################
def cur_execute (cur, sSQL, params=None):
    cur.execute (sSQL, params)

try:
    # Core Load Calls to Teradata
    cur_execute (con, "CALL "+SchemaName+".ETL_COVID_CASES_CORE (v_MsgTxt,v_RowCnt,v_ResultSet);")
    from datetime import datetime
    datetime.utcnow()
    dateTimeObj = pytz.utc.localize(datetime.utcnow()).astimezone(pytz.timezone('US/Pacific'))
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    print("ETL_COVID_CASES_CORE Finished!  " + timestampStr)

    cur_execute (con, "CALL "+SchemaName+".ETL_LABOR_STATS_CORE (v_MsgTxt,v_RowCnt,v_ResultSet);")
    from datetime import datetime
    datetime.utcnow()
    dateTimeObj = pytz.utc.localize(datetime.utcnow()).astimezone(pytz.timezone('US/Pacific'))
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    print("ETL_LABOR_STATS_CORE Finished!  " + timestampStr)

    cur_execute (con, "CALL "+SchemaName+".ETL_COVID_MODEL_CORE (v_MsgTxt,v_RowCnt,v_ResultSet);")
    from datetime import datetime
    datetime.utcnow()
    dateTimeObj = pytz.utc.localize(datetime.utcnow()).astimezone(pytz.timezone('US/Pacific'))
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    print("ETL_COVID_MODEL_CORE Finished!  " + timestampStr)

    cur_execute (con, "CALL "+SchemaName+".ETL_GOOGLE_MOBILITY_CORE (v_MsgTxt,v_RowCnt,v_ResultSet);")
    from datetime import datetime
    datetime.utcnow()
    dateTimeObj = pytz.utc.localize(datetime.utcnow()).astimezone(pytz.timezone('US/Pacific'))
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    print("ETL_GOOGLE_MOBILITY_CORE Finished!  " + timestampStr)

    cur_execute (con, "CALL "+SchemaName+".ETL_BEA_CORE (v_MsgTxt,v_RowCnt,v_ResultSet);")
    from datetime import datetime
    datetime.utcnow()
    dateTimeObj = pytz.utc.localize(datetime.utcnow()).astimezone(pytz.timezone('US/Pacific'))
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    print("ETL_BEA_CORE Finished!  " + timestampStr)

    cur_execute (con, "CALL "+SchemaName+".ETL_GOOGLE_TREND_CORE (v_MsgTxt,v_RowCnt,v_ResultSet);")
    from datetime import datetime
    datetime.utcnow()
    dateTimeObj = pytz.utc.localize(datetime.utcnow()).astimezone(pytz.timezone('US/Pacific'))
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    print("ETL_GOOGLE_TREND_CORE Finished!  " + timestampStr)

    cur_execute (con, "CALL "+SchemaName+".ETL_COVID19_DATAHUB_CORE (v_MsgTxt,v_RowCnt,v_ResultSet);")
    from datetime import datetime
    datetime.utcnow()
    dateTimeObj = pytz.utc.localize(datetime.utcnow()).astimezone(pytz.timezone('US/Pacific'))
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    print("ETL_COVID19_DATAHUB_CORE Finished!  " + timestampStr)

    cur_execute (con, "CALL "+SchemaName+".ETL_FUEL_PROD_CORE (v_MsgTxt,v_RowCnt,v_ResultSet);")
    from datetime import datetime
    datetime.utcnow()
    dateTimeObj = pytz.utc.localize(datetime.utcnow()).astimezone(pytz.timezone('US/Pacific'))
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    print("ETL_FUEL_PROD_CORE Finished!  " + timestampStr)

    cur_execute (con, "CALL "+SchemaName+".ETL_CONSUMER_SENTIMENT_CORE (v_MsgTxt,v_RowCnt,v_ResultSet);")
    from datetime import datetime
    datetime.utcnow()
    dateTimeObj = pytz.utc.localize(datetime.utcnow()).astimezone(pytz.timezone('US/Pacific'))
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    print("ETL_CONSUMER_SENTIMENT_CORE Finished!  " + timestampStr)
    
except:
    print("An exception occurred")
    
finally:
    cur_execute (con, "CALL "+SchemaName+".ETL_POST_LOAD_CORE (v_MsgTxt,v_RowCnt,v_ResultSet);")
    from datetime import datetime
    datetime.utcnow()
    dateTimeObj = pytz.utc.localize(datetime.utcnow()).astimezone(pytz.timezone('US/Pacific'))
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    print("ETL_POST_LOAD_CORE Finished!  " + timestampStr)
