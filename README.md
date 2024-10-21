# Rule Engine with AST - Project Documentation

## Project Overview

The **Rule Engine with AST (Abstract Syntax Tree)** is a 3-tier application designed to determine user eligibility based on various attributes such as age, department, income, and experience. The system allows for the dynamic creation, combination, and modification of rules, which are represented as ASTs. These rules are stored in a MySQL database, and users can evaluate data against these rules using a simple API.

### Key Features

- **Dynamic Rule Creation**: Supports defining custom rules using simple strings.
- **Rule Combination**: Allows combining multiple rules into a single AST.
- **Eligibility Evaluation**: Evaluates user data against the rules to check eligibility.
- **MySQL Database**: Stores rules and evaluation metadata.
- **API-based Design**: Provides functions to create rules, combine rules, and evaluate them.

---

## How to Set Up and Run

### Prerequisites

- Python 3.x
- MySQL
- `mysql-connector-python` library
- `pytest` for testing

### Step-by-Step Setup

1. **Clone the Repository**:
   ```bash
   git clone <your-repository-url>
   cd rule_engine_ast

### Set Up a Virtual Environment
  ```bash
  python -m venv venv
  .\venv\Scripts\activate   # Windows

  
