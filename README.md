# BizBot 🤖

[![Langchain](https://img.shields.io/badge/langchain-v0.3.0-blue)](https://github.com/hwchase17/langchain) 
[![Pinecone](https://img.shields.io/badge/pinecone-v5.1.0-yellow)](https://www.pinecone.io/) 
[![Streamlit](https://img.shields.io/badge/streamlit-v1.36.0-brightgreen)](https://streamlit.io/)

BizBot is an advanced chatbot application designed to answer user queries based on company data. It utilizes a combination of AI technologies and data retrieval methods to provide accurate and relevant responses. The application is built using Streamlit for the web interface, and it integrates with Pinecone for vector-based document retrieval and Cohere for natural language processing.

## Features

- **Interactive Chat Interface**: Users can interact with the chatbot through an intuitive web interface built with Streamlit.
- **Data Integration**: Supports PDF file uploads for dynamic updates to the knowledge base.
- **AI-Driven Responses**: Uses Cohere for generating responses based on the context provided by user queries.
- **Efficient Data Retrieval**: Leverages Pinecone for efficient vector-based search and retrieval of relevant documents.

## Technologies Used

- **Streamlit**: For building the web interface.
- **Pinecone**: For vector-based document retrieval.
- **Cohere**: For generating natural language responses.
- **Python Libraries**: Includes `langchain`, `pinecone-client`, `cohere`, and others for various functionalities.

## Getting Started

### Prerequisites

- Python 3.10+
- Docker (optional, for containerization)
- Access to Pinecone and Cohere API keys
  
## Installation and Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/chiruu12/BizBot.git
    ```

2. **Navigate to the Project Directory**:
    ```bash
    cd BizBot
    ```
3. **Set up environment variables**:
    Create a `.env` file in the project root with the following content:
    ```env
    PINECONE_API_KEY=<your_pinecone_api_key>
    COHERE_API_KEY=<your_cohere_api_key>
    PINECONE_INDEX_NAME=<your_pinecone_index_name>
    FOLDER_PATH=docs
    ```
4. **Install Required Packages**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Application**:
    ```bash
    streamlit run ui.py
    ```


# Using Docker to Install and Run the Application

### Prerequisites
- Make sure Docker is installed on your system. If not, [install Docker](https://docs.docker.com/get-docker/) for your operating system.

### Steps to Run the Application with Docker

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/chiruu12/BizBot.git
    ```

2. **Navigate to the Project Directory**:
    ```bash
    cd BizBot
    ```

3. **Build the Docker Image**:
   Ensure that the Dockerfile is located in the root directory of your project. Build the Docker image using the following command:
    ```bash
    docker build -t bizbot .
    ```
    
4. **Run the Docker Container**:
   After successfully building the image, run the container using:
    ```bash
    docker run -d -p 8501:8501 bizbot
    ```
   This command will:
   - Start the container in detached mode (`-d`).
   - Map port `8501` (Streamlit's default port) from the container to port `8501` on your host machine.

5. **Access the Application**:
   Open your web browser and go to: http://localhost:8501 

## Usage

- **Upload PDFs**: Users can upload PDF files through the sidebar to update the chatbot’s knowledge base.
- **Ask Questions**: Type your questions into the chat interface to get responses based on the provided data.

## Fake Company Data

For demonstration purposes, the project includes fake company data generated using AI. This data is used to simulate realistic interactions with the chatbot.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
