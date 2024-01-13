import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("Pythonfile")
st.subheader("I am making significant difference no matter the odds")
st.write("This app is to increase your productivity..")

st.text_input(label="", placeholder="Add new todo.....",
              on_change=add_todo, key='new_todo')

for index, todo in enumerate (todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


# print("Oghenekevwe Samuel")
#
# st.session_state