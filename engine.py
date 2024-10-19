# engine.py

class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        """
        Initialize an AST Node.
        
        :param node_type: 'operator' (AND/OR) or 'operand' (conditions).
        :param value: Operand condition or operator (e.g., 'age > 30' or 'AND').
        :param left: Left child node.
        :param right: Right child node.
        """
        self.type = node_type  # 'operator' or 'operand'
        self.value = value  # the condition for operand, or None for operator
        self.left = left  # left child node
        self.right = right  # right child node

    def __repr__(self):
        """
        Represent the node for easy debugging.
        """
        if self.type == "operand":
            return f"Operand({self.value})"
        else:
            return f"Operator({self.value}, {self.left}, {self.right})"
import re

def create_rule(rule_string):
    """
    Parse a rule string into an Abstract Syntax Tree (AST).
    
    :param rule_string: A string representing a rule like "(age > 30 AND department = 'Sales')"
    :return: Root node of the AST.
    """
    # Removing extra spaces and splitting by 'AND' and 'OR' operators
    rule_string = rule_string.replace(" ", "")
    tokens = re.split(r'(\(|\)|AND|OR)', rule_string)
    
    # Parsing logic (basic parser)
    stack = []
    
    for token in tokens:
        if token == "" or token == "(" or token == ")":
            continue
        if token == "AND" or token == "OR":
            operator = token
        else:
            # Operand like "age>30"
            operand = Node("operand", token)
            if len(stack) > 0:
                operator_node = Node("operator", operator)
                operator_node.left = stack.pop()
                operator_node.right = operand
                stack.append(operator_node)
            else:
                stack.append(operand)

    # The remaining item in the stack is the root of the AST
    return stack.pop()
def evaluate_rule(ast, data):
    """
    Evaluate the rule AST against the user data.
    
    :param ast: AST Node representing the rule.
    :param data: Dictionary containing user data (e.g., {"age": 35, "department": "Sales"}).
    :return: True if the rule matches the data, False otherwise.
    """
    if ast.type == "operand":
        # Evaluate the operand, e.g., "age>30"
        condition = ast.value
        attribute, operator, value = re.split(r'(>|<|=)', condition)
        attribute_value = data.get(attribute)
        if operator == ">":
            return attribute_value > int(value)
        elif operator == "<":
            return attribute_value < int(value)
        elif operator == "=":
            return attribute_value == value
    
    elif ast.type == "operator":
        # Evaluate the operator AND/OR
        if ast.value == "AND":
            return evaluate_rule(ast.left, data) and evaluate_rule(ast.right, data)
        elif ast.value == "OR":
            return evaluate_rule(ast.left, data) or evaluate_rule(ast.right, data)

    return False
