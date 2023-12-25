import logging
import os

import pandas as pd
from sqlalchemy import text

from app import queries
from app.configs import RAW_DATA_PATH
from app.connections import DataBaseClient

logging.getLogger().setLevel(logging.INFO)


mysql_client = DataBaseClient(
    user=os.getenv("MYSQL_ROOT_USER"),
    password=os.getenv("MYSQL_ROOT_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    db=os.getenv("MYSQL_DATABASE"),
    port=os.getenv("MYSQL_PORT"),
    dialect="mysql",
    driver="pymysql",
    echo=False
)

pg_client = DataBaseClient(
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    db=os.getenv("POSTGRES_DATABASE"),
    port=os.getenv("POSTGRES_PORT"),
    dialect="postgresql",
    driver="psycopg2",
    echo=False
)


def upload_csv_to_mysql() -> None:
    """
    The upload_csv_to_mysql function is designed 
    to facilitate the process of uploading data from a local CSV file into a MySQL database.
    """
    global mysql_client

    schema = os.getenv("MYSQL_DATABASE")
    for csv_file in os.listdir(RAW_DATA_PATH):
        base_name = csv_file.split('.')[0]
        data = pd.read_csv(os.path.join(RAW_DATA_PATH, csv_file))
        mysql_client.save_dataframe_to_the_database(
            data=data, table_name=base_name, schema=schema, index=False, if_exists='replace'
        )


def mysql_to_postgres_data_migration() -> None:
    """
    This function performs a data migration task, extracting data from a MySQL database,
    transforming it as needed, and uploading it to a PostgreSQL database. It is designed
    to facilitate the seamless transfer of data between the two database systems.
    """
    global mysql_client, pg_client

    table_query_mapping = {
        'weekly_activity': queries.query_extract_weekly_activity,
        'total_activity': queries.query_total_activity,
        'filtered_session': queries.query_filtering_session
    }
    for table_name, query in table_query_mapping.items():
        data_transformed = mysql_client.execute_read_query(
            query=text(query),
            dataframe=True,
        )
        pg_client.save_dataframe_to_the_database(
            data=data_transformed, 
            table_name=table_name, 
            schema=os.getenv("POSTGRES_SCHEMA"), 
            index=False, 
            if_exists='replace'
        )


if __name__ == '__main__':
    upload_csv_to_mysql()
    mysql_to_postgres_data_migration()
