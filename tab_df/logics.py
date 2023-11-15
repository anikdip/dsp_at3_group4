import pandas as pd


class Dataset:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
        self.cols_list = []
        self.n_rows = 0
        self.n_cols = 0
        self.n_duplicates = 0
        self.n_missing = 0
        self.n_num_cols = 0
        self.n_text_cols = 0
        self.table = None

    def set_data(self):
        self.set_df()
        if not self.is_df_none():
            self.set_columns()
            self.set_dimensions()
            self.set_duplicates()
            self.set_missing()
            self.set_numeric()
            self.set_text()
            self.set_table()

    def set_df(self):
        self.df = pd.read_csv(self.file_path, encoding='cp1252')

    def is_df_none(self):
        return self.df is None

    def set_columns(self):
        self.cols_list = self.df.columns.tolist()

    def set_dimensions(self):
        self.n_rows, self.n_cols = self.df.shape

    def set_duplicates(self):
        self.n_duplicates = self.df.duplicated().sum()

    def set_missing(self):
        self.n_missing = self.df.isnull().sum().sum()

    def set_numeric(self):
        self.n_num_cols = len(self.df.select_dtypes(include=['number']).columns)

    def set_text(self):
        self.n_text_cols = len(self.df.select_dtypes(include=['object']).columns)

    def get_head(self, n=5):
        return self.df.head(n)

    def get_tail(self, n=5):
        return self.df.tail(n)

    def get_sample(self, n=5):
        return self.df.sample(n)

    def set_table(self):
        col_info = []
        for col in self.df.columns:
            col_info.append({
                'Column Name': col,
                'Data Type': str(self.df[col].dtype),
                'Memory Usage (KB)': round(self.df[col].memory_usage(deep=True) / 1024, 2)
            })
        self.table = pd.DataFrame(col_info)

    def get_summary(self):
        summary = {
            'Description': ['Number of Rows', 'Number of Columns', 'Number of Duplicated Rows',
                            'Number of Missing Values', 'Number of Numeric Columns', 'Number of Text Columns'],
            'Value': [self.n_rows, self.n_cols, self.n_duplicates, self.n_missing, self.n_num_cols, self.n_text_cols]
        }
        summary_df = pd.DataFrame(summary)
        return summary_df
