import pandas as pd

from extract import connect_to_mongodb_for_python_jobs, connect_to_mongodb_for_new_python_jobs


if __name__ == '__main__':
    all_python_offers = connect_to_mongodb_for_python_jobs()
    new_python_offers = connect_to_mongodb_for_new_python_jobs()

