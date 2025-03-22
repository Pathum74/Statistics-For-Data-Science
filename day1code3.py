import scipy.stats as stats

#given data
variance=(3.4)**2
n=30
s=4.1
alpha=0.05

#Test statistic and distribution
T_stat=((n-1)*(s**2))/(variance)

#Critical value
T_critical=stats.chi2.ppf(1-alpha,df=n-1,)

if T_stat>T_critical:
    print('Reject H node and 5% level of significance.')
else:
    print('We can not reject H node and 5% level of significance.')     

print(f'T statistic value {T_stat:.4f}')
print(f'T critical value: {T_critical:.4f}')