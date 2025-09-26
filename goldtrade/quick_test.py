# Tạo file quick_test.py
import sqlite3
import pandas as pd
from datetime import datetime, timedelta
import numpy as np

# Tạo mock database cho testing
conn = sqlite3.connect("gold_data.db")

# Mock current prices
current_data = []
sources = ['SJC', 'PNJ', 'DOJI', 'PhuQuy', 'BTMC']
base_price = 79000000

for i, source in enumerate(sources):
    for hour in range(24):  # 24 hours of data
        price_variation = np.random.normal(0, 50000)  # Random variation
        buy_price = base_price + (i * 100000) + price_variation
        sell_price = buy_price + np.random.uniform(200000, 500000)  # Spread
        
        current_data.append({
            'source': source,
            'buy': buy_price,
            'sell': sell_price,
            'unit': 'VND',
            'timestamp': datetime.now() - timedelta(hours=23-hour),
            'url': f'https://{source.lower()}.com/giavang',
            'raw': '[]'
        })

current_df = pd.DataFrame(current_data)
current_df.to_sql('gold_prices', conn, if_exists='replace', index=False)

print("✅ Mock data created successfully!")
print(f"📊 Created {len(current_df)} data points")
print("🚀 Now run: streamlit run dashboard.py")

conn.close()