Machine Learning for Finance
============================

<img src="http://hilpisch.com/images/tpq_globe.png" width=300px>

A CQF elective with Dr. Yves J. Hilpisch, The Python Quants GmbH

General resources:

* http://tpq.io
* http://hilpisch.com

Wifi
----

You can use the following wifi in this venue:

    SSID Fitch Guest
    PW   Ft1ch#2016#!


Abstract
--------
This CQF elective is about machine learning and deep learning with Python applied to finance. It starts with techniques to retrieve financial data from open data sources and covers Python packages like NumPy, pandas, scikit-learn and TensorFlow. It provides the basis to further explore these recent developments in data science to improve traditional financial tasks such as the pricing of American options or the prediction of future stock market movements.

Among other, the elective covers:

* Getting and working with financial time series data in Python
* Using linear OLS regression to predict financial prices & returns
* Using scikit-learn for machine learning with Python
* Application to the pricing of American options by Monte Carlo simulation
* Applying logistic regression to classification problems
* Predicting stock market returns as a classification problem
* Using TensorFlow for deep learning with Python
* Using deep learning for predicting stock market returns 

Overview **slides** under http://hilpisch.com/cqf_ml_elective.pdf


Python
------

Download and install **Miniconda 3.6** from https://conda.io/miniconda.html

If you have either Miniconda or Anaconda installed there is not need to install anything new.

    conda create -n elective python=3.6
    (source) activate elective
    conda install numpy pandas=0.19 scikit-learn matplotlib
    conda install pandas-datareader pytables
    conda install ipython jupyter
    jupyter notebook

Installing `TensorFlow`: https://www.tensorflow.org/install/




Finance
-------

Download the paper by Longstaff and Schwartz (2001) about the Least-Squares Monte Carlo algorithm to price American options from [Paper about LSM algorithm](https://people.math.ethz.ch/~hjfurrer/teaching/LongstaffSchwartzAmericanOptionsLeastSquareMonteCarlo.pdf)


Basic Definitions
-----------------

> "You can think of **deep learning, machine learning and artificial intelligence** [AI] as a set of Russian dolls nested within each other, beginning with the smallest and working out. Deep learning is a subset of machine learning, which is a subset of AI. ... That is, all machine learning counts as AI, but not all AI counts as machine learning. For example, symbolic logic (rules engines, expert systems and knowledge graphs) as well as evolutionary algorithms and Baysian statistics could all be described as AI, and none of them are machine learning."

> "**Neural networks** are a set of algorithms, modeled loosely after the human brain, that are designed to recognize patterns. They interpret sensory data through a kind of machine perception, labeling or clustering raw input. The patterns they recognize are numerical, contained in vectors, into which all real-world data, be it images, sound, text or time series, must be translated."

> "**Deep learning** maps inputs to outputs. It finds correlations. It is known as a 'universal approximator', because it can learn to approximate the function f(x) = y between any input x and any output y, assuming they are related through correlation or causation at all. In the process of learning, a neural network finds the right f, or the correct manner of transforming x into y, whether that be f(x) = 3x + 12 or f(x) = 9x - 0.1."

> "All **classification tasks** depend upon labeled datasets; that is, humans must transfer their knowledge to the dataset in order for a neural to learn the correlation between labels and data. This is known as supervised learning. ... Any labels that humans can generate, any outcomes you care about and which correlate to data, can be used to train a neural network."

Source: [https://deeplearning4j.org](https://deeplearning4j.org/)


Machine Learning
----------------

Here some resources to get a first overview of basic **machine learning** concepts and **logistic regression** for classification:

* [Visual Guide to Basics of Neural Networks](http://jalammar.github.io/visual-interactive-guide-basics-neural-networks/)
* [Logistic Regression Basics & Algorithm](https://rasbt.github.io/mlxtend/user_guide/classifier/LogisticRegression/)
* [Generalized Linear Models in `scikit-learn`](http://scikit-learn.org/stable/modules/linear_model.html)


Neural Networks
---------------

Here some resources to get a first overview of **neural networks**:

* [A Neural Network in 11 Lines of Python](https://iamtrask.github.io/2015/07/12/basic-python-network/)
* [Introduction to Deep Neural Networks](https://deeplearning4j.org/neuralnet-overview)
* [A Guide to Deep Learning](http://yerevann.com/a-guide-to-deep-learning/)
* [Neural Networks and Deep Learning (free e-book)](http://neuralnetworksanddeeplearning.com/)

TensorFlow
----------

Some resources to get started with Google's `TensorFlow` package for deep learning:

* [Hello, TensorFlow!](https://www.oreilly.com/learning/hello-tensorflow)
* [TensorFlow Tutorials](https://www.tensorflow.org/tutorials/)


Data
----

Download a HDF5 database file, containing a single `pandas DataFrame` object with hitorical equites data, from http://hilpisch.com/equities.h5

<img src="http://hilpisch.com/tpq_logo.png" width=250px>