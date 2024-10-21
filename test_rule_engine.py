# test_rule_engine.py
from rule_engine import create_rule, combine_rules, evaluate_rule

def test_create_rule():
    rule = "(age > 30 AND department = 'Sales')"
    ast = create_rule(rule)
    assert ast.type == "operator"
    assert ast.value == "AND"

def test_combine_rules():
    rule1 = "(age > 30 AND department = 'Sales')"
    rule2 = "(salary > 50000)"
    combined_ast = combine_rules([rule1, rule2])
    assert combined_ast.type == "operator"
    assert combined_ast.value == "AND"

def test_evaluate_rule():
    rule = "(age > 30 AND department = 'Sales')"
    ast = create_rule(rule)
    data = {"age": 35, "department": "Sales", "salary": 60000}
    assert evaluate_rule(ast, data) == True

    data = {"age": 25, "department": "Marketing", "salary": 60000}
    assert evaluate_rule(ast, data) == False