import pandas as pd
import os
from sqlalchemy import create_engine, inspect
import logging
import time

# Set up MySQL connection details
username = 'root'
password = 'Raisha789'
host = 'localhost'
port = 3306
database = 'vendor'

# Create SQLAlchemy engine for MySQL connection
engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')

# Inspect existing tables in the database
inspector = inspect(engine)
existing_tables = inspector.get_table_names()

# Set up logging to file
os.makedirs("vendorlog", exist_ok=True)  # Create log directory if not exists

logging.basicConfig(
    filename="vendorlog/ingestion_db.log",  # File to store logs
    level=logging.DEBUG,                     # Log level DEBUG and above
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log format
    filemode="a"                            # Append mode (do not overwrite logs)
)

def ingest_db(df, table_name, engine):
    '''This function ingests a DataFrame into a MySQL table'''
    df.to_sql(table_name, con=engine, if_exists='append', index=False)

def load_raw_data():
    # Record the start time to measure total ingestion duration
    start = time.time()

    # Loop through all files in the 'vendordata' folder
    for file in os.listdir('vendordata'):
        if file.endswith('.csv'):
            table_name = file[:-4]  # Remove '.csv' extension
            
            # This script is designed to run and ingest CSV files from 'vendordata' folder
            # into corresponding MySQL tables (except for the 'sales' table, which exists already in MySQL)
            
            # Skip ingestion if this table already exists in the database
            if table_name in existing_tables:
                logging.info(f"⏩ Skipping '{table_name}', already ingested.")
                continue
            
            # Read CSV file into DataFrame
            df = pd.read_csv(f'vendordata/{file}')
            logging.info(f"📥 Ingesting '{table_name}' with shape {df.shape}")
            
            # Insert DataFrame into the database table
            ingest_db(df, table_name, engine)

    # Calculate total time taken for ingestion in minutes
    end = time.time()
    total_time = (end - start) / 60
    
    # Log completion messages
    logging.info('Ingestion Complete')
    logging.info(f'Total Time Taken: {total_time:.2f} minutes')

# Run the ingestion only if this script is executed directly
if __name__ == '__main__':
    load_raw_data()
