import os
from dotenv import load_dotenv

load_dotenv()

LAMBDA_ENDPOINT = "https://bxfmcf6d7rxlea64sn7wcvx5my0vjpjj.lambda-url.us-east-1.on.aws/"


class Config:
    DATABASE_URL = "data-managment-db.cdsoq1tqo8hf.us-east-1.rds.amazonaws.com"
    DATABASE_NAME = "analytics"
    SQLALCHEMY_DATABASE_URI = f'mssql+pyodbc://{os.getenv("DATABASE_USER")}:{os.getenv("DATABASE_PWD")}@{DATABASE_URL}/{DATABASE_NAME}?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
