
# Computes the modified z score
def modified_zscore(obs):

    import numpy as np
    from maths import pow
    amax = np.amax(obs, axis=0)
    amin = np.amin(obs, axis=0)
    
    mean = np.mean(obs)
    median = np.median(obs)
    
    sumsqdiff = np.sum(pow((obs - median),2)) # sum of square difference
    sqrtdiff = np.sqrt(sumsqdiff)
    
    mad= np.median(sqrtdiff) # mean absolute deviation
    modzscore = (0.6745 * sumsqdiff) / mad
 
    return modzscore
 
# Visualize the variable for outliers    
def makeplot(series):
    
    import numpy as np
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 4))
    plt.title('Test for outlier', size=20)
    plt.scatter(x = series.index, y=series.values, alpha=.34)
    plt.axhline(y=modified_zscore(series), ls= ':', color='red', )   
    
    plt.show()
    
    
    
    
