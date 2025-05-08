#🎨 AI Art Generator Platform Analysis

##🚀 Project Overview
This project analyzes and models data from 24 popular AI art generator platforms, focusing on their pricing strategies, feature sets, and market positioning. The goal is to uncover insights into:

How platforms structure their pricing,

Which features are most common across the market,

And how these factors correlate with subscription tiers and service accessibility.

The analysis includes exploratory data analysis (EDA), market segmentation (clustering), and a predictive model to estimate the pricing tier of an AI art generator based on its core features.

##📊 Key Objectives
###EDA & Visualization:

Compare API availability, watermark policies, and commercial-use permissions across platforms.

Visualize pricing tiers and maximum image resolution support.

###Clustering:

Use KMeans clustering + PCA to segment platforms into market clusters based on technical and pricing features.

###Predictive Modeling:

Train a Random Forest classifier to predict a platform's pricing tier (Low/Medium/High) based on its characteristics.

##🔧 Tools & Technologies
Python 3.x

pandas, matplotlib, seaborn

scikit-learn (KMeans, Random Forest)

PCA (for dimensionality reduction)

Visual Studio Code (development environment)

##🗂️ Project Structure

ai-art-platform-analysis/
├── data/
│   └── AI_Art_Generator_Platform_data.csv
├── outputs/
│   └── (plots, models)
├── src/
│   ├── eda.py              # EDA functions
│   ├── preprocessing.py    # Feature engineering
│   ├── clustering.py       # Market segmentation
│   └── model.py            # Predictive modeling
├── main.py
├── requirements.txt
└── README.md

##🔥 Highlights

Market Insight: Identified clusters of platforms that offer premium features (e.g., high resolution, API access) and typically charge higher subscription fees.

Predictive Power: Built a Random Forest model that predicts a platform's pricing tier based on API availability, resolution, watermark policy, and other factors.

Reusable Codebase: The project is modular and easy to extend—future improvements could include more features, additional platforms, or a web app interface.

##📈 Sample Outputs
###✅ EDA Visuals:

API availability distribution

Watermark presence bar plot

Max resolution vs. cost scatter plot

Subscription price distribution

###✅ Clustering:

PCA 2D plot showing 3 distinct clusters of platforms

###✅ Model Performance:

Random Forest classification report (precision, recall, F1-score)

Confusion matrix heatmap

Feature importance bar chart

##📄 License
This project is for educational and portfolio purposes.

