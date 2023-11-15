import pandas as pd
import altair as alt
from dateutil.parser import parse
import streamlit as st
from datetime import datetime

class DateColumn:
    """
    --------------------
    Description
    --------------------
    -> DateColumn (class): Class that manages a column from a dataframe of datetime data type

    --------------------
    Attributes
    --------------------
    -> file_path (str): Path to the uploaded CSV file (optional)
    -> df (pd.Dataframe): Pandas dataframe (optional)
    -> cols_list (list): List of columns names of dataset that are text type (default set to empty list)
    -> serie (pd.Series): Pandas serie where the content of a column has been loaded (default set to None)
    -> n_unique (int): Number of unique value of a serie (optional)
    -> n_missing (int): Number of missing values of a serie (optional)
    -> col_min (int): Minimum value of a serie (optional)
    -> col_max (int): Maximum value of a serie (optional)
    -> n_weekend (int): Number of times a serie has dates falling during weekend (optional)
    -> n_weekday (int): Number of times a serie has dates not falling during weekend (optional)
    -> n_future (int): Number of times a serie has dates falling in the future (optional)
    -> n_empty_1900 (int): Number of times a serie has dates equal to '1900-01-01' (optional)
    -> n_empty_1970 (int): Number of times a serie has dates equal to '1970-01-01' (optional)
    -> barchart (int): Altair barchart displaying the count for each value of a serie (optional)
    -> frequent (int): Dataframe containing the most frequest value of a serie (optional)

    """
    def __init__(self, file_path=None, df=None):
        self.file_path = file_path
        self.df = df
        self.cols_list = []
        self.serie = None
        self.n_unique = None
        self.n_missing = None
        self.col_min = None
        self.col_max = None
        self.n_weekend = None
        self.n_weekday = None
        self.n_future = None
        self.n_empty_1900 = None
        self.n_empty_1970 = None
        self.barchart = alt.Chart()
        self.frequent = pd.DataFrame(columns=['value', 'occurrence', 'percentage'])
    
    def find_date_cols(self):
        """
        --------------------
        Description
        --------------------
        -> find_date_cols (method): Class method that will load the uploaded CSV file as Pandas DataFrame and store it as attribute (self.df) if it hasn't been provided before.
        Then it will find all columns of datetime data type. If it can't find any datetime then it will look for all columns of text time. Then it will store the results in the relevant attribute (self.cols_list).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        def is_valid_date(col, date):
            if date:
                try:
                    parse(date)
                    # self.df[col] = pd.to_datetime(self.df[col])
                    self.cols_list.append(col)
                    return True
                except:
                    return False
            return False

        for col in self.df:
            is_valid_date(col, self.df[col].iloc[0])
        

    def set_data(self, col_name):
        """
        --------------------
        Description
        --------------------
        --------------------
        Description
        --------------------
        -> set_data (method): Class method that sets the self.serie attribute with the relevant column from the dataframe and then computes all requested information from self.serie to be displayed in the Date section of Streamlit app 

        --------------------
        Parameters
        --------------------
        -> col_name (str): Name of the text column to be analysed

        --------------------
        Returns
        --------------------
        -> None
        """
        st.session_state.date_column = col_name
        self.convert_serie_to_date()
        self.set_unique()
        self.set_missing()
        self.set_min()
        self.set_max()
        self.set_weekday()
        self.set_weekend()
        self.set_future()
        self.set_empty_1900()
        self.set_empty_1970()
        self.set_barchart()
        self.set_frequent()
        

    def convert_serie_to_date(self):
        """
        --------------------
        Description
        --------------------
        -> convert_serie_to_date (method): Class method that convert a Pandas Series to datetime data type and store the results in the relevant attribute (self.serie).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        self.serie = pd.to_datetime(self.df[st.session_state.date_column], format='mixed')
        

    def is_serie_none(self):
        """
        --------------------
        Description
        --------------------
        -> is_serie_none (method): Class method that checks if self.serie is empty or none 

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> (bool): Flag stating if the serie is empty or not

        """
        

    def set_unique(self):
        """
        --------------------
        Description
        --------------------
        -> set_unique (method): Class method that computes the number of unique value of a serie and store the results in the relevant attribute(self.n_unique).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        self.n_unique = self.df[st.session_state.date_column].nunique()

    def set_missing(self):
        """
        --------------------
        Description
        --------------------
        -> set_missing (method): Class method that computes the number of missing value of a serie and store the results in the relevant attribute(self.n_missing).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        self.n_missing = self.df[st.session_state.date_column].isna().sum()
        

    def set_min(self):
        """
        --------------------
        Description
        --------------------
        -> set_min (method): Class method that computes the minimum value of a serie and store the results in the relevant attribute(self.col_min).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        self.col_min = self.serie.min()
        

    def set_max(self):
        """
        --------------------
        Description
        --------------------
        -> set_max (method): Class method that computes the minimum value of a serie and store the results in the relevant attribute(self.col_max).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        self.col_max = self.serie.max()
        

    def set_weekend(self):
        """
        --------------------
        Description
        --------------------
        -> set_weekend (method): Class method that computes the number of times a serie has dates falling during weekend and store the results in the relevant attribute(self.n_weekend).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        date_to_day_value = pd.DataFrame({'date_number': self.serie.apply(lambda i: i.weekday())})
        self.n_weekend = date_to_day_value[date_to_day_value.date_number > 4].sum()['date_number']
        

    def set_weekday(self):
        """
        --------------------
        Description
        --------------------
        -> set_weekday (method): Class method that computes the number of times a serie has dates not falling during weekend and store the results in the relevant attribute(self.n_weekday).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        date_to_day_value = pd.DataFrame({'date_number': self.serie.apply(lambda i: i.weekday())})
        self.n_weekday = date_to_day_value[date_to_day_value.date_number < 5].sum()['date_number']
        

    def set_future(self):
        """
        --------------------
        Description
        --------------------
        -> set_future (method): Class method that computes the number of times a serie has dates falling in the future and store the results in the relevant attribute(self.n_future).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        self.n_future = self.serie[self.serie>datetime.now()].count()
        
    
    def set_empty_1900(self):
        """
        --------------------
        Description
        --------------------
        -> set_empty_1900 (method): Class method that computes the number of times a serie has dates equal to '1900-01-01' and store the results in the relevant attribute(self.n_empty_1900).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        self.n_empty_1900 = self.serie[self.serie == '1900-01-01'].count()
        

    def set_empty_1970(self):
        """
        --------------------
        Description
        --------------------
        -> set_empty_1970 (method): Class method that computes the number of times a serie has only digit characters and store the results in the relevant attribute(self.n_empty_1970).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        self.n_empty_1970 = self.serie[self.serie == '1970-01-01'].count()
        

    def set_barchart(self):  
        """
        --------------------
        Description
        --------------------
        -> set_barchart (method): Class method that computes the Altair barchart displaying the count for each value of a serie and store the results in the relevant attribute(self.barchart).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        self.barchart = self.serie.value_counts()
        
      
    def set_frequent(self, end=20):
        """
        --------------------
        Description
        --------------------
        -> set_frequent (method): Class method that computes the Dataframe containing the most frequest value of a serie and store the results in the relevant attribute(self.frequent).

        --------------------
        Parameters
        --------------------
        -> end (int):
            Parameter indicating the maximum number of values to be displayed

        --------------------
        Returns
        --------------------
        -> None

        """
        if self.serie is not None:
            value_counts = self.serie.value_counts()
            most_frequent = self.serie.value_counts().nlargest(20)
            # print(value_counts)
            self.frequent.value = most_frequent.index.tolist()
            print(most_frequent.index.tolist())
            self.frequent.occurrence = most_frequent.values
            print(most_frequent.values)
            self.frequent.percentage = (self.frequent.occurrence /
                                        value_counts.values.sum()) * 100

        

    def get_summary(self):
        """
        --------------------
        Description
        --------------------
        -> get_summary (method): Class method that formats all requested information from self.serie to be displayed in the Overall section of Streamlit app as a Pandas dataframe with 2 columns: Description and Value

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> (pd.DataFrame): Formatted dataframe to be displayed on the Streamlit app

        """
        
