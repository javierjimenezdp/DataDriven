Sure, here's the README for your Selenium and Python automation project in English:

---

# Automation with Selenium and Python

This project focuses on test automation using Selenium WebDriver and Python. It utilizes the Page Object methodology to enhance code maintainability and reusability in automating specific workflows, such as login in a web application.

## Author

- **Author**: Javier Jiménez
- **Role**: QA Analyst
- **Contact**: 
  - Email: [ing.javierdavidjp@gmail.com](mailto:ing.javierdavidjp@gmail.com)
  - LinkedIn: [Javier Jiménez on LinkedIn](https://www.linkedin.com/in/javierjim%C3%A9nez1021/)

## System Requirements

- Python 3.x
- Selenium WebDriver
- Compatible web browser (e.g., Chrome, Firefox)

## Installation

1. **Install Python**:
   - Download and install Python from [python.org](https://www.python.org).

2. **Setup virtual environment** (optional but recommended):
   ```bash
   pip install virtualenv
   virtualenv env
   .\env\Scripts\activate  # Windows
   source env/bin/activate  # macOS/Linux
   ```

3. **Install Selenium**:
   ```bash
   pip install selenium
   ```

4. **WebDriver Setup**:
   - Download the WebDriver for your desired browser and ensure it's in the system PATH.

## Project Structure

- **Functions/funciones.py**: Contains utility functions and general Selenium methods.
- **Excel/Funciones_ex.py**: Specific functions for interacting with Excel files.
- **Functions/Page_login.py**: Implementation of Page Objects for login pages.
- **LoginQA/ToolsLogin.py**: Main test file using unittest for test execution.

## Automation and Page Objects

This project employs the Page Object methodology to abstract the UI logic. Each web page of the application has its own Page Object class, facilitating easier maintenance and code reuse.

## Data-Driven Testing

Data-Driven Testing is utilized to execute tests with different datasets, using Excel files to store test data.

## Running Tests

To run the tests, use `unittest`:

```bash
python -m unittest LoginQA.ToolsLogin
```

## Contributing

If you wish to contribute to this project, follow these steps:

1. Fork the repository and clone it locally.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and commit (`git commit -am 'Add new feature'`).
4. Push the branch (`git push origin feature/new-feature`).
5. Create a new Pull Request.

## Known Issues

- Common issues encountered during development and test execution.
- Recommended solutions to address specific technical challenges.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
