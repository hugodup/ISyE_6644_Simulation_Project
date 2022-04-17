# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 10:04:18 2022

@author: Group 208 - Hugo Dupouy (GT903738077)
"""
##############################################################################

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

# Discrete

## Bernoulli
def bernoulli():
    #Inputs
    p = float(input("Enter your probability (between 0 and 1): "))
    n = int(input("Enter your sample size: "))
    
    #Generating RV
    from scipy.stats import bernoulli
    data_bern = bernoulli.rvs(p=p, size=n)
    
    #Graph
    graph= sns.displot(data_bern,
                     kde=False,
                     color="purple")
    graph.set(xlabel='Bernoulli Distribution', ylabel='Frequency')

    #Statistics
    mean, var, skew, kurt = bernoulli.stats(p, moments='mvsk')
    print("Bernoulli distribution: mean=",mean," and the var=",var)

    #Show the graph
    plt.show()



## Binomial
def binomial():
    #Inputs
    p = float(input("Enter your probability (between 0 and 1): "))
    n = int(input("Enter your sample size: "))
    
    #Generating RV
    from scipy.stats import binom
    data_binom = binom.rvs(n=n, p=p, size=n)
    
    #Graph
    graph = sns.displot(data_binom,
                      kde=False,
                      color='purple')
    graph.set(xlabel='Binomial Distribution', ylabel='Frequency')

    #Statistics
    mean, var, skew, kurt = binom.stats(n, p, moments='mvsk')
    print("Binomial distribution: mean=",mean," and the var=",var)

    #Show the graph
    plt.show()



## Geometric
def geometric():
    #Inputs
    p = float(input("Enter your probability (between 0 and 1): "))
    n = int(input("Enter your sample size: "))
    
    #Generating RV
    from scipy.stats import geom
    data_geom = geom.rvs(p, size=n)
    
    #Graph
    graph = sns.displot(data_geom,
                      kde=False,
                      color='purple')
    graph.set(xlabel='Geometric', ylabel='Frequency')

    #Statistics
    mean, var, skew, kurt = geom.stats(p, moments='mvsk')
    print("Geometric distribution: mean=",mean," and the var=",var)

    #Show the graph
    plt.show()



## Negative Binomial
def negative_binomial():
    #Inputs
    p = float(input("Enter your probability (between 0 and 1): "))
    n = int(input("Enter your sample size: "))

    #Generating RV    
    from scipy.stats import nbinom
    data_nbinom = nbinom.rvs(n=n, p=p, size=n)
    
    #Graph
    graph = sns.displot(data_nbinom,
                      kde=False,
                      color='purple')
    graph.set(xlabel='Negative Binomial', ylabel='Frequency')

    #Statistics
    mean, var, skew, kurt = nbinom.stats(n, p, moments='mvsk')
    print("Negative Binomial distribution: mean=",mean," and the var=",var)

    #Show the graph
    plt.show()



## Poisson
def poisson():
    #Inputs
    mu = float(input("Enter the mu-value: "))
    n = int(input("Enter your sample size: "))
    
    #Generating RV
    from scipy.stats import poisson
    data_poisson = poisson.rvs(mu=mu, size=n)
    
    #Graph
    graph = sns.displot(data_poisson,
                      bins='auto',
                      kde=False,
                      color='purple')
    graph.set(xlabel='Poisson Distribution', ylabel='Frequency')

    #Statistics
    mean, var, skew, kurt = poisson.stats(mu, moments='mvsk')
    print("Poisson distribution: mean=",mean," and the var=",var)

    #Show the graph
    plt.show()



##############################################################################



# Continuous

## Uniform
def uniform():
    #Inputs
    start = float(input("Enter your starting value a: "))
    width = float(input("Enter the width of the data b: "))
    n = int(input("Enter your integer sample size in the interval (a,b): "))

    #Generating RV
    from scipy.stats import uniform
    data_uniform = uniform.rvs(loc=start, scale=width, size=n)
    
    #Graph
    graph = sns.displot(data_uniform,
                      bins='auto',
                      kde=True,
                      color='purple')
    graph.set(xlabel='Uniform Distribution ', ylabel='Frequency')

    #Statistics
    mean, var, skew, kurt = uniform.stats(moments='mvsk')
    print("Uniform distribution: mean=",mean," and the var=",var)

    #Show the graph
    plt.show()




## Exponential
def exponential():
    #Inputs
    start = float(input("Enter your starting value a: "))
    width = float(input("Enter the width of the data b: "))
    n = int(input("Enter your integer sample size in the interval (a,b): "))
    
    #Generating RV
    from scipy.stats import expon
    data_expon = expon.rvs(loc=start, scale=width, size=n)
    
    #Graph
    graph = sns.displot(data_expon,
                      kde=True,
                      bins='auto',
                      color='purple')
    graph.set(xlabel='Exponential Distribution', ylabel='Frequency')

    #Statistics
    mean, var, skew, kurt = expon.stats(moments='mvsk')
    print("Exponential distribution: mean=",mean,"and the var=",var)

    #Show the graph
    plt.show()




## Erlang
def erlang():
    #Inputs
    a = float(input("Enter your lambda value: "))
    n = int(input("Enter your integer sample size: "))
    
    #Generating RV
    from scipy.stats import erlang
    data_erlang = erlang.rvs(a=a, size=n)
    
    #Graph
    graph = sns.displot(data_erlang,
                      kde=True,
                      bins='auto',
                      color='purple')
    graph.set(xlabel='Erlang Distribution', ylabel='Frequency')

    #Statistics
    mean, var, skew, kurt = erlang.stats(a, moments='mvsk')
    print("Erlang distribution: mean=",mean," and the var=",var)

    #Show the graph
    plt.show()



## Gamma
def gamma():
    #Inputs
    a = float(input("Enter your lambda value: "))
    n = int(input("Enter your integer sample size: "))
    
    #Generating RV
    from scipy.stats import gamma
    data_gamma = gamma.rvs(a, size=n)
    
    #Graph
    graph = sns.displot(data_gamma,
                      kde=True,
                      bins='auto',
                      color='purple')
    graph.set(xlabel='Gamma Distribution', ylabel='Frequency')

    #Statistics
    mean, var, skew, kurt = gamma.stats(a, moments='mvsk')
    print("Gamma distribution: mean=",mean," and the var=",var)

    #Show the graph
    plt.show()



## Triangular
def triangular():
    #Inputs
    a = float(input("Enter your starting value: "))
    b = float(input("Enter the mean value between 0 and 1: "))
    c = float(input("Enter your highest value: "))
    n = int(input("Enter your integer sample size: "))
    
    #Generating RV
    from scipy.stats import triang
    data_triang = triang.rvs(loc=a, c=b, scale=c, size=n)
    
    #Graph
    graph = sns.displot(data_triang,
                      kde=True,
                      bins='auto',
                      color='purple')
    graph.set(xlabel='Triangular Distribution', ylabel='Frequency')

    #Statistics
    mean, var, skew, kurt = triang.stats(c, moments='mvsk')
    print("Triangular distribution: mean=",mean," and the var=",var)

    #Show the graph
    plt.show()



## Beta
def beta():
    #Inputs
    a = float(input("Enter your starting value: "))
    b = float(input("Enter your ending value: "))
    n = int(input("Enter your integer sample size: "))
    
    #Generating RV
    from scipy.stats import beta
    data_beta = beta.rvs(a=a, b=b, size=n)
    
    #Graph
    graph = sns.displot(data_beta,
                      kde=False,
                      bins='auto',
                      color='purple')
    graph.set(xlabel='Beta(a,b)', ylabel='Frequency')

    #Statistics
    mean, var, skew, kurt = beta.stats(a, b, moments='mvsk')
    print("Beta distribution: mean=",mean," and the var=",var)

    #Show the graph
    plt.show()



## Weibull
def weibull():
    #Inputs
    a = float(input("Enter your scale parameter: "))
    b = float(input("Enter the shape parameter: "))
    n = int(input("Enter your integer sample size: "))
    
    #This is distribution is making a warning so we remove it
    import warnings
    warnings.filterwarnings("ignore")
    
    #Generating RV
    from scipy.stats import exponweib
    data_exponweib = exponweib.rvs(a=a, c=b, size=n)
    #a= scale parameter
    #c= shape parameter
    
    #Graph
    graph = sns.displot(data_exponweib,
                      kde=True,
                      bins='auto',
                      color='purple')
    graph.set(xlabel='Weibull Distribution', ylabel='Frequency')

    #Statistics
    mean, var, skew, kurt = exponweib.stats(a=a, c=b, moments='mvsk')
    print("Weibull distribution: mean=",mean," and the var=",var)
    warnings.filterwarnings("default") #to enable warning again

    #Show the graph
    plt.show()



## Cauchy
def cauchy():
    #Inputs
    n = int(input("Enter your integer sample size: "))

    # #Generating RV
    from scipy.stats import cauchy
    data_cauchy = cauchy.rvs(size=n)

    #Graph
    graph = sns.displot(data_cauchy,
                    bins='auto',
                    kde=True,
                    color='purple')
    graph.set(xlabel='Cauchy Distribution', ylabel='Frequency')
    
    #Show the graph
    plt.show()

    #Statistics
    #mean, var, skew, kurt = cauchy.stats(moments='mvsk')
    #print("Cauchy distribution: mean=",mean," and the var=",var, skew, kurt)
    #we found out that the distribution can not generate a mean and variation


## Normal
def normal():
    #Inputs
    a = float(input("Enter beginning interval a: "))
    b = float(input("Enter ending interval b: "))
    n = int(input("Enter your integer sample size: "))
    
    #Generating RV
    from scipy.stats import norm
    # generate random numbers from N(a,b)
    data_normal = norm.rvs(loc=a, scale=b, size=n)

    #Graph
    graph = sns.displot(data_normal,
                    bins='auto',
                    kde=True,
                    color='purple')
    graph.set(xlabel='Normal Distribution', ylabel='Frequency')

    #Statistics
    mean, var, skew, kurt = norm.stats(moments='mvsk')
    print("Normal distribution: mean=",mean," and the var=",var)

    #Show the graph
    plt.show()



##############################################################################

# Welcome message
def welcome():
    print("Welcome to the Random Variate Distribution Generator\n")

# Asking the user to choose the distribution
def distribution_choice():
    print("Here are the availablee Random Variable Distributions:\n",
            "1  - Bernoulli\n",
            "2  - Binomial\n",
            "3  - Geometric\n",
            "4  - Negative Binomial\n",
            "5  - Poisson\n",
            "6  - Uniform\n",
            "7  - Exponential\n",
            "8  - Erlang\n",
            "9  - Gamma\n",
            "10 - Triangual\n",
            "11 - Beta\n",
            "12 - Weibull\n",
            "13 - Cauchy\n",
            "14 - Normal\n"
            )
    # Retrieving the distribution number from user until we have a correct number
    distribution_number = int(input("Please kindly enter the number of the distribution"))
    while distribution_number not in range(1,15):
        distribution_number = int(input("Please enter an interger number from the list above (ex: 14):"))
    
    return distribution_call()


# Calling the functions
def distribution_call():
    #double checking that the number is an integer and in-between 
    assert type(distribution_number) is int and distribution_number>0 and distribution_number<16
    #Launching the distribution based on the number
    if distribution_number = 1:
        return bernoulli()
    elif distribution_number = 2:
        return binomial()
    elif distribution_number = 3:
        return binomial()
    elif distribution_number = 4:
        return binomial()
    elif distribution_number = 5:
        return binomial()
    elif distribution_number = 6:
        return binomial()
    elif distribution_number = 7:
        return binomial()
    elif distribution_number = 8:
        return binomial()
    elif distribution_number = 9:
        return binomial()
    elif distribution_number = 10:
        return binomial()
    elif distribution_number = 11:
        return binomial()
    elif distribution_number = 12:
        return binomial()
    elif distribution_number = 13:
        return binomial()
    elif distribution_number = 14:
        return binomial()
    else:
        return distribution_choice()


bernoulli()
binomial()
geometric()
negative_binomial()
poisson()

uniform()
exponential()
erlang()
gamma()

triangular()
beta()
weibull()
cauchy()
normal()