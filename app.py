from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app, template_file='swagger.yaml')

employees = [
    {"id": 1, "name": "John Doe", "department": "Production", "position": "Engineer"},
    {"id": 2, "name": "Jane Smith", "department": "Marketing", "position": "Manager"}
]
products = [
    {"id": 1, "name": "Widget X", "description": "High-quality widget for various applications", "price": 19.99},
    {"id": 2, "name": "Gadget Y", "description": "Innovative gadget for everyday use", "price": 49.95}
]
orders = [
    {"id": 1, "customerId": 123, "orderDate": "2024-10-26", "items": [{"productId": 1, "quantity": 2}, {"productId": 2, "quantity": 1}]}
]
customers = [
    {"id": 123, "name": "Jane Smith", "address": "123 Main St, Anytown, CA 91234", "phone": "555-123-4567", "email": "jane.smith@example.com"}
]
production_records = [
    {"id": 1, "productId": 1, "quantity": 100, "productionDate": "2024-10-27T08:00:00Z"}, 
    {"id": 2, "productId": 2, "quantity": 50,  "productionDate": "2024-10-27T10:00:00Z"}
]

# --- Employees ---
@app.route('/employees', methods=['GET'])
def get_employees():
    """
    List all employees
    ---
    responses:
      200:
        description: A list of employees
        schema:
          type: array
          items:
            $ref: '#/definitions/Employee'
    """
    return jsonify(employees)

@app.route('/employees', methods=['POST'])
def create_employee():
    """
    Create a new employee
    ---
    parameters:
      - in: body
        name: employee
        description: Employee object to be created
        required: true
        schema:
          $ref: '#/definitions/Employee'
    responses:
      201:
        description: Employee created successfully
        schema:
          $ref: '#/definitions/Employee'
    """
    new_employee = request.get_json()
    new_employee['id'] = len(employees) + 1
    employees.append(new_employee)
    return jsonify(new_employee), 201  


# --- Products ---
@app.route('/products', methods=['GET'])
def get_products():
    """
    List all products
    ---
    responses:
      200:
        description: A list of products
        schema:
          type: array
          items:
            $ref: '#/definitions/Product'
    """
    return jsonify(products)

@app.route('/products', methods=['POST'])
def create_product():
    """
    Create a new product
    ---
    parameters:
      - in: body
        name: product
        description: Product object to be created
        required: true
        schema:
          $ref: '#/definitions/Product'
    responses:
      201:
        description: Product created successfully
        schema:
          $ref: '#/definitions/Product'   

    """
    new_product = request.get_json()
    new_product['id'] = len(products) + 1
    products.append(new_product)
    return jsonify(new_product), 201

# --- Orders ---
@app.route('/orders', methods=['GET'])
def get_orders():
    """
    List all orders
    ---
    responses:
      200:
        description: A list of orders
        schema:
          type: array
          items:
            $ref: '#/definitions/Order'
    """
    return jsonify(orders)

@app.route('/orders', methods=['POST'])
def create_order():
    """
    Create a new order
    ---
    parameters:
      - in: body
        name: order
        description: Order object to be created
        required: true
        schema:
          $ref: '#/definitions/Order'
    responses:
      201:
        description: Order created successfully
        schema:
          $ref: '#/definitions/Order'
    """
    new_order = request.get_json()
    new_order['id'] = len(orders) + 1
    orders.append(new_order)
    return jsonify(new_order), 201

# --- Customers ---
@app.route('/customers', methods=['GET'])
def get_customers():
    """
    List all customers
    ---
    responses:
      200:
        description: A list of customers
        schema:
          type: array
          items:
            $ref: '#/definitions/Customer'
      500:
        description: Internal server error
        schema:
          $ref: '#/definitions/Error'
    """
    return jsonify(customers)

@app.route('/customers', methods=['POST'])
def create_customer():
    """
    Create a new customer
    ---
    parameters:
      - in: body
        name: customer
        description: Customer object to be created
        required: true
        schema:
          $ref: '#/definitions/Customer'
    responses:
      201:
        description: Customer created successfully
        schema:
          $ref: '#/definitions/Customer'
      400:
        description: Invalid input
        schema:
          $ref: '#/definitions/Error'
      500:
        description: Internal server error
        schema:
          $ref: '#/definitions/Error'   

    """
    new_customer = request.get_json()
    new_customer['id'] = len(customers) + 1
    customers.append(new_customer)
    return jsonify(new_customer), 201

@app.route('/customers/<int:id>', methods=['GET'])
def get_customer(id):
    """
    Get a customer by ID
    ---
    parameters:
      - in: path
        name: id
        description: ID of the customer to retrieve
        required: true
        type: integer
        format: int64
    responses:
      200:
        description: A customer object
        schema:
          $ref: '#/definitions/Customer'
      404:
        description: Customer not found
        schema:
          $ref: '#/definitions/Error'
      500:
        description: Internal server error
        schema:
          $ref: '#/definitions/Error'
    """
    customer = next((c for c in customers if c['id'] == id), None)
    if customer:
        return jsonify(customer)
    else:
        return jsonify({"code": "CUSTOMER_NOT_FOUND", "message": "Customer with the provided ID not found."}), 404

# --- Production Records ---
@app.route('/production', methods=['GET'])
def get_production_records():
    """
    List all production records
    ---
    responses:
      200:
        description: A list of production records
        schema:
          type: array
          items:
            $ref: '#/definitions/Production'
    """
    return jsonify(production_records) 

if __name__ == '__main__':
    app.run(debug=True)