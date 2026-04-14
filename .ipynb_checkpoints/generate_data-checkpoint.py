import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random 

# settings for data generation
np.random.seed(42)
random.seed(42)

# list of products and categories
products=['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones', 'Web Camera', 'USB drive', 'Hard disc', 'SSD', 'Graphic Card', 'Processor', 'RAM memory', 'Motherboard', 'Power Supply', 'Case']
categories=['Computers', 'Peripherals', 'Components', 'Equipment']
regions=['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego']

# date generation - last 24 months
start_date=datetime(2023,1,1)
end_date=datetime(2024,12,31)
num_transactions=5000

# data generation
data=[]

for i in range(num_transactions):
    days_diff= (end_date-start_date).days
    random_day=random.randint(0,days_diff)
    date=start_date+timedelta(days=random_day)
    #random product
    product=random.choice(products)

    #category assignment based on product
    if product in ['Laptop', 'Monitor', 'Graphic Card', 'Processor', 'RAM memory', 'Motherboard', 'Power Supply', 'Case']:
        category='Computers' if product == 'Laptop' else 'Components'
    elif product in ['Mouse', 'Keyboard', 'Headphones', 'Web Camera']:
        category='Peripherals' 
    else: 
        category= 'Equipment'

    # quantity
    quantity=random.randint(1,10)

    # price per unit - different prices for different products
    product_prices={
        'Laptop':(500,2000), 
        'Monitor':(150,800), 
        'Graphic Card':(300,1500), 
        'Processor':(200,1000), 
        'RAM memory':(50,300), 
        'Motherboard':(100,500), 
        'Power Supply':(50,200),
        'Case':(30,150),
        'Mouse':(20,150), 
        'Keyboard':(30,250), 
        'Headphones':(50,400),
        'Web Camera':(50,200), 
        'USB drive':(10,100),
        'Hard disc':(50,300), 
        'SSD':(80,500)
        }

    min_price, max_price=product_prices.get(product, (10,100))
    price_per_unit=random.randint(min_price, max_price)

    total_value=quantity*price_per_unit

    # cost - about 60-70% of price
    cost_per_unit=int(price_per_unit*random.uniform(0.6, 0.7))
    total_costs=quantity*cost_per_unit

    # region
    region=random.choice(regions)

    data.append({
        'Date':date,
        'Product':product, 
        'Category':category, 
        'Quantity':quantity, 
        'Price_per_unit': price_per_unit, 
        'Total_value':total_value, 
        'Region': region, 
        'Costs': total_costs
    })

# create dataframe
df=pd.DataFrame(data)  

# sort by date
df=df.sort_values('Date').reset_index(drop=True)   # descending indexes

# save to csv file
df.to_csv('sales_data.csv', index=False, encoding='utf-8-sig')

print(f'Generated {len(df)} transactions')
print(f'Period: {df["Date"].min()} to {df["Date"].max()}')
print(f'File Saved As: sales_data.csv')









