# Rule Engine with AST

## Overview
The Rule Engine with AST (Abstract Syntax Tree) application is designed to evaluate user eligibility based on various attributes, such as age, department, income, and spending. It allows for the dynamic creation, combination, and modification of conditional rules using an AST representation.

## Table of Contents
- [Installation](#installation)
- [Setup and Running the Application](#setup-and-running-the-application)
- [API Design](#api-design)
- [Data Structure](#data-structure)
- [Database Design](#database-design)
- [Test Cases](#test-cases)
- [Design Choices](#design-choices)
- [Contribution](#contribution)
- [License](#license)

## Installation

### Prerequisites
- Python 3.9 or higher
- pip (Python package installer)
- Docker (optional, for containerization)

### Dependencies
Install the required Python packages by running:

```bash
pip install -r requirements.txt

# Rule Engine with AST

## Overview
The Rule Engine with AST (Abstract Syntax Tree) application is designed to evaluate user eligibility based on various attributes, such as age, department, income, and spending. It allows for the dynamic creation, combination, and modification of conditional rules using an AST representation.

## Table of Contents
- [Installation](#installation)
- [Setup and Running the Application](#setup-and-running-the-application)
- [API Design](#api-design)
- [Data Structure](#data-structure)
- [Database Design](#database-design)
- [Test Cases](#test-cases)
- [Design Choices](#design-choices)
- [Contribution](#contribution)
- [License](#license)

## Installation

### Prerequisites
- Python 3.9 or higher
- pip (Python package installer)
- Docker (optional, for containerization)

### Dependencies
Install the required Python packages by running:

```bash
pip install -r requirements.txt
Setup and Running the Application
Clone the repository:

bash
Copy code
git clone <your-repo-url>
cd <your-repo-name>
Start the Flask server:

bash
Copy code
python app.py
API Testing: Use Postman or any other API testing tool to interact with the API endpoints.

Docker Setup (Optional)
If you wish to run the application inside a Docker container, follow these steps:

Build the Docker image:

bash
Copy code
docker build -t rule-engine .
Run the Docker container:

bash
Copy code
docker run -p 5000:5000 rule-engine
API Design
Endpoints
Create Rule

Endpoint: POST /create_rule
Description: Accepts a rule string and returns the corresponding AST representation.
Request Body:
json
Copy code
{
  "rule_string": "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
}
Combine Rules

Endpoint: POST /combine_rules
Description: Combines multiple rule strings into a single AST.
Request Body:
json
Copy code
{
  "rules": [
    "((age > 30 AND department = 'Sales'))",
    "((age < 25 AND department = 'Marketing'))"
  ]
}
Evaluate Rule

Endpoint: POST /evaluate_rule
Description: Evaluates a rule against provided user data.
Request Body:
json
Copy code
{
  "data": {
    "age": 35,
    "department": "Sales",
    "salary": 60000,
    "experience": 3
  }
}
Data Structure
Node Structure
The AST is represented by a Node class with the following fields:

type: String indicating the node type ("operator" for AND/OR, "operand" for conditions).
left: Reference to another Node (left child).
right: Reference to another Node (right child for operators).
value: Optional value for operand nodes (e.g., number for comparisons).
Database Design
Database Choice
Database: SQLite (for simplicity in development)
Schema Example:
sql
Copy code
CREATE TABLE rules (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rule_string TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
Test Cases
Test the API endpoints using Postman or automated test scripts. Sample test cases include:

Creating rules and verifying AST representation.
Combining multiple rules and ensuring the resulting AST reflects combined logic.
Evaluating rules against sample user data.
Design Choices
Architecture: The application follows a 3-tier architecture consisting of UI, API, and Backend.
Error Handling: Basic error handling for invalid rule strings and formats has been implemented.
Flexibility: The application allows for dynamic modification of existing rules.
Contribution
Contributions are welcome! Please fork the repository and submit a pull request with your changes.
