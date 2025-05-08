import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

def perform_clustering(df, n_clusters=3):
    print("\nStarting clustering...")

    # Select numeric columns for clustering
    features = [
        'API_Available_Num',
        'Commercial_Use_Num',
        'Watermark_Num',
        'Resolution_Num',
        'Cost_Num',
        'Lowest_Subscription_Price'
    ]

    X = df[features].dropna()

    if X.empty:
        print("Not enough data for clustering.")
        return

    # Standardize the data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Apply KMeans
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df_clusters = df.loc[X.index].copy()
    df_clusters['Cluster'] = kmeans.fit_predict(X_scaled)

    print(f"Cluster counts:\n{df_clusters['Cluster'].value_counts()}\n")

    # Optional: PCA to 2D for visualization
    pca = PCA(n_components=2)
    components = pca.fit_transform(X_scaled)
    df_clusters['PCA1'] = components[:, 0]
    df_clusters['PCA2'] = components[:, 1]

    # Plot clusters
    plt.figure(figsize=(8, 6))
    for cluster in range(n_clusters):
        clustered_data = df_clusters[df_clusters['Cluster'] == cluster]
        plt.scatter(clustered_data['PCA1'], clustered_data['PCA2'], label=f'Cluster {cluster}')
    plt.title('Platform Clusters (PCA 2D)')
    plt.xlabel('PCA Component 1')
    plt.ylabel('PCA Component 2')
    plt.legend()
    plt.show()

    df_clusters.to_csv('/Users/shivang/Desktop/ai_art_generator_analysis/outputs/final_platform_analysis.csv', index=False)
    print("Clustered data saved to outputs/final_platform_analysis.csv")

    return df_clusters


