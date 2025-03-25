# Mann whitneyu
import scipy.stats as stats

# Define the two samples
sample_1=[11,1,0,2,0]
sample_2=[11,11,8,5,4]

# Perform Mann Whitneyu U test
stat, p_value = stats.mannwhitneyu(sample_1,sample_2,alternative='two-sided')

# Output the results
print(f'Mann-Whitney U test statistic: {stat}')
print(f'P-value: {p_value}')

# Interpret the result
alpha=0.05
if p_value < alpha:
    print('The two sample come from significantly different distributions (reject null hyphothesis)')
else:
    print('There is no significant difference between the distribution of the two samples (fall)')    