#
# Mean-Variance Portfolio Class
#
import numpy as np
import pandas as pd
from pylab import plt

class mean_variance_portfolio(object):
    def __init__(self, symbols, weigths=None):
        self.symbols = symbols
        if weigths is None:
            weights = len(symbols) * [1 / len(symbols)]
        self.weights = weights
        self.get_data()

    def get_data(self):
        self.raw = pd.read_csv('http://hilpisch.com/tr_eikon_eod_data.csv',
                               index_col=0, parse_dates=True)
        self.data = self.raw[self.symbols]
        self.rets = np.log(self.data / self.data.shift(1)).dropna()

    def calculate_port_return(self, weights=None):
        if weights is not None:
            self.weights = weights
        return np.dot(self.rets.mean() * 252, self.weights)

    def calculate_port_volatility(self, weights=None):
        if weights is not None:
            self.weights = weights
        return np.dot(self.weights, np.dot(self.rets.cov() * 252,
                                           self.weights)) ** 0.5

    def simulate_portfolios(self, number=250):
        pc = np.random.random((number, len(self.symbols)))
        pc = (pc.T / pc.sum(axis=1)).T
        vm = [(self.calculate_port_volatility(w),
               self.calculate_port_return(w)) for w in pc]
        self.results = np.array(vm)

    def plot_results(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.results[:, 0], self.results[:, 1], 'ro')
        plt.xlabel('volatility')
        plt.ylabel('expected return')
        plt.title(' | '.join(self.symbols))

if __name__ is '__main__':
    port = mean_variance_portfolio(['AAPL.O', 'MSFT.O'])
    port.simulate_portfolios()
    port.plot_results()


