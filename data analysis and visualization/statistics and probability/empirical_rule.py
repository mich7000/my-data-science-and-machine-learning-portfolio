
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# empirical rule plot
ages= pd.Series(np.random.normal(loc=34, scale=12,size=1200 ))

plt.figure(figsize=(12, 5))
plt.hist(ages, bins=50,color='black', alpha=.47)
plt.axvline(x=(np.mean(ages)+np.std(ages)), color='red')
plt.axvline(x=(np.mean(ages)-np.std(ages)), color='red', label='68%')

plt.axvline(x=(np.mean(ages)+2*np.std(ages)), color='blue',ls= ':', label='95%')
plt.axvline(x=(np.mean(ages)-2*np.std(ages)), color='blue',ls= ':')

plt.axvline(x=(np.mean(ages)+3*np.std(ages)), color='purple', ls= '-')
plt.axvline(x=(np.mean(ages)-3*np.std(ages)), color='purple', ls= '-', label='99.5%')
plt.legend()
plt.title('The Empirical Rule')
plt.savefig('inference.png')

# empirical rule values
print('\n')
print("68% of the individual have ages between ", np.floor(np.mean(ages)-np.std(ages)), " and ", np.floor(np.mean(ages)+np.std(ages)))
print("95% of the individual have ages between ", np.floor(np.mean(ages)-2*np.std(ages)), " and ", np.floor(np.mean(ages)+2*np.std(ages)))
print("99% of the individual have ages between ", np.ceil(np.mean(ages)-3*np.std(ages)), " and ", np.floor(np.mean(ages)+3*np.std(ages)))
