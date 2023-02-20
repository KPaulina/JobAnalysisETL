import pandas as pd
from sqlalchemy import create_engine
from consts import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
from sqlalchemy.exc import OperationalError


def load_new_python_data_to_postgres(df_python_new: pd.DataFrame):
    '''
    Function that loads chosen from json data to postgres
    :return:
    '''
    try:
        db = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
        conn = db.connect()
        df_python_new.to_sql('new_python_jobs', db, schema='public', if_exists='append', index=False)
    except OperationalError as error:
        print(f'Operational error: {error}')


def load_python_data_to_postgres(df_python: pd.DataFrame):
    '''
    Function that loads chosen from json data to postgres
    :return:
    '''
    try:
        db = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
        conn = db.connect()
        df_python.to_sql('python_jobs', db, schema='public', if_exists='append', index=False)
    except OperationalError as error:
        print(f'Operational error: {error}')
