import pandas as pd

def preprocess_data(df):
    # Convert API Available to numeric
    df['API_Available_Num'] = df['API Available'].apply(lambda x: 1 if 'Yes' in str(x) else 0)

    # Convert Commercial Use Allowed to numeric
    df['Commercial_Use_Num'] = df['Commercial Use Allowed'].apply(lambda x: 1 if 'Yes' in str(x) else 0)

    # Convert Watermark to numeric (Yes = 1, No = 0)
    df['Watermark_Num'] = df['Watermark'].apply(lambda x: 1 if 'Yes' in str(x) else 0)

    # Extract numeric resolution (first number in "2048x2048")
    def extract_resolution(res):
        try:
            return int(str(res).split('x')[0])
        except:
            return None

    df['Resolution_Num'] = df['Max Resolution'].apply(extract_resolution)

    # Extract numeric cost (take lowest in range)
    def extract_cost(cost):
        try:
            cost = str(cost).replace('$', '').split('–')[0].split('(')[0]
            return float(cost.strip())
        except:
            return None

    df['Cost_Num'] = df['Cost per Image'].apply(extract_cost)

    # Extract lowest subscription price (if available)
    def extract_lowest_price(tier_str):
        import re
        prices = re.findall(r'\$([0-9]+(?:\.[0-9]+)?)', str(tier_str))
        prices = [float(p) for p in prices]
        return min(prices) if prices else None

    df['Lowest_Subscription_Price'] = df['Subscription Tiers (per month)'].apply(extract_lowest_price)

    # Preview processed data
    print("\nPreview of processed data:")
    print(df[['API_Available_Num', 'Commercial_Use_Num', 'Watermark_Num', 'Resolution_Num', 'Cost_Num', 'Lowest_Subscription_Price']].head())

    return df
