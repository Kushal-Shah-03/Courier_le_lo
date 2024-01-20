<h1>Courier IIIT-H</h1>


- [Project Overview](#project-overview)
- [Setup](#setup)
- [Backend Setup](#backend-setup)
    - [Dependencies](#dependencies)
    - [Virtual Environment](#virtual-environment)
    - [Installation](#installation)
    - [Running the flask server](#running-the-flask-server)
- [Contributing](#contributing)

# Project Overview

This project is our attempt at improving the [`courier.iiit.ac.in`](courier.iiit.ac.in) website

# Setup

To get started with the project, clone the repository to your local machine:

```bash
git clone git@github.com:Kushal-Shah-03/Courier_le_lo.git

cd Courier_le_lo/
```

# Backend Setup

The backend of this project is located in the `backend/` folder.

### Dependencies

The project uses Python for the backend. Ensure you have Python installed on your system.

- Python version: 3.10.12

### Virtual Environment

It's recommended to use a virtual environment to manage dependencies. Create and activate a virtual environment using the following commands:

```bash
# Navigate to the backend folder
cd backend/

# Unix / MacOS
# Create a virtual environment
python3 -m venv name-of-env

# Activate the virtual environment
source name-of-env/bin/activate

# Windows (Why ?)
# Create a virtual environment
python -m venv name-of-env

# Activate the virtual environment
.\name-of-env\Scripts\activate
```

### Installation

Install project dependencies using the provided `requirements.txt` file:

```bash
# Make sure you are in the backend folder and the virtual environment is activated
pip install -r requirements.txt
```

### Running the flask server

```bash
# Run the backend server
python app.py
```

# Contributing

If you'd like to contribute to the project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request
