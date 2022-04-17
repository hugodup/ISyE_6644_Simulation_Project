# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 10:04:18 2022

@author: Group 208 - Hugo Dupouy (GT903738077)
"""

# Librairies to import

# for inline plots in jupyter
#%matplotlib inline
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


##############################################################################

# INPUTS from USER

# random numbers
n = 100
start = 10
width = 20
p=0.6
a=2
b=3
c=0.158
mu=3

p = float(input("Enter your probability (between 0 and 1): "))
n = int(input("Enter your integer sample size: "))
start = float(input("Enter your starting value: "))
width = float(input("Enter the width of the data: "))
a = float(input("Enter beginning interval a: "))
b = float(input("Enter beginning interval b: "))
c = float(input("Enter the c-value: "))
mu = float(input("Enter the mu-value: "))

##############################################################################

# Discrete

## Bernoulli
def bernoulli():
    p = float(input("Enter your probability (between 0 and 1): "))
    n = int(input("Enter your sample size: "))
    
    from scipy.stats import bernoulli
    data_bern = bernoulli.rvs(p=p, size=n)
    
    graph= sns.displot(data_bern,
                     kde=False,
                     color="purple")
    graph.set(xlabel='Bernoulli Distribution', ylabel='Frequency')
    plt.show()

    mean, var, skew, kurt = bernoulli.stats(p, moments='mvsk')
    print("Bernoulli distribution: mean=",mean," and the var=",var)
bernoulli()


## Binomial
def binomial():
    p = float(input("Enter your probability (between 0 and 1): "))
    n = int(input("Enter your sample size: "))
    
    from scipy.stats import binom
    data_binom = binom.rvs(n=n, p=p, size=n)
    
    graph = sns.displot(data_binom,
                      kde=False,
                      color='purple')
    graph.set(xlabel='Binomial Distribution', ylabel='Frequency')
    plt.show()

    mean, var, skew, kurt = binom.stats(n, p, moments='mvsk')
    print("Binomial distribution: mean=",mean," and the var=",var)



## Geometric
def geometric():
    p = float(input("Enter your probability (between 0 and 1): "))
    n = int(input("Enter your sample size: "))
    
    from scipy.stats import geom
    data_geom = geom.rvs(p, size=n)
    
    graph = sns.displot(data_geom,
                      kde=False,
                      color='purple')
    graph.set(xlabel='Geometric', ylabel='Frequency')
    plt.show()

    mean, var, skew, kurt = geom.stats(p, moments='mvsk')
    print("Geometric distribution: mean=",mean," and the var=",var)



## Negative Binomial
def negative_binomial():
    p = float(input("Enter your probability (between 0 and 1): "))
    n = int(input("Enter your sample size: "))
        
    from scipy.stats import nbinom
    data_nbinom = nbinom.rvs(n=n, p=p, size=n)
    
    graph = sns.displot(data_nbinom,
                      kde=False,
                      color='purple')
    graph.set(xlabel='Negative Binomial', ylabel='Frequency')
    plt.show()

    mean, var, skew, kurt = nbinom.stats(n, p, moments='mvsk')
    print("Negative Binomial distribution: mean=",mean," and the var=",var)



## Poisson
def poisson():
    mu = float(input("Enter the mu-value: "))
    n = int(input("Enter your sample size: "))
    
    from scipy.stats import poisson
    data_poisson = poisson.rvs(mu=mu, size=n)
    
    graph = sns.displot(data_poisson,
                      bins='auto',
                      kde=False,
                      color='purple')
    graph.set(xlabel='Poisson Distribution', ylabel='Frequency')
    plt.show()

    mean, var, skew, kurt = poisson.stats(mu, moments='mvsk')
    print("Poisson distribution: mean=",mean," and the var=",var)



##############################################################################



# Continuous

## Uniform
def uniform():
    start = float(input("Enter your starting value a: "))
    width = float(input("Enter the width of the data b: "))
    n = int(input("Enter your integer sample size in the interval (a,b): "))

    from scipy.stats import uniform
    data_uniform = uniform.rvs(loc=start, scale=width, size=n)
    
    graph = sns.displot(data_uniform,
                      bins='auto',
                      kde=True,
                      color='purple')
    graph.set(xlabel='Uniform Distribution ', ylabel='Frequency')
    plt.show()

    mean, var, skew, kurt = uniform.stats(moments='mvsk')
    print("Uniform distribution: mean=",mean," and the var=",var)




## Exponential
def exponential():
    start = float(input("Enter your starting value a: "))
    width = float(input("Enter the width of the data b: "))
    n = int(input("Enter your integer sample size in the interval (a,b): "))
    
    from scipy.stats import expon
    data_expon = expon.rvs(loc=start, scale=width, size=n)
    
    graph = sns.displot(data_expon,
                      kde=True,
                      bins='auto',
                      color='purple')
    graph.set(xlabel='Exponential Distribution', ylabel='Frequency')
    plt.show()

    mean, var, skew, kurt = expon.stats(moments='mvsk')
    print("Exponential distribution: mean=",mean," and the var=",var)




## Erlang
def erlang():
    a = float(input("Enter your lambda value: "))
    n = int(input("Enter your integer sample size: "))
    
    from scipy.stats import erlang
    data_erlang = erlang.rvs(a=a, size=n)
    
    graph = sns.displot(data_erlang,
                      kde=True,
                      bins='auto',
                      color='purple')
    graph.set(xlabel='Erlang Distribution', ylabel='Frequency')
    plt.show()

    mean, var, skew, kurt = erlang.stats(a, moments='mvsk')
    print("Erlang distribution: mean=",mean," and the var=",var)



## Gamma
def Gamma():
    a = float(input("Enter your lambda value: "))
    n = int(input("Enter your integer sample size: "))
    
    from scipy.stats import gamma
    data_gamma = gamma.rvs(a, size=n)
    
    graph = sns.displot(data_gamma,
                      kde=True,
                      bins='auto',
                      color='purple')
    graph.set(xlabel='Gamma Distribution', ylabel='Frequency')
    plt.show()

    mean, var, skew, kurt = gamma.stats(a, moments='mvsk')
    print("Gamma distribution: mean=",mean," and the var=",var)



## Triangular
def triangular():
    a = float(input("Enter your starting value: "))
    b = float(input("Enter the mean value between 0 and 1: "))
    c = float(input("Enter your highest value: "))
    n = int(input("Enter your integer sample size: "))
    
    
    from scipy.stats import triang
    data_triang = triang.rvs(loc=a, c=b, scale=c, size=n)
    
    graph = sns.displot(data_triang,
                      kde=True,
                      bins='auto',
                      color='purple')
    graph.set(xlabel='Triangular Distribution', ylabel='Frequency')
    plt.show()

    mean, var, skew, kurt = triang.stats(c, moments='mvsk')
    print("Triangular distribution: mean=",mean," and the var=",var)



## Beta
def beta():
    a = float(input("Enter your starting value: "))
    b = float(input("Enter the end value: "))
    n = int(input("Enter your integer sample size: "))
    
    from scipy.stats import beta
    data_beta = beta.rvs(a=a, b=b, size=n)
    
    graph = sns.displot(data_beta,
                      kde=False,
                      bins='auto',
                      color='purple')
    graph.set(xlabel='Beta(a,b)', ylabel='Frequency')
    plt.show()

    mean, var, skew, kurt = beta.stats(a, b, moments='mvsk')
    print("Beta distribution: mean=",mean," and the var=",var)



## Weibull
def weibull():
    a = float(input("Enter your scale parameter: "))
    b = float(input("Enter the shape parameter: "))
    n = int(input("Enter your integer sample size: "))
    
    #This is distribution is making a warning so we remove it
    
    import warnings
    warnings.filterwarnings("ignore")
    
    from scipy.stats import exponweib
    data_exponweib = exponweib.rvs(a=a, c=b, size=n)
    #a= scale parameter
    #c= shape parameter
    
    graph = sns.displot(data_exponweib,
                      kde=True,
                      bins='auto',
                      color='purple')
    graph.set(xlabel='Weibull Distribution', ylabel='Frequency')
    plt.show()

    mean, var, skew, kurt = exponweib.stats(a, c, moments='mvsk')
    print("Weibull distribution: mean=",mean," and the var=",var)
    warnings.filterwarnings("default")
weibull()


## Cauchy
from scipy.stats import cauchy
data_cauchy = cauchy.rvs(size=n)

graph = sns.displot(data_cauchy,
                  bins='auto',
                  kde=True,
                  color='purple')
graph.set(xlabel='Cauchy Distribution', ylabel='Frequency')
plt.show()

mean, var, skew, kurt = cauchy.stats(moments='mvsk')
print("Cauchy distribution: mean=",mean," and the var=",var)



## Normal
from scipy.stats import norm
# generate random numbers from N(0,1)
data_normal = norm.rvs(loc=a, scale=b, size=n)

graph = sns.displot(data_normal,
                  bins='auto',
                  kde=True,
                  color='purple')
graph.set(xlabel='Normal Distribution', ylabel='Frequency')
plt.show()

mean, var, skew, kurt = norm.stats(moments='mvsk')
print("Normal distribution: mean=",mean," and the var=",var)