######################################################################
# 2015. Richard Diamond. Quieries to r.diamond@cqf.com               #
# Models are specified and validated but any use is at your own risk #
######################################################################

# ECM IMPLEMENTATION (two variables, Engle-Granger method)

# ADF TEST ON SERIES
# "drift" -- refers Delta Y= constant,  "trend" refers to Delta Y = beta*t -- increases critical values but overfits time dependence

adf.test = ur.df(curve2.this$X10, type = "drift")
print(summary(adf.test))

adf.test = ur.df(curve2.this$X25, type = "drift")
print(summary(adf.test))

# NAIVE COINTEGRATING EQUATION

coint.reg = lm(curve2.this$X10 ~ curve2.this$X25)
print(summary(coint.reg))

# CADF TEST ON RESIDUAL

cadf.test = ur.df(residuals(coint.reg), type = "none") # CADF because ADF test applies to cointegrated residual
print(summary(cadf.test))

# ECM PARAMETERS ESTIMATION (one-way)

tenorY.diff = diff(curve2.this$X10) #tenorY.diff = tenorY.diff - mean(tenorY.diff) # however, mean is very small
tenorX.diff = diff(curve2.this$X25)

eq_corr.lag = lag(residuals(coint.reg), k = -1)
ecm.reg = lm(tenorY.diff ~ tenorX.diff + eq_corr.lag + 0)
print(summary(ecm.reg))

#ECM with Delta Y_t-1 # // but that variable comes as not significant by t statistic
#ecm.reg = lm(tenorY.diff[ time(tenorY.diff) != as.Date("2013-05-31")] ~ lag(tenorY.diff, k = -1) + tenorX.diff[ time(tenorX.diff) != as.Date("2013-05-31")] + eq_corr.lag[ time(eq_corr.lag) != as.Date("2013-05-31")] + 0)
#print(summary(ecm.reg))


# to check the relationship 'the other way', r_25Y on r_10Y -- we recompute the residual eq-correction term
# that will save time on deciding which way is 'better' and which variable is leading (we do two things in one)
cointO.reg = lm(curve2.this$X25 ~ curve2.this$X10)
eq_corrO.lag = lag(residuals(cointO.reg), k = -1) #omit the step of testing residual with CADF but test result given on Case - Extra Slides
ecmO.reg = lm(tenorX.diff ~ tenorY.diff + eq_corrO.lag + 0)
print(summary(ecmO.reg))

# LINEAR REGRESSION ON DIFFERENCES (for comparison) // linear regression in differences gives the minimum variance hedge

simple.reg = lm(diff(curve2.this$X10) ~ diff(curve2.this$X25) + 0) # + 0 means no cash holdings
print(summary(simple.reg))
