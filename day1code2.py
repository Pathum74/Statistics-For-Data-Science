import scipy.stats as stats

#given data
mu_0 = 400
x_bar = 250
ps = 25
n= 50
alpha = 0.05


z_stat = abs((x_bar-mu_0)/(ps/(n**0.5)))

# get the critical t-value for one-tailed test
z_critical = stats.norm.ppf(1- alpha/2)
#ppf(q) returns the value pf t such that the probability of getting a value 

if z_stat > z_critical:
    print("reject the null hypothesis: there is sufficient evidence to conclude")
else:
    print("fail to reject the null hypithesis: there is not enough evidence to conclude that the sewer pipe meets the")

    #print results
print(f"Test statostoc (z-value): {z_stat:.4f}")
print(f"critical z-value: {z_critical:.4f}")
