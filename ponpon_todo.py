import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["nt"] + "\n"
    st.session_state["nt"] = ''

    todos.append(todo)
    functions.save_todos(todos)

st.title('PonPon Todo App')
st.subheader('This is my todo app.')
st.write('This app is to increase your productitivy.')

for index, todo in enumerate(todos) :
    checkbox = st.checkbox(todo, key=todo) # Better to match the key with the content to avoid errors
    if checkbox:
        todos.pop(index)
        functions.save_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="",placeholder= 'Add new todo...', on_change=add_todo, key= "nt")