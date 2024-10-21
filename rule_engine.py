import re
from ast_node import Node
import mysql.connector

def store_rule_in_db(rule_string):
    conn = mysql.connector.connect(user='root', password='2002', host='localhost', database='rule_engine')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO rules (rule_string) VALUES (%s)", (rule_string,))
    conn.commit()
    rule_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return rule_id

def parse_condition(condition):
    """Parses a condition like 'age > 30' into an AST node."""
    # Remove spaces from condition
    condition = condition.replace(" ", "")
    # Regex to capture the field, operator, and value
    match = re.match(r'([a-zA-Z_]+)([<>!=]=?|=)(.*)', condition)
    if match:
        field, operator, value = match.groups()
        # Convert numeric values to int or float
        value = value.strip("'")  # Remove surrounding quotes for string values
        if value.isdigit():
            value = int(value)
        else:
            try:
                value = float(value)
            except ValueError:
                pass  # Keep as string if not a number
        return Node("operand", value=(field, operator, value))
    else:
        raise ValueError(f"Invalid condition format: {condition}")

def eval_rule_string(rule_string):
    """Evaluates a rule string recursively into AST nodes."""
    # Remove leading and trailing whitespace and outer parentheses
    rule_string = rule_string.strip()
    if rule_string.startswith("(") and rule_string.endswith(")"):
        rule_string = rule_string[1:-1].strip()
    
    tokens = re.split(r'\s+(AND|OR)\s+', rule_string)
    
    # If there are logical operators (AND/OR) in the tokens
    if len(tokens) > 1:
        operator = tokens[1]
        left_part = tokens[0].strip()
        right_part = tokens[2].strip()
        return Node("operator", left=create_rule(left_part), right=create_rule(right_part), value=operator)
    else:
        return parse_condition(tokens[0])

def create_rule(rule_string):
    """Creates an AST from a rule string."""
    return eval_rule_string(rule_string)


def combine_rules(rules):
    """Combines multiple ASTs into a single AST using AND operator."""
    combined_ast = None
    for rule in rules:
        ast = create_rule(rule)
        if combined_ast is None:
            combined_ast = ast
        else:
            combined_ast = Node("operator", left=combined_ast, right=ast, value="AND")
    return combined_ast


def evaluate_rule(ast, data):
    """Evaluates the AST against the input data."""
    if ast.type == "operand":
        field, operator, value = ast.value
        # Handle different comparison operators
        if operator == '=':
            return data[field] == value
        elif operator == '!=':
            return data[field] != value
        elif operator == '>':
            return data[field] > value
        elif operator == '<':
            return data[field] < value
        elif operator == '>=':
            return data[field] >= value
        elif operator == '<=':
            return data[field] <= value
    elif ast.type == "operator":
        left_result = evaluate_rule(ast.left, data)
        right_result = evaluate_rule(ast.right, data)
        if ast.value == "AND":
            return left_result and right_result
        elif ast.value == "OR":
            return left_result or right_result
    return False  # Default case if something goes wrong