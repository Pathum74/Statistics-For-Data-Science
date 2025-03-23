import scipy.stats as stats

variance=0.037
n=24
s=0.11
alpha=0.05

#Test statistical and distribution
T_stat=((n-1)*(s**2))/variance

#Critical value
T_critical1=stats.chi2.ppf(1-alpha/2,df=n-1) 
T_critical2=stats.chi2.ppf(1-(1-alpha/2),df=n-1)

if T_stat>T_critical1 or T_stat<T_critical2:
    print('We can reject H node and 5% level of significance.')
else:
    print('We can not reject H node and 5% level of significance.')

print(f'T statistic value: {T_stat:.4f}')
print(f'T critical value1: {T_critical1:.4f}')
print(f'T critical value2: {T_critical2:.4f}')
