#######################################
# Pull data for a specified ticker
#   Report financial outlook and current/historical performance of spcecific ticker symbol from public API financial data
#
# Options (parameters)
#       -x  x array bounds in space delimited format: min max
#
#######################################
###  CB: Basic & Default Settings
#######################################
maxHistoryDays = 1500                   # Maximum number of days in the past that will be considered

#######################################
###  CB: Test Arguments & import base moduels
#######################################
import datetime as dt
import sys
from datetime import date,  timedelta
from argparse import ArgumentParser

### Read passed arguements from the command line
parser = ArgumentParser(
    description='tbd',
    epilog="Example: python .../tickerData.py -d 15 01 2018 -t 'SPY'")
parser.add_argument("-t", "--TickerSymbol", dest="tickerSymbol", help="Text string ticker symbol for the index fund or firm", default="SPY", metavar="TICKER", type=str)
parser.add_argument("-d", "--datePast", dest="pastDate", help="Integers representing a past date from which to perform the reporting", nargs="+", default=(1,1,2018), metavar="dd mm yyyy", type=int)
# Assign to other handles for simplicity in debugging
args = parser.parse_args()
tickerSymbol=args.tickerSymbol
pastDate=args.pastDate

### Try conditions, if fail then exit or revert to default values
try:
    startDate = dt.datetime(pastDate[2], pastDate[1], pastDate[0])
    print(startDate)
    today = date.today()
    endDate = dt.datetime( today.year, today.month, today.day )
    if not endDate > startDate:
        print('\nCritical error encountered during processing.\nDate parameter is not in the past.')
        sys.exit(1)
    if (endDate - startDate).days > maxHistoryDays:
        print('\nParameter date exceeds historical data limit.\nHistorical data limit set to (in days): ' + str(maxHistoryDays))
        startDate = endDate - timedelta(days=maxHistoryDays)
except:
    print('\nTerminating on error\n\n')
    sys.exit(1)

#######################################
###  CB: If conditions passed then import rest of modules
#######################################
import pandas_datareader as pdr
import pandas as pd
from matplotlib import cm
import matplotlib.pyplot as plt

#######################################
### CB: Pull Ticker data from public financial data API
#######################################
HistoricalFirmValuation = pdr.get_data_yahoo(tickerSymbol, startDate, endDate)
# SP500 Index, Market Portfolio proxy
HistoricalIndexFund = pdr.get_data_yahoo("SPY", startDate, endDate)


#######################################
### CB: Report for Ticker
#######################################
plt.plot(HistoricalFirmValuation["Close"])
plt.plot(HistoricalIndexFund["Close"])
plt.show()
