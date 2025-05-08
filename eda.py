import matplotlib.pyplot as plt
import seaborn as sns

def plot_api_availability(df):
    print("\nPlotting API availability...")
    api_count = df['API Available'].value_counts()
    sns.barplot(x=api_count.index, y=api_count.values)
    plt.title('Platforms Offering API')
    plt.xlabel('API Available')
    plt.ylabel('Number of Platforms')
    plt.show()

def plot_commercial_use(df):
    print("\nPlotting Commercial Use Allowed...")
    commercial_count = df['Commercial Use Allowed'].value_counts()
    sns.barplot(x=commercial_count.index, y=commercial_count.values)
    plt.title('Platforms Allowing Commercial Use')
    plt.xlabel('Commercial Use Allowed')
    plt.ylabel('Number of Platforms')
    plt.show()

def plot_watermark(df):
    print("\nPlotting Watermark presence...")
    watermark_count = df['Watermark'].apply(lambda x: 'Yes' if 'Yes' in str(x) else 'No').value_counts()
    sns.barplot(x=watermark_count.index, y=watermark_count.values)
    plt.title('Platforms Adding Watermark')
    plt.xlabel('Watermark Present')
    plt.ylabel('Number of Platforms')
    plt.show()

def plot_resolution_vs_cost(df):
    print("\nPlotting Max Resolution vs. Cost per Image...")

    def extract_resolution(res):
        try:
            return int(res.split('x')[0])
        except:
            return None

    def extract_cost(cost):
        try:
            cost = str(cost).replace('$', '').split('–')[0].split('(')[0]
            return float(cost.strip())
        except:
            return None

    df['Resolution_Num'] = df['Max Resolution'].apply(extract_resolution)
    df['Cost_Num'] = df['Cost per Image'].apply(extract_cost)

    plot_df = df.dropna(subset=['Resolution_Num', 'Cost_Num'])

    if plot_df.empty:
        print("Not enough numeric data for this plot.")
    else:
        plt.scatter(plot_df['Resolution_Num'], plot_df['Cost_Num'])
        plt.title('Max Resolution vs. Cost per Image')
        plt.xlabel('Max Resolution (Width in Pixels)')
        plt.ylabel('Cost per Image (USD)')
        plt.show()

def plot_subscription_tiers(df):
    print("\nPlotting Subscription Tier Prices...")

    # Function to extract the *lowest* numeric price from subscription tiers
    def extract_lowest_price(tier_str):
        import re
        prices = re.findall(r'\$([0-9]+(?:\.[0-9]+)?)', str(tier_str))
        prices = [float(p) for p in prices]
        return min(prices) if prices else None

    # Apply extraction
    df['Lowest_Subscription_Price'] = df['Subscription Tiers (per month)'].apply(extract_lowest_price)

    # Drop NaNs (platforms with no subscription)
    sub_df = df.dropna(subset=['Lowest_Subscription_Price'])

    if sub_df.empty:
        print("No numeric subscription data found.")
    else:
        # Plot histogram of subscription prices
        sns.histplot(sub_df['Lowest_Subscription_Price'], bins=8, kde=False)
        plt.title('Distribution of Lowest Subscription Prices')
        plt.xlabel('Lowest Subscription Price (USD per Month)')
        plt.ylabel('Number of Platforms')
        plt.show()
