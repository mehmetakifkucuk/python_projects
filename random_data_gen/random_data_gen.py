import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

# Create a Faker instance for generating fake data
fake = Faker()

# Number of orders and customers
num_orders = 200
num_customers = 50

# Generate customer data
customers = []
for _ in range(num_customers):
    customer_id = fake.unique.random_number(digits=5)
    customer_registration_date = fake.date_between(start_date='-5y', end_date='today')
    customers.append((customer_id, customer_registration_date))

# Generate order data
orders = []
for _ in range(num_orders):
    order_id = fake.unique.random_number(digits=6)
    customer_id, registration_date = random.choice(customers)
    unit_id = fake.unique.random_number(digits=4)
    number_of_items = random.randint(1, 10)
    unit_price = round(random.uniform(10, 1000), 2)
    order_date = fake.date_between(start_date=registration_date, end_date='today')
    unit_name = fake.word()
    unit_category = fake.word()
    orders.append((
        order_id, customer_id, unit_id, number_of_items, unit_price,
        order_date, unit_name, unit_category, registration_date
    ))

# Create a DataFrame
columns = [
    'order_id', 'customer_id', 'unit_id', 'number_of_items', 'unit_price',
    'order_date', 'unit_name', 'unit_category', 'customer_registration_date'
]
df = pd.DataFrame(orders, columns=columns)

# Save the dataset to a CSV file
df.to_csv('dummy_dataset.csv', index=False)
