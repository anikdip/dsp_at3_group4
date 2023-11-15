import streamlit as st

import pandas as pd

from tab_date.logics import DateColumn

def display_tab_date_content(file_path=None, df=None):
    """
    --------------------
    Description
    --------------------
    -> display_tab_date_content (function): Function that will instantiate tab_date.logics.DateColumn class, save it into Streamlit session state and call its tab_date.logics.DateColumn.find_date_cols() method in order to find all datetime columns.
    Then it will display a Streamlit select box with the list of datetime columns found.
    Once the user select a datetime column from the select box, it will call the tab_date.logics.DateColumn.set_data() method in order to compute all the information to be displayed.
    Then it will display a Streamlit Expander container with the following contents:
    - the results of tab_date.logics.DateColumn.get_summary() as a Streamlit Table
    - the graph from tab_date.logics.DateColumn.histogram using Streamlit.altair_chart()
    - the results of tab_date.logics.DateColumn.frequent using Streamlit.write
 
    --------------------
    Parameters
    --------------------
    -> file_path (str): File path to uploaded CSV file (optional)
    -> df (pd.DataFrame): Loaded dataframe (optional)

    --------------------
    Returns
    --------------------
    -> None

    """

    date_analysis = DateColumn(file_path, df)

    # Find the list of date column
    date_analysis.find_date_cols()
    # Show the date columns in dropdown list
    date_analysis_column = st.selectbox("Which datetime column do you want to explore", date_analysis.cols_list)
    # Set all datas
    date_analysis.set_data(date_analysis_column)

    # Show some informatics data into table
    df = pd.DataFrame(
        [

            {"Description":"Number of Unique Values", "Value":str(date_analysis.n_unique)},
            {"Description":"Number of Missing Values", "Value":str(date_analysis.n_missing)},
            {"Description":"Number of Weekend Dates", "Value":str(date_analysis.n_weekend)},
            {"Description":"Number of Weekdays Dates", "Value":str(date_analysis.n_weekday)},
            {"Description":"Number of Days in Future", "Value":str(date_analysis.n_future)},
            {"Description":"Number of Rows with 1900-01-01", "Value":str(date_analysis.n_empty_1900)},
            {"Description":"Number of Rows with 1970-01-01", "Value":str(date_analysis.n_empty_1970)},
            {"Description":"Minimum Value", "Value":str(date_analysis.col_min)},
            {"Description":"Maximum Value", "Value":str(date_analysis.col_max)}
        ])

    st.table(df)

    # Show the barchart of the data column
    st.bar_chart(date_analysis.barchart)

    # Display a table listing the occurrences and percentage of the top 20 most frequent values
    st.markdown("*Most Frequent Values*")
    st.write(date_analysis.frequent)
    
