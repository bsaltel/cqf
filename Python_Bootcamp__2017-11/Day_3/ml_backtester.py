#
# Class for the backtesting of ML-based trading strategies
#
# FPQ Bootcamp
#
import numpy as np
import pandas as pd
from pylab import plt
from sklearn.svm import SVC
from sklearn import linear_model
from sklearn.naive_bayes import GaussianNB


class ScikitBacktester(object):
    def __init__(self):
        self.data_url = 'http://hilpisch.com/tr_eikon_eod_data.csv'
        self.get_raw_data()

    def get_raw_data(self):
        self.raw_data = pd.read_csv(self.data_url,
                                    index_col=0,
                                    parse_dates=True)

    def get_algorithm(self, model):
        self.model = model
        if self.model == 'LinearRegression':
            self.algorithm = linear_model.LinearRegression()
        elif self.model == 'NaiveBayes':
            self.algorithm = GaussianNB()
        elif self.model == 'LogisticRegression':
            self.algorithm = linear_model.LogisticRegression()
        elif self.model == 'SVC':
            self.algorithm = SVC()
        else:
            return 'Model not known.'

    def prepare_data(self, symbol, start, end, lags):
        data = pd.DataFrame(self.raw_data[symbol])
        data['Returns'] = np.log(data / data.shift(1))
        self.cols = []
        for lag in range(1, lags + 1):
            col = 'lag_%d' % lag
            data[col] = np.where(data['Returns'].shift(lag) > 0, 1, 0)
            self.cols.append(col)
        self.data = data.loc[start:end]

    def run_strategy(self, symbol, start, end, model, lags):
        self.symbol = symbol
        self.get_algorithm(model)
        self.prepare_data(symbol, start, end, lags)
        self.algorithm.fit(self.data[self.cols], np.sign(self.data['Returns']))
        self.data['Prediction'] = self.algorithm.predict(self.data[self.cols])
        self.data['Strategy'] = self.data['Prediction'] * self.data['Returns']
        return self.data[['Returns', 'Strategy']].cumsum(
                                    ).apply(np.exp).iloc[-1]

    def plot_results(self):
        try:
            self.data[['Returns', 'Strategy']].cumsum(
                                    ).apply(np.exp).plot(figsize=(10, 6),
                                    title=self.symbol)
        except:
            return 'No backtesting results available yet.'







