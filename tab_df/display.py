import streamlit as st
from tab_df.logics import Dataset

def display_tab_df_content(file_path):
    """
    Display the content of a DataFrame from an uploaded CSV file.
   
    Parameters:
        file_path (str): File path to uploaded CSV file.
    """
    # Create an instance of the Dataset class
    dataset = Dataset(file_path)
   
    # Compute summary and table information
    dataset.set_data()

    #set the session
    if not dataset.is_df_none():
        st.session_state.dataset = dataset
        st.session_state.df = dataset.df
   
    # Display summary in an expander container
    with st.expander("Summary"):
        # Display the results of get_summary() as a Streamlit Table
        st.table(dataset.get_summary())
        # Display the results of table using Streamlit.write()
        st.write(dataset.table)
   
    # Display rows in an expander container
    with st.expander("Display Rows"):
        # Slider to select the number of rows to display
        num_rows_to_display = st.slider("Number of Rows to Display", 5, 50, 5)
        # Radio button to choose the logic for displaying rows
        display_logic = st.radio("Display Logic", ["Head (First Rows)", "Tail (Last Rows)", "Sample (Random Sample)"])
       
        st.write("Displayed Data:")
        if display_logic == "Head (First Rows)":
            st.dataframe(dataset.get_head(num_rows_to_display))
        elif display_logic == "Tail (Last Rows)":
            st.dataframe(dataset.get_tail(num_rows_to_display))
        else:
            st.dataframe(dataset.get_sample(num_rows_to_display))
