import cx_Oracle

try:
    # Explicitly specify the Oracle Client library path
    cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient")
    print("Oracle Client initialized successfully!")
except cx_Oracle.DatabaseError as e:
    print(f"Error initializing Oracle Client: {e}")
