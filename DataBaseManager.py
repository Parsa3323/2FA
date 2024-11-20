import sqlite3

conn = sqlite3.connect('data')
# Function to create a new database file and return a connection object
def create_database(db_name):
    """
    Create a new database file with the specified name.

    Parameters:
    db_name (str): The name of the database file (e.g., 'my_database.db').

    Returns:
    conn (sqlite3.Connection): A connection object to interact with the database.
    """
    conn = sqlite3.connect(db_name)  # Creates a new database file if it does not exist
    print(f"Database '{db_name}' created and connected successfully.")
    return conn


# Function to create a table in the database
def create_table(conn, table_name, columns):
    """
    Create a table in the connected database.

    Parameters:
    conn (sqlite3.Connection): The connection object.
    table_name (str): The name of the table to create.
    columns (dict): A dictionary where keys are column names and values are the column types (e.g., {'id': 'INTEGER', 'name': 'TEXT'}).

    Returns:
    None
    """
    cursor = conn.cursor()

    # Generate the SQL command for creating the table
    columns_with_types = ', '.join([f"{col} {col_type}" for col, col_type in columns.items()])
    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_with_types});"

    cursor.execute(create_table_query)
    conn.commit()
    print(f"Table '{table_name}' created successfully.")


# Function to insert data into a table
def insert_into_table(conn, table_name, data):
    """
    Insert data into a table.

    Parameters:
    conn (sqlite3.Connection): The connection object.
    table_name (str): The name of the table to insert data into.
    data (dict): A dictionary where keys are column names and values are the data to insert.

    Returns:
    None
    """
    cursor = conn.cursor()

    # Generate the SQL command for inserting the data
    columns = ', '.join(data.keys())
    placeholders = ', '.join('?' for _ in data)
    insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders});"

    cursor.execute(insert_query, tuple(data.values()))
    conn.commit()
    print(f"Data inserted into '{table_name}' successfully.")


# Function to get data from a table
def get_from_table(conn, table_name, columns="*", conditions=None):
    """
    Fetch data from a table and return it as a list of dictionaries.

    Parameters:
    conn (sqlite3.Connection): The connection object.
    table_name (str): The name of the table to query.
    columns (str): The columns to select (default is all columns '*').
    conditions (str, optional): The WHERE conditions to apply (default is None).

    Returns:
    list: A list of dictionaries where each dictionary represents a row.
    """
    cursor = conn.cursor()

    # Set the row factory to sqlite3.Row to return rows as dictionaries
    conn.row_factory = sqlite3.Row

    # Generate the SQL command to select data
    query = f"SELECT {columns} FROM {table_name}"
    if conditions:
        query += f" WHERE {conditions}"

    cursor.execute(query)
    rows = cursor.fetchall()

    # Convert rows (which are tuples) into a list of dictionaries
    result = [dict(row) for row in rows]

    return result

# Function to update data in a table
def update_table(conn, table_name, data, conditions):
    """
    Update data in a table.

    Parameters:
    conn (sqlite3.Connection): The connection object.
    table_name (str): The name of the table to update.
    data (dict): A dictionary where keys are column names and values are the new data.
    conditions (str): The WHERE conditions to specify which rows to update.

    Returns:
    None
    """
    cursor = conn.cursor()

    # Generate the SQL command for updating the data
    set_clause = ', '.join([f"{col} = ?" for col in data.keys()])
    update_query = f"UPDATE {table_name} SET {set_clause} WHERE {conditions};"

    cursor.execute(update_query, tuple(data.values()))
    conn.commit()
    print(f"Data in '{table_name}' updated successfully.")


# Function to delete data from a table
def delete_from_table(conn, table_name, conditions):
    """
    Delete data from a table.

    Parameters:
    conn (sqlite3.Connection): The connection object.
    table_name (str): The name of the table to delete data from.
    conditions (str): The WHERE conditions to specify which rows to delete.

    Returns:
    None
    """
    cursor = conn.cursor()

    # Generate the SQL command for deleting data
    delete_query = f"DELETE FROM {table_name} WHERE {conditions};"

    cursor.execute(delete_query)
    conn.commit()
    print(f"Data deleted from '{table_name}' successfully.")


# Example usage
# if __name__ == "__main__":
#     # Create a database and connect
#     db_name = "example.db"
#     conn = create_database(db_name)
#
#     # Create a table called "users"
#     table_name = "users"
#     columns = {"id": "INTEGER PRIMARY KEY", "name": "TEXT", "age": "INTEGER"}
#     create_table(conn, table_name, columns)
#
#     # Insert some data into the "users" table
#     user_data = {"name": "Alice", "age": 30}
#     insert_into_table(conn, table_name, user_data)
#
#     # Get data from the "users" table
#     users = get_from_table(conn, table_name)
#     print("Users:", users)
#
#     # Update data in the "users" table
#     updated_data = {"age": 31}
#     update_table(conn, table_name, updated_data, "name = 'Alice'")
#
#     # Get updated data from the "users" table
#     users = get_from_table(conn, table_name)
#     print("Updated Users:", users)
#
#     # Delete data from the "users" table
#     delete_from_table(conn, table_name, "name = 'Alice'")
#
#     # Get data after deletion
#     users = get_from_table(conn, table_name)
#     print("Users after Deletion:", users)
#
#     # Close the connection
#     conn.close()
