from flask import Flask, jsonify, request

app = Flask(__name__)

# Base route (root URL)
@app.route('/')
def home():
    return "Welcome to the Rule Engine API!"

# Route for creating a rule
@app.route('/create_rule', methods=['POST'])
def create_rule():
    data = request.json
    rule = data.get('rule')
    if not rule:
        return jsonify({"error": "No rule provided"}), 400
    # Logic to create rule goes here
    return jsonify({"message": "Rule created", "rule": rule})

# Route for combining rules
@app.route('/combine_rules', methods=['POST'])
def combine_rules():
    data = request.json
    rules = data.get('rules')
    if not rules or not isinstance(rules, list):
        return jsonify({"error": "No rules provided"}), 400
    # Logic to combine rules goes here
    return jsonify({"message": "Rules combined", "rules": rules})

# Route for evaluating a rule
@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule():
    data = request.json
    ast = data.get('ast')
    input_data = data.get('data')
    if not ast or not input_data:
        return jsonify({"error": "Invalid data provided"}), 400
    # Logic to evaluate rule goes here
    return jsonify({"result": True})  # Just a placeholder

if __name__ == "__main__":
    app.run(debug=True, port=5500)

    