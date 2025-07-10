# LangChain AI Agent

This project is an AI-powered research assistant built using LangChain, OpenAI, and community tools. It can answer questions, perform web searches, and save structured research outputs to a file.

## Features
- Conversational research assistant using OpenAI's GPT models
- Web search integration (DuckDuckGo)
- Structured output parsing with Pydantic
- Save research results to a text file

## Requirements
- Python 3.8+
- API key for OpenAI (set as `OPENAI_API_KEY` in a `.env` file)

## Setup
1. **Clone the repository**
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Set up your environment variables:**
   - Create a `.env` file in the project root:
     ```env
     OPENAI_API_KEY=your_openai_api_key_here
     ```

## Usage
Run the main script:
```sh
python LangCHain_Ai_Agen.py
```
- The assistant will prompt you for a query.
- It will use web search tools and language models to answer.
- Results can be saved to a text file using the provided tool.

## Project Structure
- `LangCHain_Ai_Agen.py` — Main entry point for the AI agent
- `tools.py` — Definitions for web search and file-saving tools
- `requirements.txt` — Python dependencies

## Extending
- Add more tools in `tools.py` and include them in the `tools` list in the main script.
- Customize the prompt or output parser as needed.

## Notes
- The DuckDuckGo search tool uses the latest `ddgs` backend (see warning in logs).
- Wikipedia tool is commented out due to compatibility issues in some versions.

## License
MIT License (add your own if different) 