
# ADF test for statioanrity
def adf_report(data):
    """
    Displays the ADF test results with the hypothesis
    data: time series data with date as an index
    """
    from statsmodels.tsa.stattools import adfuller 
    adfullerreport = adfuller(data) 
    adfullerreportdata = pd.DataFrame(adfullerreport[0:4],columns = ["Values"], 
                                  index=["ADF F% statistics",
                                         "P-value",  
                                         "No. of lags used",
                                         "No. of observations"]
                                 )
    if adfullerreportdata.values[1] < 0.05:
        test= 'data is staionary'
    else:
        test= 'data is not stationary'

    return adfullerreportdata, test


# basic statistical plots

def stat_plot(data, plot='acf'):
    """
    Makes some basic statistical plots..
    data: ts_data with date as the index
    plot: 'acf' for acf plots, 
          'pacf' for pacf plot, 
          'decompose' for time series decomposition plot

    """

    from statsmodels.graphics.tsaplots import plot_acf, plot_pacf, plot_predict
    from statsmodels.tsa.api import seasonal_decompose

    if plot == 'acf':
        plot_acf(data);
    if plot == 'pacf':
        plot_pacf(data);
    if plot == 'decompose':
        d = seasonal_decompose(data)
        d.plot();
    else:
        pass


def opti_sarimax(data):
    """
    It outputs the optimised parameters for SARIMAX model
    data: times series data with date index
    """

    import itertools 
    p = d = q = range(0, 2) 
    pdq = list(itertools.product(p, d, q)) 
    seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product (p, d, q))] 
    
    for param in pdq:    
        for param in pdq:        
            for param_seasonal in seasonal_pdq:            
                try:                
                    mod = sm.tsa.statespace.SARIMAX(data, 
                                                    order=param,   
                                                    seasonal_order=param_seasonal, 
                                                    enforce_stationarity=False, 
                                                    enforce_invertibility=False)
                    results = mod.fit() 
                    print('SARIMAX{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
                except:                
                    continue


