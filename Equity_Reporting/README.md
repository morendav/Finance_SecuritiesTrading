# Security Reporting

Scripts used to call upon publicly available financial data through a python pandas API and report relevant information about the security (securities) and their relationship to other index funds.

## Prerequisites

A number of python libraries are used in these scripts at different points. Please refer to the .py file for specific modules required by each script.
These are mostly from SciPy and commonly available in standard IDEs used in python development

In no specific order:
  + matplotlib
  + numpy
  + argparse
  + datetime

### Running the script

The script requires at least one pass parameter, a text string representing the ticker for the firm or fund to report on.
The script will default a past date of Jan 01, 2018. Otherwise a past date may be passed in the -d parameter in the format dd mm yyyy

Example Run:
```
python3 tickerData.py -d 20 01 2015 -t "AAPL"
```

In this example we are gather metrics for:
- Ticker        Apple Inc, a technology company HQ in Cupertino, California
- From Date     20 Jan, 2015

## Acknowledgments

* Awesome tutorials are all over the internet for gather financial data using Pands pd and publicly available financial data APIs
* Yahoo Finance API



## Version

### V 1.01
  + working model, simply plots data from past date
