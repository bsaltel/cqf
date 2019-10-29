ODSC Europe 2017 (London)
=========================

**Algorithmic Trading**

**_With Machine & Deep Learning_**

Workshop by Dr. Yves J. Hilpisch | The Python Quants GmbH

London, 12. October 2017

(short link to this Gist: https://goo.gl/LAQ8Ze)

<img src="http://hilpisch.com/images/finaince_visual_low.png" width=300px>


Resources
---------

* http://tpq.io
* http://hilpisch.com
* http://twitter.com/dyjh
* http://pyalgo.tpq.io
* http://certificate.tpq.io

Quote
-----

"Pichai said that as an 'AI first' company, this is a 'unique moment in time' for Google to combine hardware, software and artificial intelligence. 'It's radically rethinking how computing should work', he said."

_Business Standard, "Google Ramps up Hardware Business", 06. October 2017._

Slides
------

You find the slides under http://hilpisch.com/odsc_workshop.pdf


Python
------

If you have either Miniconda or Anaconda already installed, there is no need to install anything new.

We are using Python 3.6. Download and install **Miniconda 3.6** from https://conda.io/miniconda.html if you do not have `conda` already installed.

In any case, you should execute the following lines on the shell/command prompt to create a new environment with the needed packages:

    conda create -n odsc python=3.6
    (source) activate odsc
    conda install numpy pandas=0.19 scikit-learn matplotlib
    conda install ipython jupyter
    conda install tensorflow
    jupyter notebook

Read more about the management of environments under https://conda.io/docs/using/envs.html

Agenda
------

<img src="http://hilpisch.com/images/finaince_logo.png" width=300px>

We are going to cover the following topics:

* Reading Financial Time Series Data with pandas
* Formulating an Algorithmic Trading Strategy
* Vectorized Backtesting of the Trading Strategy
* Random Walk Hypothesis
* Prediction based on Logistic Regression
* Neural Networks from Scratch
* Prediction based on DNN Classifier

Data
----

You find the data set used under http://hilpisch.com/eurusd.csv (as provided by FXCM Forex Capital Markets Ltd.).

Cloud
-----
Use this link to get a 10 USD starting credit on **[DigitalOcean](https://m.do.co/c/fbe512dd3dac)** when signing up for a new account.

Books
-----

Good book about everything important in Python data analysis: [Python Data Science Handbook, O'Reilly](http://shop.oreilly.com/product/0636920034919.do)

Good book covering object-oriented programming in Python: [Fluent Python, O'Reilly](http://shop.oreilly.com/product/0636920032519.do)


<img src="http://hilpisch.com/tpq_logo.png" width=250px>