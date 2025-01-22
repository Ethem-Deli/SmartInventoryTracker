import os
from flask import Flask, jsonify, request, send_from_directory
from app.database import get_connection
from app.models import add_inventory_item, add_employee

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return send_from_directory('static', 'index.html')

    # Retrieve inventory with color scale and low-stock reminders
    @app.route('/api/inventory', methods=['GET'])
    def inventory():
        connection = get_connection()
        if not connection:
            return jsonify({"error": "Database connection failed."}), 500
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM inventory")
            rows = cursor.fetchall()

            # Color scale for pricing and low-stock reminders
            inventory_list = []
            for row in rows:
                item = {col[0]: row[idx] for idx, col in enumerate(cursor.description)}
                price = item['price']
                quantity = item['quantity']
                batch_name = item['batch_name']

                # Color scale based on price (green to red)
                if price < 10:
                    item['price_color'] = "green"
                elif 10 <= price <= 50:
                    item['price_color'] = "yellow"
                else:
                    item['price_color'] = "red"

                # Low stock alert
                if quantity < 5:
                    item['low_stock_alert'] = True
                else:
                    item['low_stock_alert'] = False

                inventory_list.append(item)

            return jsonify(inventory_list)
        finally:
            cursor.close()
            connection.close()

    # Add an inventory item with batch name (FIFO management)
    @app.route('/api/inventory', methods=['POST'])
    def add_inventory():
        data = request.get_json()
        product_name = data.get('product_name')
        quantity = data.get('quantity')
        price = data.get('price')
        batch_name = data.get('batch_name')

        if not all([product_name, quantity, price, batch_name]):
            return jsonify({"error": "All fields are required!"}), 400

        connection = get_connection()
        if not connection:
            return jsonify({"error": "Database connection failed."}), 500
        cursor = connection.cursor()
        try:
            cursor.execute(
                """
                INSERT INTO inventory (product_name, quantity, price, batch_name)
                VALUES (:product_name, :quantity, :price, :batch_name)
                """,
                {
                    "product_name": product_name,
                    "quantity": quantity,
                    "price": price,
                    "batch_name": batch_name
                }
            )
            connection.commit()
            return jsonify({"message": "Item added successfully!"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()
            connection.close()

    # Fast-moving item tracker
    @app.route('/api/fast_moving_items', methods=['GET'])
    def fast_moving_items():
        connection = get_connection()
        if not connection:
            return jsonify({"error": "Database connection failed."}), 500
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT product_name, COUNT(*) as sales_count
                FROM sales
                GROUP BY product_name
                ORDER BY sales_count DESC
                LIMIT 5
            """)
            rows = cursor.fetchall()
            return jsonify([{"product_name": row[0], "sales_count": row[1]} for row in rows])
        finally:
            cursor.close()
            connection.close()

    # Employee directory management
    @app.route('/api/employees', methods=['GET'])
    def employees():
        connection = get_connection()
        if not connection:
            return jsonify({"error": "Database connection failed."}), 500
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM employees")
            rows = cursor.fetchall()
            return jsonify([{col[0]: row[idx] for idx, col in enumerate(cursor.description)} for row in rows])
        finally:
            cursor.close()
            connection.close()

    @app.route('/api/employees', methods=['POST'])
    def add_employee_endpoint():
        data = request.json
        name = data.get('name')
        contact_details = data.get('contact_details')
        department = data.get('department')

        if not all([name, contact_details, department]):
            return jsonify({"error": "All fields are required!"}), 400

        add_employee(name, contact_details, department)
        return jsonify({"message": "Employee added successfully!"})

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

