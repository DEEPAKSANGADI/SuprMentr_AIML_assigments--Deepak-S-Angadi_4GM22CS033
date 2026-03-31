import numpy as np

import matplotlib.pyplot as plt

# Sample data for visualization
categories = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [45, 38, 52, 41, 49]
ages = np.random.normal(35, 15, 1000)

# Create figure with subplots
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Sales and Demographic Analysis', fontsize=16, fontweight='bold')

# Bar Chart
axes[0, 0].bar(categories, sales, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8'])
axes[0, 0].set_title('Sales by Product', fontweight='bold')
axes[0, 0].set_ylabel('Sales ($1000s)')
axes[0, 0].grid(axis='y', alpha=0.3)

# Pie Chart
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
axes[0, 1].pie(sales, labels=categories, autopct='%1.1f%%', colors=colors, startangle=90)
axes[0, 1].set_title('Market Share Distribution', fontweight='bold')

# Histogram
axes[1, 0].hist(ages, bins=30, color='#45B7D1', edgecolor='black', alpha=0.7)
axes[1, 0].set_title('Age Distribution of Customers', fontweight='bold')
axes[1, 0].set_xlabel('Age')
axes[1, 0].set_ylabel('Frequency')
axes[1, 0].grid(axis='y', alpha=0.3)

# Data Story (text)
story = """
DATA STORY: Market Performance & Demographics

Key Findings:
• Product C leads with 52K in sales (19.6%)
• Product B underperforms with 38K (14.4%)
• Average customer age: 35 years
• Customer base is distributed across all age groups

Trends:
1. Product C & E show strong demand (above average)
2. Products A & B require marketing boost
3. Diverse customer base suggests broad market appeal
4. Mid-range pricing (Product A: 45K) attracts stable segment
"""

axes[1, 1].text(0.05, 0.95, story, transform=axes[1, 1].transAxes, 
                fontsize=10, verticalalignment='top', fontfamily='monospace',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
axes[1, 1].axis('off')

plt.tight_layout()
plt.show()