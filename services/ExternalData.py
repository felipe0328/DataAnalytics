import config
import requests


def obtain_dataset() -> str:
    dataset_request = requests.get(config.LAMBDA_ENDPOINT)
    if dataset_request.status_code == 200:
        return dataset_request.content.decode()
