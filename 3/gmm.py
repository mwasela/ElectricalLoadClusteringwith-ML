import pandas as pd
from scipy.stats import multivariate_normal
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
import numpy as np

# Generate sample data
df = pd.read_csv("output.csv")
imputer = SimpleImputer(strategy='median')
X = imputer.fit_transform(df)

# Initialize the GMM model
gmm = GaussianMixture(n_components=2, covariance_type='full', max_iter=1000)

# Fit the GMM model using the EM algorithm
gmm.fit(X)

# Compute the means, covariances, and mixing weights of the Gaussian components
means = gmm.means_
covs = gmm.covariances_
weights = gmm.weights_

# Compute the probability density function of each Gaussian component for each observation
densities = np.array([multivariate_normal.pdf(X, mean=means[k], cov=covs[k]) for k in range(len(weights))]).T

# Compute the final probability that each observation belongs to each cluster as a convex combination of the Gaussian components
probs = np.dot(densities, weights)

probs = pd.DataFrame(probs, columns=['Cluster 1 Probability'])
probs.to_csv('probs.csv', index=False)

print(probs[:223])

# Plot the probabilities for the first 100 observations
plt.plot(probs[:223])
plt.xlabel('Observations')
plt.ylabel('Probability')
plt.title('GMM Probabilities of first 223 Days')
plt.show()