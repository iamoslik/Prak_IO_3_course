import numpy as np
import statsmodels.api as sm

def DFtest(v):
    test = sm.tsa.adfuller(v)
    print ('adf: ', test[0])
    print ('p-value: ', test[1])
    print ('Critical values: ', test[4])
    if test[0]> test[4]['5%']:
        return False
    else:
        return True


def Integration_order(v):
    order = 0
    test = v
    while (not DFtest(test)):
        test = test.diff().dropna()
        order += 1
    return order, test
