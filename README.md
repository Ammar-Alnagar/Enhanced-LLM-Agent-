# Enhanced LLM Agent 🧠🤖

This project showcases an advanced **LLM (Large Language Model) agent** capable of answering natural language questions using a variety of tools. The agent can perform searches, execute calculations, translate text, and more by leveraging APIs such as OpenAI, DuckDuckGo, Wolfram Alpha, and others.

## Key Features
- **Dynamic Tool Selection**: The agent intelligently chooses from a set of tools (search engines, math utilities, language tools, etc.) to answer complex queries.
- **Custom Prompt and Parsing**: Designed with a custom prompt template for effective reasoning and output parsing.
- **Modular Structure**: Tools are designed as independent modules, making it easy to extend and add more functionality.
- **Simple Web Interface**: A Flask-based web app that allows users to interact with the agent and receive results instantly.
- **LLM Chain**: Uses LangChain framework to integrate with OpenAI for generating responses.

## Tech Stack
- **Flask**: For the web interface and routing.
- **LangChain**: To structure interactions with the LLM and tools.
- **OpenAI**: As the core language model for answering questions.
- **Tools**: DuckDuckGo Search, Wolfram Alpha, Python REPL, Google Translator, TextBlob for sentiment analysis, etc.

## How It Works
1. **Frontend**: The web interface allows users to input questions.
2. **Backend**: Flask sends the queries to the LLM agent.
3. **Agent Processing**: The agent decides which tools to use based on the query.
4. **Response**: The agent returns the answer after processing, which is displayed on the web page.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/enhanced_llm_agent.git
    ```

2. Navigate into the project directory:

    ```bash
    cd enhanced_llm_agent
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables for `OPENAI_API_KEY` and `SECRET_KEY`:

    ```bash
    export OPENAI_API_KEY='your-openai-api-key'
    export SECRET_KEY='your-secret-key'
    ```

5. Run the application:

    ```bash
    python run.py
    ```

6. Open a browser and go to `http://127.0.0.1:5000/`.

## Example Usage

- **Ask a General Question**: "What’s the current weather in New York?"
- **Complex Calculation**: "Solve the integral of x^2 using Wolfram Alpha."
- **Translate Text**: "Translate 'Hello' to Spanish."

## Contributions
Contributions are welcome! If you'd like to add a new tool or improve the system, feel free to fork the repo and create a pull request.

---

**Author**: Ammar Alnagar
 