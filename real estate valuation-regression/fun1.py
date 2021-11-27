
# test for outliers


def modified_zscore(obs):
    """
    Computes the threshold to detect extreme values in a distribution
    
    modified_zscore = zscore/MAD
    MAD is the mean absolute devaition
    """
    import numpy as np
    amax = np.amax(obs, axis=0)
    amin = np.amin(obs, axis=0)
    
    mean = np.mean(obs)
    median = np.median(obs)
    
    sumsqdiff = np.sum(pow((obs - median),2))
    sqrtdiff = np.sqrt(sumsqdiff)
    
    mad= np.median(sqrtdiff)
    modzscore = (0.6745 * sumsqdiff) / mad
 
    return modzscore
    
def makeplot(series):
    
    """
    create visualization of the outliers detected.
    """
    import numpy as np
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 4))
    plt.title('Test for outlier', size=20)
    plt.scatter(x = series.index, y=series.values, alpha=.34)
    plt.axhline(y=modified_zscore(series), ls= ':', color='red', )   
    
    plt.show()
    
    
    
    
