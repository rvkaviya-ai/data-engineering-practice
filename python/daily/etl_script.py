import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(f"{func.__name__} took {end_time - start_time} seconds")
        return result
    return wrapper

@timer
def extract_data(file_path):

    try:
        df = pd.read_csv('/Users/kaviya/Desktop/py_kaviya/orders.csv',
                         dtype={'order_id':str, 'amount':float,'customer_name':str,'status':str},
                         parse_dates=['order_date'],
                         sep=',',
                        encoding='utf-8'                        
                        )
        return df
    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        raise
    except Exception as e:
        logger.error(f"Error reading file: {e}")
        raise

def validate_data(df):
    try:
        if df['order_id'].isnull().sum() > 0:
            raise ValueError(" order_id values is null")
        if df['amount'].isnull().any() > 0:
            raise ValueError("amount values is null")
        logger.info(f"Data validation passed: {len(df)} records")

    except Exception as e:
        logger.error(f"Error validating data: {e}")
        raise

def transform_data(df):
    try:
        df['status'] = df['status'].str.lower().str.strip()
        df = df[df['status'] =='completed']
        df['amount_inr'] = df['amount'] * 83

        logger.info(f"Data transformation completed: {len(df)} records")
        return df
    except Exception as e:
        logger.error(f"Error transforming data: {e}")
        raise

def load_data(df, output_path):
    try:
        schema = pa.schema(
            [
                pa.field('order_id', pa.string()),
                pa.field('customer_name', pa.string()),
                pa.field('amount', pa.float64()),
                pa.field('order_date', pa.date32()),
                pa.field('status', pa.string()),
                pa.field('amount_inr', pa.float64())
            ]
        )
        table = pa.Table.from_pandas(df, schema=schema)
        pq.write_table(table, output_path, compression='snappy')
        logger.info(f"Data loaded successfully to {output_path}")
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        raise

if __name__ == "__main__":
    input_file = '/Users/kaviya/Desktop/py_kaviya/orders.csv'
    output_file = '/Users/kaviya/Desktop/py_kaviya/orders.parquet'

    try:
        logger.info("Starting ETL pipeline...")
        df = extract_data(input_file)
        validate_data(df)
        df= transform_data(df)
        load_data(df, output_file)
        logger.info("ETL pipeline completed successfully.")
    except Exception as e:
        logger.error(f"ETL pipeline failed: {e}")
