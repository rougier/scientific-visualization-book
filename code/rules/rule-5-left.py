from pylab import *

fig = plt.figure(figsize=(8, 4))

n = 256
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)
plot(X, C), plot(X, S)

savefig("../../figures/rules/rule-5-left.pdf")
show()
