import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt

# Load CSV file into a Pandas dataframe
df = pd.read_csv('output.csv')

# Convert dataframe to numpy array
X = df.to_numpy()
# Impute nan values with median
imputer = SimpleImputer(strategy='median')
X = imputer.fit_transform(df)


# Create KMeans object and fit to data
kmeans = KMeans(n_clusters=9, random_state=0).fit(X)

# get cluster labels and counts
labels = kmeans.labels_
counts = np.bincount(labels)

# create a dataframe with cluster centroids
centroid_df = pd.DataFrame(kmeans.cluster_centers_, columns=df.columns)

# add a column for the frequency of occurrence of each cluster
centroid_df['Frequency of Occurrence'] = counts

# save centroid dataframe to csv file
centroid_df.to_csv('cluster_centroidsKmeans.csv', index=False)

#print each cluster index, its centroid and the count of observations for each of the clusters
#Introduce the PPAAC zero sum time decay function to mask the cluster info
for i in range(kmeans.n_clusters):
    print("Cluster ", i, " Centroid: ", kmeans.cluster_centers_[i][0], " Count: ", counts[i])

# a histogram showing the clusters and frequency distribution of each profile
plt.hist(labels, bins=range(10))
plt.xlabel('Clusters')
plt.ylabel('Frequency of occurrence')
plt.title('Frequency Distribution of DLP Across Kmeans Clusters')
plt.show()

# save frequency counts to csv file
freq_df = pd.DataFrame({'Cluster': range(kmeans.n_clusters), 'Frequency of Occurrence': counts})
freq_df.to_csv('cluster_frequenciesKmeans.csv', index=False)
