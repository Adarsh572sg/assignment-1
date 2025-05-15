# Flask Age Verification App

This is a simple Flask web application that verifies a user's eligibility based on their age. The application takes a user's name and age as input and displays a message indicating whether they are eligible or not.

## Features

- Accepts user input for name and age through a web form.
- Validates the input to ensure the age is a valid number.
- Displays personalized messages based on the age provided.
- Provides real-time feedback for invalid input.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Python](https://www.python.org/downloads/) 3.6 or higher
- [Flask](https://flask.palletsprojects.com/) web framework

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Adarsh572sg/assignment-1.git
   cd assignment-1
   ```

2. Install the required Python packages:

   ```bash
   pip install flask
   ```

## Usage

1. Run the Flask application:

   ```bash
   python app.py
   ```

2. Open your web browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

3. Enter your name and age in the form, then submit to see the result.

## Application Logic

- If the age is less than 17, the application will display: `"Hello, [Name]! Age restriction: You are Not Allowed"`
- If the age is 17 or above, the application will display: `"Hello, [Name]! Permission Granted: You are Eligible"`
- If the age is invalid (not a number), the application will display: `"Please enter a valid age"`

## Project Structure

```
assignment-1/
├── app.py          # Main application file
├── index.html      # HTML template for the web form
└── README.md       # Documentation for the project
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
