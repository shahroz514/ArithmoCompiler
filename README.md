
# ArithmoCompiler

### Overview
**ArithmoCompiler** is a lightweight arithmetic expression compiler developed to validate and evaluate simple mathematical expressions. This project demonstrates core principles of compiler construction, including lexical analysis, syntax analysis, and expression evaluation. The compiler is integrated with a user-friendly front-end interface for seamless input and output handling.

### Features
- **Lexical Analysis**: Tokenizes input arithmetic expressions for validation.
- **Syntax Analysis**: Parses expressions to ensure correct syntax based on predefined grammar rules.
- **Expression Evaluation**: Computes results for valid expressions efficiently.
- **User Interface**: Front-end built using **HTML, CSS, and JavaScript**, allowing users to input expressions and view results directly.
- **Integration with Python**: The back-end compiler processes user inputs and generates outputs in real-time.

### Technology Stack
- **Front-End**: HTML, CSS, JavaScript (to accept user inputs and display outputs)
- **Back-End**: Python (compiler logic for lexical, syntax analysis, and evaluation)


### How It Works
1. **Input Expressions**: Users enter arithmetic expressions through the front-end interface.
2. **Lexical Analysis**: The compiler identifies tokens such as numbers, operators, and parentheses.
3. **Syntax Analysis**: Expressions are parsed based on grammar rules to validate correctness.
4. **Evaluation**: The compiler computes the result for valid expressions or highlights errors for invalid inputs.
5. **Output**: Results or error messages are displayed on the front-end interface.


### Installation
1. Clone the repository:
   
   git clone https://github.com/yourusername/ArithmoCompiler.git
   
2. Install the required dependencies:
   
   pip install -r requirements.txt
   
3. Run the application:
   
   python app.py
   
4. Open the interface in your browser:

   http://localhost:5000


### Folder Structure
- **`static/`**: Contains front-end assets (CSS, JavaScript).
- **`templates/`**: HTML files for the user interface.
- **`compiler/`**: Python modules for lexical analysis, syntax parsing, and evaluation.


### Future Enhancements
- Support for advanced arithmetic operations like exponents and modular arithmetic.
- Integration with visual parsing trees for better debugging and understanding.
- Extending grammar support for logical and relational operators.


### Contributions
Contributions are welcome! Feel free to fork the repository, suggest new features, or submit pull requests to improve the project.
