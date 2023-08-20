# Ami Coding Pari Na Django Project

Welcome to the "Ami Coding Pari Na" Django project. 

## Project Overview

### User Authentication

The project includes user authentication features that allow users to register and log in securely.

### Khoj - The Search

The core of the project is the "Khoj - The Search" feature. This feature allows users to:

1. Take input comma-separated integers.
2. Search for a specific integer.
3. Check if the search value is present in the input values return True else False.
4. Store the input values in a sorted descending order in the database.


## Installation and Setup

To run the project locally, follow these steps:

1. Clone the repository:
```
https://github.com/rifatjamil54/Ami-Coding-Pari-Na.git
```


2. Navigate to the project directory and Create a virtual environment:
```
cd Ami-Coding-Pari-Na
python -m venv venv 

```


4. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

5. Install dependencies, Migrate database, Run development server
```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
6. Access the project in your web browser: http://127.0.0.1:8000/

## API Endpoint
7. To allow token-based authenticated users to view their details via an API request.
### Get All Input Values
This API documentation provides details about the "Get All Input Values" endpoint. To retrieve all input values entered by a user within a specified time range.

Then Generate the Token

Make a GET request to the API endpoint and include the token in the Authorization header.
Endpoint: `/api/get-all-input-values/`

Parameters:
- `start_datetime` (inclusive) - Start of the time range in YYYY-MM-DD HH:MM:SS format.
- `end_datetime` (inclusive) - End of the time range in YYYY-MM-DD HH:MM:SS format.

Example Request:

`curl -H "Authorization: Token YOUR_TOKEN_HERE" "http://127.0.0.1:8000/api/?start_datetime=2023-08-14T13:00:00Z&end_datetime=2023-08-15T20:20:00Z"`

Example Response:
`{
    "status": "success",
    "user_id": 1,
    "payload": [
        {
            "input_values":"7, 7, 6, 4, 3, 1",
            "timestamp":"2023-08-14 13:56"
        },
        {
            "input_values":"9, 9, 5, 4, 4, 1",
            "timestamp":"2023-08-14 13:56"
        }
    ]
}
`
## Demo

#### Khoj the Page
![K_S](https://raw.githubusercontent.com/rifatjamil54/Ami-Coding-Pari-Na/main/demo/k_s.gif)

#### Generat Token
![genetar_token](https://raw.githubusercontent.com/rifatjamil54/Ami-Coding-Pari-Na/main/demo/g_token.gif)


