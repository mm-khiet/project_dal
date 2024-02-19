


def data_description_handler(df):
    data_description_dataset_shape(df)
    data_description_head_snippet(df)
    data_description_info(df)
    data_description_statistical_properties(df)
    data_description_categorical_data_insights(df)
    data_description_missing_values(df)
    data_description_corrleation_insights(df)
    pass


# Shape of the dataset <colums, rows>
def data_description_dataset_shape(df):
    print(f"Dataset contains {df.shape[0]} records and {df.shape[1]} features.")
    pass


# Print the first several rows to understand how data looks like
def data_description_head_snippet(df):
    print(df.head())
    pass


# Print a concise summary of the DataFrame
# This includes column names, non-null counts, and data types
def data_description_info(df):
    print(df.info())
    pass


# Describe the statistical properties of numerical features
def data_description_statistical_properties(df):
    print(df.describe())
    pass


# For categorical data, you might want to see unique values and their counts
def data_description_categorical_data_insights(df):
    for col in df.select_dtypes(include=['object']).columns:
        print(f"\nColumn: {col}")
        print(df[col].value_counts().head())  # Adjust as needed to see more/less values
    pass


# Check for missing values
def data_description_missing_values(df):
    print(df.isnull().sum())
    pass


# Additional insights such as correlations can be helpful for numerical data
def data_description_corrleation_insights(df):
    # print(df.corr())
    pass

