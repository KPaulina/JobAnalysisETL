import pandas as pd
import numpy as np


def transform_before_loading(df: pd.DataFrame):
    df = df[['job title', 'company_name', 'link', 'date', 'is_new']]
    df = df.rename(columns={'job title': 'job_title'})
    if 'is_new' in df.columns:
        df['is_new'] = np.where(df['is_new'].str.contains('NOWA'), True, False)
    # df_new_python_jobs.reset_index(inplace=True)
    # df_new_python_jobs = df_new_python_jobs.rename({'id': 'index'})
    return df

