
# test for outliers
def modified_zscore(obs):
    
    """
    Computes the threshold to detect extreme values in a distribution
    
    modified_zscore = zscore/MAD
    MAD is the mean absolute devaition
    """
    amax = np.amax(data, axis=0)
    amin = np.amin(data, axis=0)
    
    mean = np.mean(data)
    median = np.median(data)
    
    sumsqdiff = np.sum(pow((data - median),2))
    sqrtdiff = np.sqrt(sumsqdiff)
    
    mad= np.median(sqrtdiff) # mean absolute deviation
    modzscore = (0.6745 * sumsqdiff) / mad
 
    return result
    
def makeplot(series):
    
    """
    create visualization of the outliers detected.
    """
    
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 4))
    plt.title('--test for outlier--')
    plt.scatter(x = series.index, y=series.values, alpha=.34)
    plt.axhline(y=modified_zscore(series), ls= ':', color='red', label='threshold')   
    plt.legend()
    plt.show()
    
    
    
    
