# SmartInventoryTracker
"A robust SQL-based inventory management system integrated with an employee directory. Features include real-time stock tracking, FIFO batch management, restocking alerts, fast-moving item analysis, and role-based employee management. Built using Oracle SQL."

## Project Description
Smart Inventory Tracker is a web application that helps manage inventory efficiently. It supports:

- **FIFO Management**: Ensures first-in-first-out for inventory batches.
- **Low Stock Alerts**: Automatically notifies for low stock items.
- **Fast-Selling Item Tracking**: Identifies the fastest-selling items.
- **Employee Directory**: Stores employee information such as name, contact, and department.
- **Price-Based Coloring**: Highlights inventory items with color codes based on their price ranges.

## Features
1. Inventory tracking with price-based coloring (green, yellow, red).
2. Automated inventory reminders for low-stock items.
3. REST API for accessing inventory and employee data.
4. FIFO-based inventory deduction.
5. Employee management system.

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   python app.py
   ```
## Setup Instructions
1. Clone the repository:
    ```bash
    git clone <repository_url>
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables in a `.env` file:
    ```env
    DB_USER=<your_username>
    DB_PASSWORD=<your_password>
    DB_DSN=<your_dsn>
    ```

4. Initialize the database:
    ```bash
    python init.sql
    ```

5. Run the application:
    ```bash
    python app.py
    ```

## API Endpoints
1. `/api/inventory`: Fetch all inventory items.
2. `/api/low_stock`: Fetch low stock items (threshold: 15).
3. `/api/priced_colored`: Fetch inventory items with price-based coloring.

## Future Enhancements
- Add user authentication.
- Build a fully-featured front-end with charts.
then output will be 
Serving Flask app 'app' (lazy loading)
 * Environment: development
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 860-900-161
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [21/Jan/2025 13:29:12] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [21/Jan/2025 13:29:13] "GET /favicon.ico HTTP/1.1" 404 -

##CONGRATULATION THE APP IS RUNNING WELL

youtube video walktrough the code
https://youtu.be/oieFII7i8SE