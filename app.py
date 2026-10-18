import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()

df: pd.DataFrame = None

def set_df(_df:pd.DataFrame):
    global df
    df = _df

if "messages" not in st.session_state:
    st.session_state.messages = []

# print(df.head())

@tool
def get_data_info():
    """Get columns, data types, shape, and first 5 rows of the uploaded csv file"""

    if df is None:
        return "No CSV loaded"

    return f"""
    Shape: {df.shape},
    Columns & Types: {df.dtypes.to_string()},
    First 5 rows: {df.head().to_string()}
    """

def filter_tool(condition: str):
    """
        Filter rows using a pandas query condition
        Example: 'Age > 30 and Department == 'Engineering''
    """

    if df is None:
       return "No CSV loaded"

    try:
        result = df.query(condition)
        return f"Found :{len(result)} rows: {result.to_string()}"
    except Exception as e:  # noqa: BLE001
        return f"Error: {e}"

def analyze_data(expression: str):
    """
        Run a pandas expression on the dataframe(referred to as df)
        Examples:
            df['salary'].mean()
            df.groupby('Department')['Salary'].mean()
            df['City'].value_counts()
    """

    if df is None:
        return "CSV not loaded"

    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"


all_tools = [get_data_info, filter_tool, analyze_data]

llm = ChatGroq(model="openai/gpt-oss-20b")

system_prompt = """
You are a Data Analyst assisstant. You help users explore and analyse CSV data.
Use the Tools to answer questions:
    - get_data_info  -> see columns, types and sample rows
    - filter_tool    -> filter rows by condition
    - analyze_data   -> run pandas expressions for stats and aggregations
Always use get_data_info first if you are unsure about the column names 
"""

MEMORY = InMemorySaver()

agent = create_agent(
    model = llm,
    tools= all_tools,
    system_prompt= system_prompt,
    checkpointer= MEMORY
)

def run_agent(query: str):
    
    res = agent.invoke(
        {"messages":[{"role": "user", "content": query}]},
        {"configurable": {"thread_id": "1"}}
        )

    answer = res["messages"][-1].content
    return answer

### lets build our UI

st.header('Data Analysis(CSV) AI Agent')
file = st.file_uploader(label="Select your csv file", type='csv')
if file:
    df = pd.read_csv(file)
    set_df(df)
    st.dataframe(df.head())
    st.success(f"Loaded {df.shape[0]} rows.")

for msg in st.session_state.messages:
    role = msg['role']
    content = msg['content']
    st.chat_message(role).markdown(content)

query = st.chat_input("Ask Anything...")
if query:
    st.chat_message("user").markdown(query)
    st.session_state.messages.append({'role':'user', 'content': query})

    res = run_agent(query)

    st.chat_message("ai").markdown(res)
    st.session_state.messages.append({'role': 'ai', 'content': res})