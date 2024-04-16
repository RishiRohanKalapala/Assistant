

# MyAIAssistant

MyAIAssistant is a Python-based AI assistant that provides information and assistance to users via a web interface.

## Description

MyAIAssistant leverages natural language processing (NLP) and various APIs to understand user queries and provide relevant responses. It includes features such as fetching information about rivers, retrieving data from external APIs, and interacting with users via a web interface.

## Features

- Fetch information about rivers in India based on user queries.
- Retrieve data from external APIs (e.g., Wikipedia) to gather information about rivers.
- Interactive web interface for users to interact with the AI assistant.
- Support for natural language processing to understand user queries.

## Setup

1. **Clone the Repository**: Clone this repository to your local machine using Git:

    ```bash
    git clone https://github.com/yourusername/myaiassistant.git
    ```

2. **Install Dependencies**: Navigate to the project directory and install the required dependencies:

    ```bash
    cd myaiassistant
    pip install -r requirements.txt
    ```

3. **Set Up API Keys**: Obtain API keys for any external APIs you plan to use (e.g., Wikipedia). Add these API keys to the appropriate configuration file (`config.py`).

4. **Run the Flask App**: Start the Flask application to run the AI assistant and web server:

    ```bash
    python assistant.py
    ```

    The web server will be accessible at `http://127.0.0.1:5000`.

## Usage

1. **Access the Web Interface**: Open a web browser and navigate to `http://127.0.0.1:5000`.
   
2. **Interact with the AI Assistant**: Enter your queries related to rivers in India in the input field and click the "Ask" button to receive responses from the AI assistant.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these guidelines:

- Fork the repository and create your branch from `main`.
- Make your changes and ensure all tests pass.
- Open a pull request with a detailed description of the changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

