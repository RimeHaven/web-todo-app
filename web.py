import streamlit as st
import functions

todos = functions.get_file()


def add_todo():
    new_todo = st.session_state["new_todo"]
    todos.append(new_todo + "\n")
    functions.write_file(todos)
    st.session_state["new_todo"] = ""


# st.title("My App")
st.subheader("Todo App")
# st.write("This App is just an exercise")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"cb{index}")
    if checkbox:
        todos.pop(index)
        functions.write_file(todos)
        del st.session_state[f"cb{index}"]
        st.rerun()

st.text_input(label="Add a new todo", placeholder="Add a new todo", on_change=add_todo,
              key="new_todo", label_visibility="collapsed")

# st.session_state
