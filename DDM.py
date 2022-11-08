# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 13:51:55 2021

@author: zanna
"""
# Script that calculates price of a stock
# using the dividend discount model
# Lets create a function that calculates the price
import pandas as pd
import yfinance as yf
import numpy as np

# Lets tackle this in two steps
# Step 1: Create the code for a single stock
# Step 2: Modify the code and turn it into a function
rf = .015
rm = yf.Ticker('SPY').history('5y').Close
rm = rm.resample('1y').last().pct_change().mean()

tickers = ['WMT','GM','MCD','DLTR']

# This code only works for constant-growth stocks that pay a dividend
def calculate_price(tic):
	df = yf.Ticker(tic)
	fin = df.financials
	bs = df.balance_sheet
	D0 = df.dividends[-1] * 4
	ni = fin.loc['Net Income'][0]
	eqty = bs.loc['Total Stockholder Equity'][0]
	roe = ni / eqty
	retained = bs.loc['Retained Earnings'][0]
	rr = 1 - (D0 / ni / df.info['revenuePerShare'])
	g =  roe * rr
	beta = df.info['beta']
	r = rf + beta*(rm - rf)
	p0 = (D0 * (1+g)) / (r-g)
	return(p0)

# Loop through and calculate price of multiple tickers
for ticker in tickers:
	prc = calculate_price(ticker)
	print(ticker, "Price is:",prc)

calculate_price('WMT')
# 

P0 = d1/(1+g1)**1 + d2/(1+g2) **2 + (d3 / ((r-g3) ** 2))

