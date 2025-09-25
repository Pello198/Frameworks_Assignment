CORD-19 Research Papers Exploration

This repository contains an exploratory data analysis (EDA) of the CORD-19 dataset
, specifically focusing on the metadata.csv file.

The project is split into two main components:

Jupyter Notebook (CORD19_Analysis.ipynb) → Step-by-step analysis & visualization.

Streamlit Application (streamlit_app.py) → Interactive dashboard for exploration.

🚀 Workflow Overview

The project follows a data science workflow:

Data Loading & Exploration

Load metadata.csv into a pandas DataFrame.

Inspect structure (rows, columns, data types).

Check for missing values.

Generate basic statistics.

Data Cleaning & Preparation

Handle missing values by dropping/filling as needed.

Convert publication dates into proper datetime format.

Extract year for time-based analysis.

Create new features such as abstract word count.

Data Analysis & Visualization

Count research papers per year.

Identify top publishing journals.

Find frequent words in titles.

Create visualizations:

Publications over time (bar chart).

Top journals (bar chart).

Word cloud of titles.

Distribution by source.

Application & Sharing

Notebook documents the full workflow (transparent & reproducible).

Streamlit app enables interactive exploration with filters (year ranges, dropdowns).

GitHub repo makes it shareable for others to view and run.

📒 File 1: CORD19_Analysis.ipynb

This Jupyter Notebook provides a step-by-step narrative of the analysis.

Structure of the Notebook

Part 1: Data Loading & Exploration

Loads metadata.csv into a DataFrame.

Prints shape, info, missing values.

Part 2: Data Cleaning & Preparation

Handles missing data.

Parses publish_time into datetime.

Extracts year column.

Adds abstract word count column.

Part 3: Data Analysis & Visualization

Counts publications per year.

Identifies top 10 journals.

Tokenizes titles & counts most frequent words.

Generates plots (bar charts, word cloud).

✅ Purpose: Acts as your research log — showing all transformations, decisions, and insights step by step.

🌐 File 2: streamlit_app.py

This Streamlit application transforms the notebook’s insights into an interactive web app.

Features of the App

Layout

Title, description, sidebar filters.

Filters

Year range slider.

Journal dropdown.

Visualizations

Publications over time (based on selected year range).

Top publishing journals.

Word cloud of paper titles.

Data Preview

Displays a sample of the dataset.

✅ Purpose: Acts as your presentation tool — others can explore the dataset dynamically without writing code.

🔄 How They Complement Each Other

Notebook (.ipynb) → Explains the why and how.

Streamlit (.py) → Demonstrates the what and results.

Together:

Notebook = in-depth analysis.

Streamlit = interactive storytelling.

🛠️ How to Run
1. Run the Notebook

You can open the notebook in:

Google Colab → Upload CORD19_Analysis.ipynb + metadata.csv.

Jupyter Notebook → Run locally with Python & Jupyter installed.

2. Run the Streamlit App

Install dependencies:

pip install pandas matplotlib wordcloud streamlit


Run the app:

streamlit run streamlit_app.py


Open the provided localhost link in your browser.

📌 Notes

The dataset (metadata.csv) is too large for GitHub, so it is not included in this repository.

You can download it directly from the CORD-19 dataset on Kaggle
.

Place metadata.csv in the same folder as the notebook and the Streamlit app.

