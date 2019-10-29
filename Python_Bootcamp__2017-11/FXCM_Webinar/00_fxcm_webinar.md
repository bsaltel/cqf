FXCM Webinar Series
===================

**on Algorithmic Trading**

**_Python & Historical Tick Data_**

Dr. Yves J. Hilpisch | The Python Quants GmbH

Online, 24. October 2017

(short link to this Gist: https://goo.gl/C1WD8r)

<img src="http://hilpisch.com/images/finaince_visual_low.png" width=300px>


Resources
---------

* http://tpq.io
* http://hilpisch.com
* http://twitter.com/dyjh
* http://pyalgo.tpq.io
* http://certificate.tpq.io

Risk Disclaimer
---------------

Trading forex/CFDs on margin carries a high level of risk and may not be suitable for all investors as you could sustain losses in excess of deposits. Leverage can work against you. Due to the certain restrictions imposed by the local law and regulation, German resident retail client(s) could sustain a total loss of deposited funds but are not subject to subsequent payment obligations beyond the deposited funds. Be aware and fully understand all risks associated with the market and trading. Prior to trading any products, carefully consider your financial situation and experience level. Any opinions, news, research, analyses, prices, or other information is provided as general market commentary, and does not constitute investment advice. FXCM will not accept liability for any loss or damage, including without limitation to, any loss of profit, which may arise directly or indirectly from use of or reliance on such information.

Slides
------

You find the slides under http://hilpisch.com/fxcm_webinar_tick_data.pdf

Agenda
------

<img src="http://hilpisch.com/images/finaince_logo.png" width=300px>

The webinar covers the following topics:

**Introduction**

* The Python Quants Group
* Driving Forces in Algorithmic Trading
* Why Python for Algorithmic Trading?

**Live Demo**

* Using Python & pandas for Backtesting
* Working with FXCM Historical Tick Data
* Adding Indicators to Data Sets
* Visualization of OHLC Data & Studies

Data
----

You find the historical EOD data set used under http://hilpisch.com/eurusd.csv (as provided by FXCM Forex Capital Markets Ltd.).

You find further information about the historical tick data source under https://github.com/FXCMAPI/FXCMTickData (as provided by FXCM Forex Capital Markets Ltd.).

Python
------

If you have either Miniconda or Anaconda already installed, there is no need to install anything new.

The code that follows uses Python 3.6. For example, download and install **Miniconda 3.6** from https://conda.io/miniconda.html if you do not have `conda` already installed.

In any case, for **Linux/Mac** you should execute the following lines on the shell  to create a new environment with the needed packages:

    conda create -n fxcm python=3.6
    source activate fxcm
    conda install numpy pandas matplotlib statsmodels
    pip install plotly cufflinks
    conda install ipython jupyter
    jupyter notebook

On **Windows**, execute the following lines on the command prompt:
    
    conda create -n fxcm python=3.6
    activate fxcm
    conda install numpy pandas matplotlib statsmodels
    pip install plotly cufflinks
    pip install win-unicode-console
    set PYTHONIOENCODING=UTF-8
    conda install ipython jupyter
    jupyter notebook

Read more about the management of environments under https://conda.io/docs/using/envs.html

Books
-----

The following book is recommended for Python data analysis: [Python Data Science Handbook, O'Reilly](http://shop.oreilly.com/product/0636920034919.do)

<img src="http://hilpisch.com/images/fxcm_logo_bg.png" width=250px>
<img src="http://hilpisch.com/tpq_logo.png" width=250px>