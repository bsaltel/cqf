#
# Python Class for Technical Analysis
# eg Based on Data from FXCM Financial Capital Markets Limited
#
# The Python Quants GmbH
# October 2017
#
# Note that this code and the data (service) accessed
# by the code are for illustration purposes only.
# They come with no warranties or representations,
# to the extent permitted by applicable law.
#
# Read the RISK DISCLAIMER carefully.
#
# Status: Experimental
#
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None

class technical_indicators(object):
    """ A class to generate technical, financial indicators 
    based on pandas DataFrame objects """
    def __init__(self, data, index=''):
        if not isinstance(data, pd.DataFrame):
            raise TypeError('data must be a pandas DataFrame')
        self.data = data
        if index != "" and index in self.data.columns:
            self.data.set_index(index, inplace=True)

    def add_columns(self, data, name):
        """ Add columns to the data object """
        self.data[name] = data

    def remove_columns(self, name):
        """ Remove the column with name 'name' """
        self.data = self.data.drop([name], axis=1)

    def get_data(self):
        """ Return the data as pandas DataFrame object """
        return self.data
    
    def check_periods(self, periods):
        try:
            periods = int(periods)
        except:
            raise TypeError('periods must be an integer')
        if periods < 1:
            raise TypeError('periods must be a positive integer')
        return periods

    def sma(self, column_name, periods):
        """ Return the simple moving average (SMA) of the data

        Arguments:
        ==========
        column_name: string
            the name of the data set's column to use

        periods: integer
            the length of the time window

        Returns:
        ======== 
        sma: ndarray
            the simple moving average data set
        """
        periods = self.check_periods(periods)
        sma = self.data[column_name].rolling(periods).mean()
        return sma

    def add_sma(self, column_name, periods):
        """ Add simple moving average (SMA) of the data

        Arguments:
        ==========
        column_name: string
            the name of the data set's column to use

        periods: integer
            the length of the time window

        Returns:
        ========
        name: string
            the name of the added SMA column
        """
        periods = self.check_periods(periods)
        name = 'sma_%s_%s' % (periods, column_name)
        data = self.sma(column_name, periods)
        self.add_columns(data, name)
        return name

    def ewma(self, column_name, periods):
        """ Return the exponential weighted moving average (EWMA) of the data

        Arguments:
        ==========
        column_name: string,
            the name of the data set's column to use

        periods: integer, 
            the length of the time window

        Returns:
        ======== 
        ewma: ndarray
            the exponentially weighted moving average (EWMA) data set
        """
        periods = self.check_periods(periods)
        ewma = self.data[column_name].ewm(span=periods,
                              min_periods=periods).mean()
        return ewma

    def add_ewma(self, column_name, periods):
        """ Add the exponential weighted moving average (EWMA) of the data

        Arguments:
        ==========
        column_name: string
            the name of the data set's column to use

        periods: integer
            the length of the time window

        Returns:
        ======== 
        name: string
            name of the added EWMA column
        """
        periods = self.check_periods(periods)
        name = 'ewma_%s_%s' % (periods, column_name)
        data = self.ewma(column_name, periods)
        self.add_columns(data, name)
        return name

    def bollinger_upper(self, column_name, periods):
        """ Return upper Bollinger band of the data

        Arguments:
        ==========
        column_name: string
            the name of the data set's column to use

        periods: integer
            the length of the time window

        Returns:
        ========
        upper_bol: ndarray
            the upper Bollinger band data
        """
        periods = self.check_periods(periods)
        stdev = self.data[column_name].rolling(periods).std()
        upper_bol = self.sma(column_name, periods) + (2 * stdev)
        return upper_bol

    def add_bollinger_upper(self,  column_name, periods):
        """ Add upper Bollinger band to the data

        Arguments:
        ==========

        column_name: string,
            the name of the dateset's column to use.

        periods: integer, 
            the length of the time window.

        Returns:
        ======== 
        name: string
            the name of the added column
        """
        periods = self.check_periods(periods)
        name = 'boll_up_%s_%s' % (periods, column_name)
        data = self.bollinger_upper(column_name, periods)
        self.add_columns(data, name)
        return name

    def bollinger_lower(self, column_name, periods):
        """ Return upper Bollinger band of the data

        Arguments:
        ==========

        column_name: string,
            the name of the dateset's column to use.

        periods: integer, 
            the length of the time window.

        Returns:
        ========
        lower_bol: ndarray
            the lower Bollinger band data
        """
        periods = self.check_periods(periods)
        stdev = self.data[column_name].rolling(periods).std()
        lower_bol = self.sma(column_name, periods) - (2 * stdev)
        return lower_bol

    def add_bollinger_lower(self,  column_name, periods):
        """ Add lower Bollinger band to the data

        Arguments:
        ==========

        column_name: string,
            the name of the dateset's column to use.

        periods: integer, 
            the length of the time window.

        Returns:
        ======== 
        name: string
            the name of the added column
        """
        periods = self.check_periods(periods)
        name = 'boll_low_%s_%s' % (periods, column_name)
        data = self.bollinger_lower(column_name, periods)
        self.add_columns(data, name)
        return name

    def rsi(self, column_name, periods):
        """ Return the relative strength index (RSI) of the data

        Arguments:
        ==========

        column_name: string,
            the name of the dateset's column to use.

        periods: integer,
            the lenght of the time window.

        Returns:
        ========
        rsi: ndarray
            relative strength index (RSI) data
        """
        periods = self.check_periods(periods)
       
        data = self.data[column_name]
        delta = data.diff()
        delta = delta[1:] 

        up, down = delta.copy(), delta.copy()
        up[up < 0] = 0
        down[down > 0] = 0
        down = down.abs()

        sma_up =  up.rolling(periods).mean()
        sma_down = down.rolling(periods).mean()

        rs = sma_up / sma_down
        rsi = 100.0 - (100.0 / (1.0 + rs))
        
        return rsi

    def add_rsi(self, column_name, periods):
        """ Add the relative streng index (RSI) of the data

        Arguments:
        ==========

        column_name: string
            the name of the data set's column to use

        periods: integer
            the length of the time window

        Returns:
        ======== 
        name: string
            the name of the added column
        """

        try:
            periods = int(periods)
        except:
            raise TypeError('periods must be an integer')
        if periods < 1:
            raise TypeError('periods must be positive')

        name = 'rsi_%s_%s' % (periods, column_name)
        data = self.rsi(column_name, periods)
        self.add_columns(data, name)

        return name

    def macd(self, column_name, periods_fast, periods_slow):
        """ Return the moving average convergence/divergence (MACD) of the data

        Arguments:
        ==========
        column_name: string
            the name of the data set's column to use

        periods_fast: integer,
            the length of the shorter ewma time window

        periods_slow: integer 
            the length of the longer ewma time window

        Returns:
        ======== 
        macd: ndarray
            the moving average convergence/divergence (MACD) data
        """
        periods_fast = self.check_periods(periods_fast)
        periods_slow = self.check_periods(periods_slow)

        if periods_slow < periods_fast:
            raise ValueError('periods_fast must be smaller/shorter than periods_slow') 

        ewma_fast = self.ewma(column_name, periods_fast)
        ewma_slow = self.ewma(column_name, periods_slow)
        macd = ewma_fast - ewma_slow
        return macd

    def add_macd(self, column_name, periods_fast, periods_slow):
        """ Add moving average convergence/divergence (MACD) to the data

        Arguments:
        ==========
        column_name: string
            the name of the data set's column to use

        periods_fast: integer, 
            the length of the shorter ewma time window

        periods_slow: integer, 
            the length of the longer ewma time window

        Returns:
        ======== 
        name: string
            the name of the added column
        """
        periods_fast = self.check_periods(periods_fast)
        periods_slow = self.check_periods(periods_slow)

        if periods_slow < periods_fast:
            raise ValueError('periods_fast must be smaller/shorter than periods_slow') 

        name = 'macd_%sx%s_%s' % (periods_fast, periods_slow, column_name)
        data = self.macd(column_name, periods_fast, periods_slow)
        self.add_columns(data, name)
        return name

    def macd_signal(self, column_name, periods_fast, periods_slow, 
                     periods_signal):
        """ Return the signal generated by the MACD of the data

        Arguments:
        ==========
        column_name: string
            the name of the dat aset's column to use

        periods_fast: integer
            the length of the shorter ewma time window

        periods_slow: integer 
            the length of the longer ewma time window

        periods_signal: integer 
            the length of the time window used for signal generation

        Returns:
        ======== 
        macd_signal: ndarray
            the moving average convergence/divergence (MACD) signal data
        """
        periods_fast = self.check_periods(periods_fast)
        periods_slow = self.check_periods(periods_slow)
        periods_signal = self.check_periods(periods_signal)

        if periods_slow < periods_fast:
            raise ValueError('periods_fast must be smaller/shorter than periods_slow') 

        macd = self.macd(column_name, periods_fast, periods_slow)
        macd_signal = macd.ewm(span=periods_signal, min_periods=periods_signal).mean()
        return macd_signal

    def add_macd_signal(self, column_name, periods_fast, periods_slow,
                        periods_signal):
        """ Add the signal gernerated by the macd of the data

        Arguments:
        ==========
        column_name: string
            the name of the data set's column to use

        periods_fast: integer
            the length of the shorter ewma time window

        periods_slow: integer 
            the length of the longer ewma time window

        periods_signal: interger
            the length of the time window used for signal generation

        Returns:
        ======== 
        name: string
            the name of the added column
        """
        periods_fast = self.check_periods(periods_fast)
        periods_slow = self.check_periods(periods_slow)
        periods_signal = self.check_periods(periods_signal)

        if periods_slow < periods_fast:
            raise ValueError('periods_fast must be smaller/shorter than periods_slow') 

        name = 'macd_signal_%sx%sx%s_%s' % (periods_fast, periods_slow,
                                            period_signal, column_name)
        data = self.macd_signal(column_name, periods_fast, periods_slow,
                                period_signal)
        self.add_columns(data, name)
        return name
