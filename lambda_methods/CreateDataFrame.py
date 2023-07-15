# This code creates a fake dataset.

import csv
import random
from datetime import datetime, timedelta

def lambda_handler(event, context):
    
    file_object = create_random_data()
    # TODO implement
    return {
        'statusCode': 200,
        'headers': { "Content-Type": "text/csv" },
        'body': file_object.read().encode('utf-8')
    }

def create_random_data():
    
    header = ['purchase_amount', 'element_type', 'timestamp']
    elementTypes = ['Bed', 'Dinning Table', 'Mattress', 'Office Desk', 'Pillow']
    
    currentTime = datetime.now()
    
    with open('/tmp/file.csv', 'w', encoding="utf-8")  as file:
        writer = csv.writer(file)
        
        writer.writerow(header)
        
        for _ in range(1000): #creating 1000 elements in the csv
            purchase_amount = random.randint(100, 10000) # the purchase can be between 100 and 10 thousand usd
            element_type = random.choice(elementTypes)
            timestamp = currentTime - timedelta(minutes=(random.randint(1,1440)))
            writer.writerow([purchase_amount, element_type, timestamp])
    
    return open('/tmp/file.csv', 'r')