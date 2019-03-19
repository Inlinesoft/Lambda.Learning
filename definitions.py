import os
import urllib.parse
from prettyconf import config

VERSION="0.0.1"

ROOT_DIR=os.path.dirname(os.path.abspath(__file__))

DATABASE_HOST =config('DATABASE_HOST')
DATABASE_USER =config('DATABASE_USER')
DATABASE_PASS =config('DATABASE_PASS')
DATABASE_NAME =config('DATABASE_NAME')
DATABASE_CONN_URL = "mssql+pymssql://{username}:{password}@{host}/{database}".format(
    username = config('DATABASE_USER')
    , password = urllib.parse.quote_plus(config('DATABASE_PASS'))
    , host=config('DATABASE_HOST')
    , database=config('DATABASE_NAME')
)

EMAIL_ACCOUNT_USERNAME=config('EMAIL_ACCOUNT_USERNAME')
EMAIL_ACCOUNT_PASSWORD=config('EMAIL_ACCOUNT_PASSWORD')
EMAIL_PRIMARY_SMTP_ADDRESS=config('EMAIL_PRIMARY_SMTP_ADDRESS')