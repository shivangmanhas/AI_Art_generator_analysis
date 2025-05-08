import pandas as pd
from src import eda, preprocessing, clustering, model
import os

os.makedirs('outputs', exist_ok=True)

DATA_PATH = '/Users/shivang/Desktop/ai_art_generator_analysis/data/AI_Art_Generator_Platform_data.csv'

def load_data(path):
    print(f"Loading data from {path}...")
    df = pd.read_csv(path)
    print("First 5 rows of the dataset:")
    print(df.head())
    return df

if __name__ == '__main__':
    df = load_data(DATA_PATH)
    
    # === Run EDA ===
    eda.plot_api_availability(df)
    eda.plot_commercial_use(df)
    eda.plot_watermark(df)
    eda.plot_resolution_vs_cost(df)
    eda.plot_subscription_tiers(df)

    # === Preprocess Data ===
    df = preprocessing.preprocess_data(df)
    
    # === Perform Clustering ===
    clustered_df = clustering.perform_clustering(df, n_clusters=3)

    # === Predictive Modeling ===
    model.build_and_evaluate_model(df)
