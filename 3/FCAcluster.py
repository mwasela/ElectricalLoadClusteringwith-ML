import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from sklearn.impute import SimpleImputer


# Load CSV file into a Pandas dataframe
df = pd.read_csv('output.csv')

# Convert dataframe to numpy array
X = df.to_numpy()
# Impute nan values with median
imputer = SimpleImputer(strategy='median')
X = imputer.fit_transform(df)


#Set number of clusters desired
num_clusters = 6

#Perform fuzzy means clustering .The inputs to the function are the input data, the number of clusters, a fuzziness coefficient (in this case, 2), an error tolerance, and a maximum number of iterations.
cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(X, num_clusters, 2, error=0.005, maxiter=10000)

# This calculates the cluster assignments based on the membership matrix u by finding the maximum membership degree for each data point across all clusters.
labels = np.argmax(u, axis=0)


centroid_df = pd.DataFrame(cntr.T, columns=['Cluster {}'.format(i) for i in range(num_clusters)])

# Create dataframe for membership matrix
probs_df = pd.DataFrame(u.T, columns=['Cluster {} Probability'.format(i) for i in range(num_clusters)])

# Write dataframes to csv files
centroid_df.to_csv('cluster_centroidsFCA.csv', index=False)
probs_df.to_csv('membership_matrixFCA.csv', index=False)

print("Cluster Centroids:\n", cntr)
print("\nMembership Matrix:\n", u)
print("\nCluster Assignments:\n", labels)

