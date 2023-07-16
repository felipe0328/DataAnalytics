from services import ExternalData
import pandas as pd
from io import StringIO
from flask import json
from dal.analitics.purchaseAnalitics import insert_new_analitics_entry
import asyncio


def analize_data_and_return_results() -> dict[str, str]:
    receivedData = ExternalData.obtain_dataset()  # data format is string
    dataStringIO = StringIO(receivedData)
    df = pd.read_csv(dataStringIO, sep=',', header=0)
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Analizing the data

    # Analizing by element_type
    purchasesByType = df['element_type'].value_counts()

    # Obtaining the mean of the amount of money inverted by hour
    # This works to know what was the time where more money was inverted by users
    moneyInvertedByHour = df.groupby(
        [df['timestamp'].dt.hour]).purchase_amount.mean()

    # Group the data by the element type
    purchaseElementsSubset = df[['element_type', 'purchase_amount']]
    purchaseGroupedData = purchaseElementsSubset.groupby(['element_type'])
    purchaseElementCountData = purchaseGroupedData.count()

    # Get the amount of elements purchased by hour, to understand how many elements are purchased by hour
    elementsPurchasedSubset = df[['timestamp', 'element_type']]
    elementsPurchasedAndGrouped = elementsPurchasedSubset.groupby(
        [elementsPurchasedSubset['timestamp'].dt.hour, 'element_type'])
    elementsPurchasedByHour = elementsPurchasedAndGrouped.count()

    purchasesByTypeJson = json.loads(purchasesByType.to_json(orient='index'))

    insert_new_analitics_entry(purchasesByTypeJson)

    analizedData = {
        'PurchaseByType': purchasesByTypeJson,
        'MoneyInvertedByHour': json.loads(moneyInvertedByHour.to_json()),
        'ElementsTypePurchasedCount': json.loads(purchaseElementCountData.purchase_amount.to_json()),
        'ElementsPurchasedByHour': json.loads(elementsPurchasedByHour.timestamp.to_json())
    }

    return analizedData
