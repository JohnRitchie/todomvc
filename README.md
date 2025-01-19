# TodoMVC Testing Project

This project is a demonstration of testing the [TodoMVC React application](https://todomvc.com/examples/react/dist/) using Python, Playwright, and the Page Object Model (POM) pattern. The tests verify key functionalities of the TodoMVC app, such as adding, marking as completed, and deleting TODO items, while maintaining clean code organization and reusability.

## Project Structure

```
├── helpers.py                # Utility functions for the project
├── requirements.txt          # List of dependencies for the project
├── pages/                    # Page Object Model classes
│   └── todomvc_page.py       # POM class for TodoMVC interactions
├── tests/                    # Test files and configurations
│   ├── conftest.py           # Pytest fixtures
│   └── test_todomvc.py       # Main test file
```

### Key Components
- **helpers.py**: Contains utility functions.
- **requirements.txt**: Contains Python dependencies required for the project.
- **pages/todomvc_page.py**: Implements the POM class, `TodoMVCPage`, encapsulating interactions with the TodoMVC app.
- **tests/conftest.py**: Defines Pytest fixtures for setting up the browser and managing context.
- **tests/test_todomvc.py**: Contains the primary test class that verifies the functionality of the TodoMVC app.

## Installation

1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install Playwright dependencies:
   ```bash
   playwright install
   ```

## Running Tests

1. Run the tests with Pytest:
   ```bash
   pytest --alluredir=allure-results
   ```

2. To run tests in headless mode, use the `--headless` flag:
   ```bash
   pytest --alluredir=allure-results --headless
   ```

3. To generate and view an Allure report:
   ```bash
   allure serve
   ```

## Test Scenarios

The primary test, `test_todomvc`, validates the following scenarios:

1. Adding a TODO item and verifying its presence in the list.
2. Adding another TODO item with a different date and verifying its presence.
3. Marking a TODO item as completed and verifying its completion status.
4. Deleting a TODO item and verifying its removal.

## Additional Features

- **Allure Reporting**: Provides detailed test reports with screenshots and step-by-step analysis.
- **Video and Trace Recording**: Records video and traces of test execution for debugging purposes.

## Troubleshooting

- If tests fail, ensure that:
  1. Dependencies are installed correctly.
  2. The Playwright browser dependencies are up-to-date.
  3. The internet connection is stable (required for accessing the TodoMVC app).

- Check the `screenshots/` directory and `videos/` folder for visual debugging.

## Contribution

Feel free to open issues or submit pull requests to improve the project. 

## License

This project is licensed under the MIT License. See the LICENSE file for details.
