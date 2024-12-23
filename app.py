from flask import Flask, jsonify, request, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Khalid@123',
        database='ecommerce',
        auth_plugin='mysql_native_password'
    )
    return connection

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_customers', methods=['GET'])
def get_customers():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM customer;")
        customers = cursor.fetchall()
        return jsonify(customers)
    except Error as e:
        return jsonify({"error": str(e)})
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/get_addresses', methods=['GET'])
def get_addresses():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM address;")
        addresses = cursor.fetchall()
        return jsonify(addresses)
    except Error as e:
        return jsonify({"error": str(e)})
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/get_orders', methods=['GET'])
def get_orders():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM orders;")
        orders = cursor.fetchall()
        return jsonify(orders)
    except Error as e:
        return jsonify({"error": str(e)})
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/get_products', methods=['GET'])
def get_products():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM product;")
        products = cursor.fetchall()
        return jsonify(products)
    except Error as e:
        return jsonify({"error": str(e)})
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/get_payments', methods=['GET'])
def get_payments():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM payments;")
        payments = cursor.fetchall()
        return jsonify(payments)
    except Error as e:
        return jsonify({"error": str(e)})
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/get_cancels', methods=['GET'])
def get_cancels():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM cancel;")
        cancels = cursor.fetchall()
        return jsonify(cancels)
    except Error as e:
        return jsonify({"error": str(e)})
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/get_whishlist', methods=['GET'])
def get_whishlist():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM whishlist;")
        whishlist = cursor.fetchall()
        return jsonify(whishlist)
    except Error as e:
        return jsonify({"error": str(e)})
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/get_recently', methods=['GET'])
def get_recently():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM recently;")
        recently = cursor.fetchall()
        return jsonify(recently)
    except Error as e:
        return jsonify({"error": str(e)})
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/get_coupons', methods=['GET'])
def get_coupons():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM coupon;")
        coupons = cursor.fetchall()
        return jsonify(coupons)
    except Error as e:
        return jsonify({"error": str(e)})
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/get_sales', methods=['GET'])
def get_sales():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM sale;")
        sales = cursor.fetchall()
        return jsonify(sales)
    except Error as e:
        return jsonify({"error": str(e)})
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/get_order_items', methods=['GET'])
def get_order_items():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM order_items;")
        order_items = cursor.fetchall()
        return jsonify(order_items)
    except Error as e:
        return jsonify({"error": str(e)})
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    app.run(debug=True) 