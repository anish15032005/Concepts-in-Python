def Bigo(n):
    return 45*n**3+20*n**2+19

#we will observe that as the value of n increases, the terms with lower exponents become less significant
print(Bigo(10))
#so that this algo has an order of n^3


from math import log
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial  # Import factorial function
plt.style.use('bmh')

# Set up runtime comparisons
n = np.linspace(1, 10, 100)  # Increase resolution for smoother curves
labels = ['Constant', 'Logarithmic', 'Linear', 'Log Linear', 'Quadratic', 'Cubic', 'Exponential', 'Factorial', 'n^n']
big_o = [
    np.ones(n.shape),  # Constant
    np.log(n),         # Logarithmic
    n,                 # Linear
    n * np.log(n),     # Log Linear
    n**2,              # Quadratic
    n**3,              # Cubic
    2**n,              # Exponential
    factorial(n, exact=False),  # Factorial
    n**n               # n^n
]

# Plot setup
plt.figure(figsize=(12, 10))
plt.ylim(0, 50)  # Adjust as needed for better visualization

for i in range(len(big_o)):
    plt.plot(n, big_o[i], label=labels[i])

plt.legend(loc=0)
plt.ylabel('Relative Runtime')
plt.xlabel('n')
plt.title('Big-O Complexity Comparisons')
plt.show()