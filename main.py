import pandas as pd
from load import load_new_python_data_to_postgres, load_python_data_to_postgres
from extract import connect_to_mongodb_for_python_jobs, connect_to_mongodb_for_new_python_jobs
from transform import transform_before_loading

if __name__ == '__main__':
    all_python_offers = connect_to_mongodb_for_python_jobs()
    new_python_offers = connect_to_mongodb_for_new_python_jobs()
    new_python_offers = transform_before_loading(new_python_offers)
    all_python_offers = transform_before_loading(all_python_offers)
    all_python_offers = all_python_offers.drop(columns='is_new')

    load_python_data_to_postgres (all_python_offers)
    load_new_python_data_to_postgres(new_python_offers)

