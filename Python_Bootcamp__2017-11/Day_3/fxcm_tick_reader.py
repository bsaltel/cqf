#
# A Class for the Retrieval of Historical Tick Data
# as Provided by FXCM Financial Capital Markets Limited
#
# The Python Quants GmbH
# October 2017
#
# Note that this code and the data service accessed
# by the code are for illustration purposes only.
# They come with no warranties or representations,
# to the extent permitted by applicable law.
#
#
# Read the RISK DISCLAIMER carefully.
#
# Status: Experimental
#
import gzip
import pandas as pd
import urllib.request
import datetime as dt
from io import BytesIO, StringIO


class fxcm_tick_reader(object):
    """ A class to retrieve historical tick data provided by FXCM. """

    symbols = ('AUDCAD', 'AUDCHF', 'AUDJPY', 'AUDNZD', 'CADCHF', 'EURAUD',
               'EURCHF', 'EURGBP', 'EURJPY', 'EURUSD', 'GBPCHF', 'GBPJPY',
               'GBPNZD', 'GBPUSD', 'GBPCHF', 'GBPJPY', 'GBPNZD', 'NZDCAD',
               'NZDCHF', 'NZDJPY', 'NZDUSD', 'USDCAD', 'USDCHF', 'USDJPY')

    def __init__(self, symbol, start, stop):
        """ Constructor of the class.

        Arguments:
        ==========
        symbol: string
            one of symbols

        start: datetime.date
            the first day to retrieve data for

        stop: datetime.date
            the last day to retrieve data for

        """

        if not (isinstance(start, dt.datetime) or isinstance(start, dt.date)):
            raise TypeError('start must be a datetime object')
        else:
            self.start = start

        if not (isinstance(stop, dt.datetime) or isinstance(stop, dt.date)):
            raise TypeError('stop must be a datetime object')
        else:
            self.stop = stop

        if self.start > self.stop:
            raise ValueError('Invalid date range')

        if symbol not in self.symbols:
            msg = 'Symbol %s is not supported. For a list of supported'
            msg += ' symbols, call get_available_symbols()'
            raise ValueError(msg % symbol)
        else:
            self.symbol = symbol

        self.data = None
        self.url = 'https://tickdata.fxcorporate.com/%s/%s/%s.csv.gz'
        self.__fetch_data__()

    def get_raw_data(self):
        """ Returns the raw data set as pandas DataFrame """
        return self.data

    def get_data(self, start=None, end=None):
        """ Returns the requested data set as pandas DataFrame;
        DataFrame index is converted to DatetimeIndex object """
        try:
            self.data_adj
        except:
            data = self.data.copy()
            index = pd.to_datetime(data.index.values,
                                   format='%m/%d/%Y %H:%M:%S.%f')
            data.index = index
            self.data_adj = data
        data = self.data_adj
        if start is not None:
            data = data[data.index >= start]
        if end is not None:
            data = data[data.index <= end]
        return data

    @classmethod
    def get_available_symbols(cls):
        """ Returns all available symbols """
        return cls.symbols

    def __fetch_data__(self):
        """ Retrieve the data for the given symbol and the given time window """
        self.data = pd.DataFrame()
        running_date = self.start
        seven_days = dt.timedelta(days=7)
        while running_date <= self.stop:
            year, week, noop = running_date.isocalendar()
            url = self.url % (self.symbol, year, week)
            data = self.__fetch_dataset__(url)
            if len(self.data) == 0:
                self.data = data
            else:
                self.data = pd.concat((self.data, data))
            running_date = running_date + seven_days

    def __fetch_dataset__(self, url):
        """ Retrieve data for the given symbol for one week """
        print('Fetching data from: %s' % url)
        requests = urllib.request.urlopen(url)
        buf = BytesIO(requests.read())
        f = gzip.GzipFile(fileobj=buf)
        data = f.read()
        data_str = data.decode('utf-16')
        data_pandas = pd.read_csv(StringIO(data_str), index_col=0)
        return data_pandas
