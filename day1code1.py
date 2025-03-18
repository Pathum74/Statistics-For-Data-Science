#pip install scipy
import scipy.stats as stats

#Give data 
mu_0=2500 #population mean
x_bar=2571 #Sample mean 
s=115 #sample standard deviation
n=7 #sample size
alpha=0.05

#Perform one sample T test
#Calculate t score
t_stat=(x_bar-mu_0)/(s/(n**0.5))


#Critical value
t_critical=stats.t.ppf(1-alpha,df=n-1)
# In python, alpha show '1-alpha' acording to real alpha
# ppf(q) return the value of t such that the probability of getting a value less than or equal to t is q.

if t_stat>t_critical:
    print('Reject the null hypothesis:There is sufficent evidance to conclude that the sewer pipe meets requried')
else:
    print('Fall to reject the null hyppthesis')   

print(f'T statistics (T value): {t_stat:.4f}')     
print(f'Critical T value: {t_critical:.4f}')



