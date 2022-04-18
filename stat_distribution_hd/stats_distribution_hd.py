# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 10:04:18 2022

@author: Group 208 - Hugo Dupouy (GT903738077)

Library of Random Variate distributions based on the Simulation Project from Georgia Tech.
    
    """

##############################################################################
def __init__(self):

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
    pass        
        
##############################################################################

# Discrete

## Bernoulli
def bernoulli(p,n):
    #Message
    x="Bernoulli distribution"
    print(x)
        
    #Inputs
    #p = float(input("Enter your probability (between 0 and 1): "))
    #n = int(input("Enter your sample size: "))
        
    #Generating RV
    from scipy.stats import bernoulli as y
    data = y.rvs(p=p, size=n)
        
    return statistics(y,x,p), graph_generator(data,x), distribution_end()



## Binomial
def binomial(p,n):
    #Message
    x="Binomial distribution"
    print(x)
        
    #Inputs
    #p = float(input("Enter your probability (between 0 and 1): "))
    #n = int(input("Enter your sample size: "))
        
    #Generating RV
    from scipy.stats import binom as y
    data = y.rvs(n=n, p=p, size=n)

    return statistics(y,x,n,p), graph_generator(data,x), distribution_end()    



## Geometric
def geometric(p,n):
    #Message
    x="Geometric distribution"
    print(x)
        
    #Inputs
    #p = float(input("Enter your probability (between 0 and 1): "))
    #n = int(input("Enter your sample size: "))
        
    #Generating RV
    from scipy.stats import geom as y
    data = y.rvs(p=p, size=n)

    return statistics(y,x,p), graph_generator(data,x), distribution_end()



## Negative Binomial
def negative_binomial(p,n):
    #Message
    x="Negative Binomial distribution"
    print(x)
        
    #Inputs
    #p = float(input("Enter your probability (between 0 and 1): "))
    #n = int(input("Enter your sample size: "))
    #Generating RV    
    from scipy.stats import nbinom as y
    data = y.rvs(n=n, p=p, size=n)
    return statistics(y,x,n,p), graph_generator(data,x), distribution_end()


## Poisson
def poisson(c,n):
    #Message
    x="Poisson distribution"
    print(x)
        
    #Inputs
    #c = float(input("Enter the mu-value: "))
    #n = int(input("Enter your sample size: "))
    
    #Generating RV
    from scipy.stats import poisson as y
    data = y.rvs(mu=c, size=n)
    
    return statistics(y,x,c), graph_generator(data,x), distribution_end()

##############################################################################



# Continuous

## Uniform
def uniform(start, width, n):
    #Message
    x="Uniform distribution"
    print(x)
    
    #Inputs
    #start = float(input("Enter your starting value a: "))
    #width = float(input("Enter the width of the data b: "))
    #n = int(input("Enter your integer sample size in the interval (a,b): "))
    #Generating RV
    from scipy.stats import uniform as y
    data = y.rvs(loc=start, scale=width, size=n)
    
    return statistics(y,x), graph_generator(data,x), distribution_end()



## Exponential
def exponential(a,b,n):
    #Message
    x="Exponential distribution"
    print(x)
    
    #Inputs
    #a = float(input("Enter your starting value a: "))
    #b = float(input("Enter the width of the data b: "))
    #n = int(input("Enter your integer sample size: "))
    
    #Generating RV
    from scipy.stats import expon as y
    data = y.rvs(loc=a, scale=b, size=n)
    
    return statistics(y,x), graph_generator(data,x), distribution_end()



## Erlang
def erlang(c,n):
    #Message
    x="Erlang distribution"
    print(x)
        
    #Inputs
    #c = float(input("Enter your lambda value: "))
    #n = int(input("Enter your integer sample size: "))
    
    #Generating RV
    from scipy.stats import erlang as y
    data = y.rvs(c, size=n)
    
    return statistics(y,x,c), graph_generator(data,x), distribution_end()


## Gamma
def gamma(a,n):
    #Message
    x="Gamma distribution"
    print(x)
    
    #Inputs
    #a = float(input("Enter your lambda value: "))
    #n = int(input("Enter your integer sample size: "))
    
    #Generating RV
    from scipy.stats import gamma as y
    data = y.rvs(a=a, size=n)
    
    return statistics(y,x,a), graph_generator(data,x), distribution_end()


## Triangular
def triangular(a,c,b,n):
    #Message
    x="Triangular distribution"
    print(x)
    
    #Inputs
    #a = float(input("Enter your starting value: "))
    #c = float(input("Enter the mean value between 0 and 1: "))
    #b = float(input("Enter your highest value: "))
    #n = int(input("Enter your integer sample size: "))
    
    #Generating RV
    from scipy.stats import triang as y
    data = y.rvs(loc=a, c=c, scale=b, size=n)
    
    return statistics(y,x,c), graph_generator(data,x), distribution_end()


## Beta
def beta(a,b,n):
    #Message
    x="Beta distribution"
    print(x)
    
    #Inputs
    #a = float(input("Enter your starting value: "))
    #b = float(input("Enter your ending value: "))
    #n = int(input("Enter your integer sample size: "))
    
    #Generating RV
    from scipy.stats import beta as y
    data = y.rvs(a=a, b=b, size=n)
    
    return statistics(y,x,a,b), graph_generator(data,x), distribution_end()


## Weibull
def weibull(a,b,n):
    #Message
    x="Weibull distribution"
    print(x)
    
    #Inputs
    #a = float(input("Enter your scale parameter: "))
    #b = float(input("Enter the shape parameter: "))
    #n = int(input("Enter your integer sample size: "))
    
    #This is distribution is making a warning so we remove it
    import warnings
    warnings.filterwarnings("ignore")
    
    #Generating RV
    from scipy.stats import exponweib as y
    data = y.rvs(a=a, c=b, size=n)
    #a= scale parameter
    #c= shape parameter
    
    return statistics(y,x,a,b), graph_generator(data,x), distribution_end()



## Cauchy
def cauchy(n):
    #Message
    x="Cauchy distribution"
    print(x)

    #Inputs
    #n = int(input("Enter your integer sample size: "))

    # #Generating RV
    from scipy.stats import cauchy as y
    data = y.rvs(size=n)

    #Statistics
    #mean, var, skew, kurt = cauchy.stats(moments='mvsk')
    #print("Cauchy distribution: mean=",mean," and the var=",var, skew, kurt)
    #we found out that the distribution can not generate a mean and variation

    return graph_generator(data,x), distribution_end()



## Normal
def normal(a,b,n):
    #Message
    x="Normal distribution"
    print(x)
        
    #Inputs
    #a = float(input("Enter beginning interval a: "))
    #b = float(input("Enter ending interval b: "))
    #n = int(input("Enter your integer sample size: "))
        
    #Generating RV
    from scipy.stats import norm as y
    # generate random numbers from N(a,b)
    data = y.rvs(loc=a, scale=b, size=n)

    return statistics(y,x), graph_generator(data,x), distribution_end()


##############################################################################

# Generating Stats and Graphs:

#Statistics
# The y.stats() requires different parameters based on the distribution y
def statistics(y,x,a=None,b=None,c=None,n=None,p=None):
    if a == None and b == None and c == None and n == None and p != None:
        mean, var, skew, kurt = y.stats(p, moments='mvsk')
        print(x,": mean=",mean," and the var=",var)
    elif a != None and b != None and c == None and n == None and p == None:
        mean, var, skew, kurt = y.stats(a, b, moments='mvsk')
        print(x,": mean=",mean," and the var=",var)
    elif a != None and b == None and c != None and n == None and p == None:
        mean, var, skew, kurt = y.stats(a, c, moments='mvsk')
        print(x,": mean=",mean," and the var=",var)
    elif a == None and b == None and c == None and n != None and p != None:
        mean, var, skew, kurt = y.stats(n, p, moments='mvsk')
        print(x,": mean=",mean," and the var=",var)
    elif a != None and b == None and c == None and n == None and p == None:
        mean, var, skew, kurt = y.stats(a, moments='mvsk')
        print(x,": mean=",mean," and the var=",var)
    elif a == None and b == None and c != None and n == None and p == None:
        mean, var, skew, kurt = y.stats(c, moments='mvsk')
        print(x,": mean=",mean," and the var=",var)
    else:
        mean, var, skew, kurt = y.stats(moments='mvsk')
        print(x,": mean=",mean," and the var=",var)
        

#Graph
def graph_generator(data,x):
    graph = sns.displot(data,
                        bins='auto',
                        kde=True,
                        color='purple')
    graph.set(xlabel=x, ylabel='Frequency')
    return plt.show()


##############################################################################

# Welcome message to start the program
def welcome():
    print("Welcome to the Random Variate Distribution Generator\n")
    return distribution_choice()

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
    distribution_number = int(input("Please kindly enter the number of the distribution: "))
    while distribution_number not in range(1,15):
        distribution_number = int(input("Please enter an interger number from the list above (ex: 14): "))
        
    return distribution_call(distribution_number)


# Calling the functions
def distribution_call(distribution_number):
    #double checking that the number is an integer and in-between 
    assert isinstance(distribution_number, int) 
    assert distribution_number in range(1,15)
    
    #Launching the distribution based on the number
    if distribution_number == 1:
        return bernoulli()
    elif distribution_number == 2:
        return binomial()
    elif distribution_number == 3:
        return geometric()
    elif distribution_number == 4:
        return negative_binomial()
    elif distribution_number == 5:
        return poisson()
    elif distribution_number == 6:
        return uniform()
    elif distribution_number == 7:
        return exponential()
    elif distribution_number == 8:
        return erlang()
    elif distribution_number == 9:
        return gamma()
    elif distribution_number == 10:
        return triangular()
    elif distribution_number == 11:
        return beta()
    elif distribution_number == 12:
        return weibull()
    elif distribution_number == 13:
        return cauchy()
    elif distribution_number == 14:
        return normal()
    else:
        return distribution_choice()


def distribution_end():
    # Asking to continue or not
    answer = int(input("Do you want to continue with a new distribution or not ?\n Enter 1 for Yes and 0 for No: "))
    while answer not in range(0,2):
        answer = int(input("Please double check your choice\n Enter 1 or 0: "))
    # Asnwer choice
    if answer == 1: return distribution_choice()
    elif answer == 0: return print("Thank you for trying our Library of distributions. Bye-bye!")        