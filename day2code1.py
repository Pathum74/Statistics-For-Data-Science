import scipy.stats as stats

test_1=[82,69,73,43,58,56,76,85]
test_2=[63,43,74,37,51,43,80,82]

# Perform wilcoxon signed-rank test
stat, p_value= stats.wilcoxon(test_1,test_2)

# Output the results
print(f'Test statistic: {stat}')
print(f'P-Value: {p_value}')

# Interpret the result
alpha = 0.5 
if p_value<alpha:
    print('There is a significant different between the two tests (reject null hypothesis).')
else:
    print('There is no significant difference between the two tests (fail to reject null hypothesis).')
