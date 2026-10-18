# Data Analysis AI Agent

A lightweight **Streamlit** app that lets users upload a CSV file and ask questions about it in natural language.

The app combines **Pandas** for data handling, **LangChain** for agent orchestration, **Groq** for the LLM, and **LangGraph memory** for basic conversation continuity.

---

## What it does

- Upload a CSV file
- Preview the dataset
- Ask questions in chat
- Inspect columns, row counts, and data types
- Filter rows using a condition
- Run simple Pandas expressions for analysis

---

## Features

- **CSV upload and preview**
- **Chat-based interaction**
- **Dataset inspection tool**
- **Row filtering tool**
- **Pandas expression analysis tool**
- **Session-based chat history**
- **Simple local setup**

---

## Example Questions

You can ask questions like:

- What columns are in this file?
- Show me the first few rows
- Filter rows where `Age > 30`
- What is the average salary?
- How many unique cities are in the dataset?

---

## Tech Stack

- **Python**
- **Streamlit**
- **Pandas**
- **LangChain**
- **LangGraph**
- **Groq API**
- **python-dotenv**

---

## How It Works

1. The user uploads a CSV file.
2. The file is read into a Pandas `DataFrame`.
3. The agent uses tools to inspect or analyze the data.
4. The response is shown in the chat UI.
5. Chat messages are stored in `st.session_state` for the current session.

---

## Project Structure

```text
.
├── app.py
├── README.md
└── .env
```

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/data-analysis-ai-agent.git
cd data-analysis-ai-agent
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows**
```bash
.venv\Scripts\activate
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Add your API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_api_key_here
```

### 6. Run the app

```bash
streamlit run app.py
```

---

## Usage

1. Start the app
2. Upload a `.csv` file
3. Ask a question in the chat box
4. Read the assistant’s response

---

## Notes

- `get_data_info()` returns dataset shape, column names, data types, and sample rows
- `filter_tool()` uses `df.query()` to filter rows
- `analyze_data()` uses `eval()` to run Pandas expressions

---

## Limitations

This project is intentionally small and focused.

- `eval()` should be replaced with a safer approach before production use
- The dataframe is stored globally, so it is not suitable for multi-user deployment as-is
- The app is designed for lightweight CSV analysis, not large-scale data processing
- There is no authentication or file validation layer yet

---

## Future Improvements

Possible next steps:

- safer expression handling instead of `eval()`
- per-user session isolation
- support for multiple uploads
- chart and visualization support
- improved error handling
- export chat history

---

## Why I Built This

I built this project to combine practical Python data handling with LLM-powered interaction in a small, useful application. It demonstrates how to build a focused AI tool that is simple, readable, and easy to extend.

---

## License

Add a license if you plan to publish this repository publicly.