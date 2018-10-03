#######################################
# Pull data for a specified ticker
#   Report financial outlook and current/historical performance of spcecific ticker symbol from public API financial data
#
# Options (parameters)
#       -x  x array bounds in space delimited format: min max
#
#######################################
###  CB: Modules &  Init Var
#######################################
import pandas_datareader as pdr
import pandas as pd
import datetime as dt
import sys
from datetime import date
from argparse import ArgumentParser
from matplotlib import cm
import matplotlib.pyplot as plt


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

try:
    startDate = dt.datetime(pastDate[2], pastDate[1], pastDate[0])
    today = date.today()
    endDate = dt.datetime( today.year, today.month, today.day )
    endDate > startDate
except:
    print('\nCritical error encountered during processing.\nPassed date parameter expects three integers for a past date, in format: \ndd mm yyyy')
    sys.exit(1) # on date error exit the whole script

#######################################
### CB: Pull Ticker data from public financial data API
#######################################
HistoricalFirmValuation = pdr.get_data_yahoo(tickerSymbol, startDate, endDate)
# SP500 Index, Market Portfolio proxy
HistoricalIndexFund = pdr.get_data_yahoo("SPY", startDate, endDate)


#######################################
### CB: Report for Ticker
#######################################
plt.plot(HistoricalFirmValuation[Close])
