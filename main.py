
#import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
# import scipy
import scipy as scipy
# import seaborn
import seaborn as sns
# settings for seaborn plotting style
sns.set(color_codes=True)
# settings for seaborn plot sizes
sns.set(rc={'figure.figsize':(5,5)})


#Import the librairy
from stat_distribution_hd.distributions import distributions

#Triangular distribution
#Inputs
        #a = float(input("Enter your starting value: "))
        #c = float(input("Enter the mean value between 0 and 1: "))
        #b = float(input("Enter your highest value: "))
        #n = int(input("Enter your integer sample size: "))
distributions.triangular(1,0.5,10,100)