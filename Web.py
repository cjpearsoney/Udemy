import streamlit as st
import functions


todos = functions.get_tados()

def add_todo():
    todo = st.session_state['new_todo']+"\n"
    todos.append(todo.title())
    functions.write_tados(todos)

st.title("My ToDo App")
st.subheader("This is my to-do app new")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_tados(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="", placeholder="Enter a todo...",
              on_change=add_todo, key = 'new_todo')
