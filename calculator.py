import streamlit as st
import sympy as sp

# Set the page configuration
st.set_page_config(page_title="Scientific Calculator", page_icon="🧮", layout="centered")

# Title and description
st.title("🧮 Scientific Calculator")
st.write("A simple and stunning scientific calculator built with Streamlit.")

# Initialize session state for expression
if 'expression' not in st.session_state:
    st.session_state.expression = ""

# Function to update the expression
def update_expression(symbol):
    st.session_state.expression += str(symbol)

# Function to clear the expression
def clear_expression():
    st.session_state.expression = ""

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = sp.sympify(st.session_state.expression)
        st.session_state.expression = str(result)
    except sp.SympifyError:
        st.session_state.expression = "Error"

# Display the current expression
st.text_input("Expression", st.session_state.expression, key="display", disabled=True)

# Create calculator buttons
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

for row in buttons:
    cols = st.columns(4)
    for i, symbol in enumerate(row):
        if symbol == '=':
            cols[i].button(symbol, on_click=evaluate_expression)
        else:
            cols[i].button(symbol, on_click=update_expression, args=(symbol,))

# Clear button
st.button("C", on_click=clear_expression)

# Footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
        padding: 10px;
        background-color: #f1f1f1;
    }
    </style>
    <div class="footer">
        <p>Developed with ❤️ by GitHub Copilot</p>
    </div>
    """,
    unsafe_allow_html=True,
)