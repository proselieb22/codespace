# Your Desktop Reminders

## Overview

Your Desktop Reminders is a task manager application designed to facilitate task creation, viewing, deletion, and email notifications for task updates. It consists of two primary files:

1. **project.py**: Contains the core functionalities of the reminder application.
2. **test_project.py**: Includes unit tests to validate the project's functionalities.

## Description

This application offers a simple and efficient way to manage tasks. Users can create, view, and delete tasks, and receive email notifications for task-related actions. It comprises the following components:

### 1. `project.py`

#### 1.1 Classes

- **Task**: Represents a task entity with properties such as name, description, and due date.

  - **Methods**:
    - `__init__(self, name, description, due_date=None)`: Initializes the task object.
    - `__str__(self)`: Returns a formatted string representation of the task.

- **Functions**:

  - `rtask(n, d)`: Returns a new Task instance with the provided name and description.
  - `email_alert(body, to)`: Sends an email alert with the specified body to the given email address.
  - `create_task(to_email="test@example.com")`: Creates a new task with user input and sends an email notification.
  - `view_task(name)`: Displays information about a specific task.
  - `delete_task(name, to_email="test@example.com")`: Deletes a task and sends an email notification.
  - `main()`: The main function serving as the application's entry point.

#### 1.2 Usage

- Execute `main()` to interact with the application.
- Utilize the menu options for task creation, viewing, or deletion.
- Email notifications will be triggered for task creation and deletion.

### 2. `test_project.py`

#### 2.1 Unit Tests

- `test_Task()`: Validates the functionality of the Task class.
- `test_view_task()`: Tests the ability to view an existing task.
- `test_email_alert()`: Verifies the email alert functionality.

#### 2.2 Running Tests

- Use `pytest test_project.py` to execute the unit tests.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/YourDesktopReminders.git
   cd YourDesktopReminders
Install dependencies:
pip install -r requirements.txt
Create a .env file with the following variables:
APP_EMAIL=your_email@gmail.com
APP_PASSWORD=your_email_password
Replace your_email@gmail.com and your_email_password with your email credentials.

Run the application:
python project.py
