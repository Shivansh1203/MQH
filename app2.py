

# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import os

# def reshape_csv_table(csv_file):
#     # Read the CSV file
#     df = pd.read_csv(csv_file)
    
#     # Initialize empty lists for Timestamp and Value
#     timestamps = []
#     values = []
    
#     # Iterate through each row in the dataframe
#     for index, row in df.iterrows():
#         # Iterate through each column in the row
#         for column in df.columns:
#             # If the column name starts with "Timestamp"
#             if column.startswith('Timestamp'):
#                 # Get the timestamp value
#                 timestamp = row[column]
#                 # If the timestamp value is not NaN
#                 if pd.notna(timestamp):
#                     # Append the timestamp value to the list
#                     timestamps.append(timestamp)
#                     # Extract the corresponding value from the row
#                     value_col = column.replace('Timestamp', '')
#                     value = row[value_col.strip('. ')]
#                     # Append the corresponding value to the list
#                     values.append(value)
    
#     # Create a new dataframe with Timestamp and Value columns
#     new_df = pd.DataFrame({'Timestamp': timestamps, 'Value': values})
    
#     # Remove rows with NaN values in the "Value" column
#     new_df = new_df.dropna(subset=['Value'])
    
#     # Convert Timestamp column to datetime
#     new_df['Timestamp'] = pd.to_datetime(new_df['Timestamp'], format='%d-%m-%Y', errors='coerce')
    
#     # Sort the dataframe by Timestamp in ascending order
#     new_df = new_df.sort_values(by='Timestamp')
    
#     # Remove rows with NaN values after sorting
#     new_df = new_df.dropna(subset=['Timestamp'])
    
#     return new_df

# # Streamlit UI
# st.title('CSV Viewer and Graph Plotter')

# # Fetch all CSV files from the current directory
# csv_files = [file for file in os.listdir('.') if file.endswith('.csv')]

# # Dropdown menu to select a CSV file
# selected_csv = st.selectbox("Choose a CSV file", csv_files)

# if selected_csv:
#     # Process the selected CSV file
#     dataframe = reshape_csv_table(selected_csv)
    
#     # Display the dataframe (optional)
#     st.write(dataframe)
    
#     # Convert minimum and maximum Timestamp values to datetime objects
#     min_timestamp = pd.to_datetime(dataframe['Timestamp'].min(), format='%d-%m-%Y')
#     max_timestamp = pd.to_datetime(dataframe['Timestamp'].max(), format='%d-%m-%Y')
    
#     # Set default start and end dates
#     default_start_date = pd.Timestamp('2011-01-18')
#     default_end_date = pd.Timestamp('2011-01-25')
    
#     # Date range selection
#     start_date = st.date_input('Start date', min_value=min_timestamp.date(), max_value=max_timestamp.date(), value=default_start_date.date())
#     end_date = st.date_input('End date', min_value=min_timestamp.date(), max_value=max_timestamp.date(), value=default_end_date.date())
    
#     # Convert Timestamp column to Timestamp format
#     dataframe['Timestamp'] = pd.to_datetime(dataframe['Timestamp'], format='%d-%m-%Y')
    
#     # Filter the dataframe based on the selected date range
#     mask = (dataframe['Timestamp'] >= pd.Timestamp(start_date)) & (dataframe['Timestamp'] <= pd.Timestamp(end_date))
#     filtered_df = dataframe.loc[mask]
    
#     # Plotting with Matplotlib
#     if not filtered_df.empty:
   
#         st.subheader("Plotly Plot")
#         st.write("Hover over the plot to see data values.")
#         fig = px.line(filtered_df, x='Timestamp', y='Value', title='Value over Time', labels={'Timestamp': 'Timestamp', 'Value': 'Value'})
#         fig.update_xaxes(rangeslider_visible=True)  # Add range slider for zooming
#         st.plotly_chart(fig)
#     else:
#         st.write("No data available for the selected date range.")
    
#     # Plotting with Plotly
#     if not filtered_df.empty:
#         st.subheader("Matplotlib Plot")
#         st.line_chart(filtered_df.set_index('Timestamp'))
        
#         # Calculate range of values
#         value_range = filtered_df['Value'].max() - filtered_df['Value'].min()
#         st.write(f'Range of values: {value_range}')
        
#         # Calculate highest and lowest values
#         highest_value = filtered_df['Value'].max()
#         lowest_value = filtered_df['Value'].min()
#         st.write(f'Highest value: {highest_value}')
#         st.write(f'Lowest value: {lowest_value}')
#     else:
#         st.write("No data available for the selected date range.")

import streamlit as st
import pandas as pd
import plotly.express as px
import os

def reshape_csv_table(csv_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)
    
    # Initialize empty lists for Timestamp and Value
    timestamps = []
    values = []
    
    # Iterate through each row in the dataframe
    for index, row in df.iterrows():
        # Iterate through each column in the row
        for column in df.columns:
            # If the column name starts with "Timestamp"
            if column.startswith('Timestamp'):
                # Get the timestamp value
                timestamp = row[column]
                # If the timestamp value is not NaN
                if pd.notna(timestamp):
                    # Append the timestamp value to the list
                    timestamps.append(timestamp)
                    # Extract the corresponding value from the row
                    value_col = column.replace('Timestamp', '')
                    value = row[value_col.strip('. ')]
                    # Append the corresponding value to the list
                    values.append(value)
    
    # Create a new dataframe with Timestamp and Value columns
    new_df = pd.DataFrame({'Timestamp': timestamps, 'Value': values})
    
    # Remove rows with NaN values in the "Value" column
    new_df = new_df.dropna(subset=['Value'])
    
    # Convert Timestamp column to datetime
    new_df['Timestamp'] = pd.to_datetime(new_df['Timestamp'], format='%d-%m-%Y', errors='coerce')
    
    # Sort the dataframe by Timestamp in ascending order
    new_df = new_df.sort_values(by='Timestamp')
    
    # Remove rows with NaN values after sorting
    new_df = new_df.dropna(subset=['Timestamp'])
    
    return new_df

# Streamlit UI
st.title('CSV Viewer and Graph Plotter')

# Fetch all CSV files from the current directory
csv_files = [file for file in os.listdir('.') if file.endswith('.csv')]

# Multiselect menu to select multiple CSV files
selected_csvs = st.multiselect("Choose CSV files", csv_files)

if selected_csvs:
    # Process the selected CSV files
    dataframes = [reshape_csv_table(csv_file) for csv_file in selected_csvs]
    
    for idx, dataframe in enumerate(dataframes):
        st.subheader(f"CSV File {idx + 1}")
        st.write(dataframe)
    
    # Convert minimum and maximum Timestamp values to datetime objects
    min_timestamp = min(df['Timestamp'].min() for df in dataframes)
    max_timestamp = max(df['Timestamp'].max() for df in dataframes)
    
    # Set default start and end dates
    default_start_date = pd.Timestamp('2011-01-18')
    default_end_date = pd.Timestamp('2011-01-25')
    
    # Date range selection
    start_date = st.date_input('Start date', min_value=min_timestamp.date(), max_value=max_timestamp.date(), value=default_start_date.date())
    end_date = st.date_input('End date', min_value=min_timestamp.date(), max_value=max_timestamp.date(), value=default_end_date.date())
    
    # Filter the dataframes based on the selected date range
    filtered_dfs = []
    for dataframe in dataframes:
        mask = (dataframe['Timestamp'] >= pd.Timestamp(start_date)) & (dataframe['Timestamp'] <= pd.Timestamp(end_date))
        filtered_df = dataframe.loc[mask]
        filtered_dfs.append(filtered_df)
    
    # Plotting with Plotly
    for idx, filtered_df in enumerate(filtered_dfs):
        if not filtered_df.empty:
            st.subheader(f"Plot for CSV File {idx + 1}")
            st.write("Hover over the plot to see data values.")
            fig = px.line(filtered_df, x='Timestamp', y='Value', title=f'Value over Time (CSV File {idx + 1})', labels={'Timestamp': 'Timestamp', 'Value': 'Value'})
            fig.update_xaxes(rangeslider_visible=True)  # Add range slider for zooming
            st.plotly_chart(fig)

            
        else:
            st.write(f"No data available for CSV File {idx + 1}.")
