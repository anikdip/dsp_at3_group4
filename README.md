# <project title>

## Authors
Group <group number> :
- Anik Mahamood (24704052)
- Sadia Afrin Mallick (24880231) 

## Description
The main purpose of this application is to show some statistics of any given csv dataset.

First uploading the csv dataset through upload function then with that given dataset it will visualize
some analytics of the overall dataset and some analytics of the date field.

### The problem we faced:
- Design the web application with give template
- Using git within the team and code merging 
- Team collaboration and communication
- Finding the proper method for finding the date field 

### Features implement in future
- Implement more analysis
- Incorporate major Machine learning models
- Make it more dynamics

## How to Setup
Clone the repository: git clone <repository_url>
    Navigate to the project directory: cd <project_directory>
    Create a virtual environment: python -m venv venv
    Activate the virtual environment:
        On Windows: venv\Scripts\activate
        On macOS/Linux: source venv/bin/activate
    Install required packages: pip install -r requirements.txt

## How to Run the Program
Check if Python is installed on the system.
    To view the project directory, use the terminal.
    Run the project using this commend: streamlit run /<project_directory>/app/streamlit_app.py
    After being sent to the application page, you may explore the features and upload any kind of CSV file.

## Project Structure
    app/
        streamlit_app.py: Main Streamlit application script.
    tab_df/
        display_tab_df_content.py: Module for displaying DataFrame tab content.
    tab_date/
        display_tab_date_content.py: Module for displaying Datetime Series tab content.

