#######################################
# Pull data for a specified ticker
#   Report financial outlook and current/historical performance of spcecific ticker symbol from public API financial data
#
# Options (parameters)
#       -x  x array bounds in space delimited format: min max
#
#######################################
###  CB: Init config variables
#######################################
config = {}
config["maxDays"] = 2000
config["shortWindow"] = 50
config["longWindow"] = 100


#######################################
###  CB: Init Modules & Init Var
#######################################
import datetime as dt
import sys
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

### try date variable init, exit on error
try:
	startDate = dt.datetime(pastDate[2], pastDate[1], pastDate[0])
	today = dt.date.today()
	endDate = dt.datetime( today.year, today.month, today.day )
	if (endDate-startDate).days > config["maxDays"]:
		startDate = endDate - dt.timedelta(days=config["maxDays"])
		print('\nMax historical data limit reached, max limit set to: ' + str(config["maxDays"]) + ' days\n')
	if (endDate < startDate):
		print('\nCritical error encountered during processing.\nDate parameter not in past.')
		sys.exit(1)
except:
    print('\nCritical error encountered during processing.\nPassed date parameter expects three integers for a past date, in format: \ndd mm yyyy\n')
    sys.exit(1) # on date error exit the whole script



#######################################
###  CB: import other modules
#######################################
import pandas_datareader as pdr
import pandas as pd
from matplotlib import cm
import matplotlib.pyplot as plt


#######################################
### CB: Pull Ticker data from public financial data API
#######################################
historical_MarketCap = pdr.get_data_yahoo(tickerSymbol, startDate, endDate).filter(['Close'],axis=1)
###     Pull index funds for reporting
# pull S&P500, create intiial pandas dataset
indexFund = pdr.get_data_yahoo("^GSPC", startDate, endDate).filter(['Close'],axis=1)
indexFund = indexFund.rename(index=str, columns={"Close":"sp500"})
#pull Nasdaq & DownJones Industrial
indexFund['nasdaq'] = pdr.get_data_yahoo("^IXIC", startDate, endDate)['Close']
indexFund['dowJonesInd']  = pdr.get_data_yahoo("^DJI", startDate, endDate)['Close']


#######################################
### CB: Data Analysis
#######################################
# Normailze hte index funds to the maximum value from reported firm's market capitalization
normalized_indexFund = ((indexFund-indexFund.min())/(indexFund.max()-indexFund.min())) * (historical_MarketCap['Close'].max())



#######################################
### CB: Report for Ticker
#######################################
plt.plot(historical_MarketCap)
plt.plot(historical_MarketCap.rolling(window=config["shortWindow"]).mean())
plt.plot(historical_MarketCap.rolling(window=config["longWindow"]).mean())
plt.plot(normalized_indexFund['sp500'])
plt.plot(normalized_indexFund['nasdaq'])
plt.plot(normalized_indexFund['dowJonesInd'])

plt.show()
