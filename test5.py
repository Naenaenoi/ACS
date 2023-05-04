from scipy.stats import binom

probability=float(input())
#calculate binomial probability
print(binom.pmf(k=2, n=5, p=probability))