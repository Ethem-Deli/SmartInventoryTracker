# SmartInventoryTracker
"A robust SQL-based inventory management system integrated with an employee directory. Features include real-time stock tracking, FIFO batch management, restocking alerts, fast-moving item analysis, and role-based employee management. Built using Oracle SQL."

# Smart Inventory Tracker

A project that tracks inventory and employee information.

## Features
- Inventory Management: Track product quantities, prices, and sales.
- FIFO Logic: Manage batches using FIFO.
- Employee Directory: Store employee details.
- Low Stock Tracker: Alerts for products below a specified quantity.
- Fastest Selling Item: Identify the best-selling product based on sales data.

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   python app.py
   ```

## Testing
Run tests using:
```bash
python -m unittest discover tests

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