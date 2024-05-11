import streamlit as st # type: ignore
import query
import upload
import list as list_module
import delete
import retrieve

# Set the title of the application
st.title("RAG PROJECT")

# Sidebar navigation
st.sidebar.title("Navigation")
choice = st.sidebar.radio(
    "Select an option",
    ["Query", "Upload", "List", "Delete", "Retrieve"]
)

# Handle the choice
if choice == "Query":
    query_function_result = query.run_query()
    st.write("Query result:", query_function_result)

elif choice == "Upload":
    upload_function_result = upload.run_upload()
    st.write("Upload result:", upload_function_result)

elif choice == "List":
    list_function_result = list_module.run_list()
    st.write("List result:", list_function_result)

elif choice == "Delete":
    delete_function_result = delete.run_delete()
    st.write("Delete result:", delete_function_result)

elif choice == "Retrieve":
    retrieve_function_result = retrieve.run_retrieve()
    st.write("Retrieve result:", retrieve_function_result)
