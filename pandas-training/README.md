Pandas Training

A structured, hands-on Pandas learning module built to practice the core concepts of working with tabular data in Python. This project covers everything from creating Series and DataFrames to filtering, cleaning, grouping, combining, and intermediate Pandas operations such as apply, map, datetime handling, pivot tables, and crosstabs.

⸻

Project Goals

This repository is designed to help you:

* learn Pandas in a structured order instead of memorizing random commands
* understand how DataFrames and Series work
* practice inspecting, filtering, cleaning, and transforming tabular data
* build confidence with real CSV datasets
* revise Pandas topic-by-topic using separate Python files

⸻

Tech Stack

* Python
* Pandas
* NumPy

⸻

Project Structure

pandas-training/
│
├─ README.md
├─ requirements.txt
├─ main.py
│
├─ datasets/
│  ├─ employees.csv
│  ├─ sales.csv
│  └─ students.csv
│
├─ notes/
│  ├─ 01_pandas_basics.md
│  ├─ 02_selection_filtering.md
│  ├─ 03_cleaning_editing.md
│  ├─ 04_grouping_sorting_combining.md
│  └─ 05_intermediate_pandas.md
│
└─ src/
   ├─ 01_getting_started/
   │  ├─ 01_series_dataframe.py
   │  ├─ 02_read_write_csv.py
   │  └─ 03_dataframe_overview.py
   │
   ├─ 02_looking_at_data/
   │  ├─ 01_head_tail_shape.py
   │  ├─ 02_info_describe.py
   │  └─ 03_value_counts_unique.py
   │
   ├─ 03_selecting_filtering/
   │  ├─ 01_select_columns.py
   │  ├─ 02_loc_iloc.py
   │  ├─ 03_filter_rows.py
   │  └─ 04_multiple_conditions.py
   │
   ├─ 04_cleaning_editing/
   │  ├─ 01_find_fill_drop_nulls.py
   │  ├─ 02_add_edit_column.py
   │  ├─ 03_change_dtype.py
   │  ├─ 04_drop_rename_duplicates.py
   │  └─ 05_string_cleaning_basics.py
   │
   ├─ 05_grouping_sorting_combining/
   │  ├─ 01_sort_values.py
   │  ├─ 02_groupby_basics.py
   │  ├─ 03_merge_dataframes.py
   │  └─ 04_concat_dataframes.py
   │
   └─ 06_intermediate_pandas/
      ├─ 01_apply_map_lambda.py
      ├─ 02_datetime_basics.py
      ├─ 03_pivot_table_intro.py
      └─ 04_crosstab_intro.py

⸻

Topics Covered

1. Getting Started with Pandas

* Importing Pandas
* Creating a Series
* Creating a DataFrame
* Reading CSV files with pd.read_csv()
* Writing CSV files with to_csv()
* Understanding DataFrame structure using shape, columns, index, and dtypes

2. Looking at Data

* head() and tail()
* info()
* describe()
* value_counts()
* unique()
* nunique()

3. Selecting and Filtering

* Selecting single and multiple columns
* Using loc[]
* Using iloc[]
* Filtering rows with conditions
* Filtering with multiple conditions using & and |

4. Cleaning and Editing

* Detecting missing values with isnull()
* Filling missing values with fillna()
* Dropping missing values with dropna()
* Adding and editing columns
* Changing data types with astype()
* Converting dates with pd.to_datetime()
* Dropping rows/columns
* Renaming columns
* Removing duplicates
* Basic string cleaning with .str

5. Grouping, Sorting, and Combining

* Sorting rows with sort_values()
* Grouping with groupby()
* Aggregating with mean(), count(), max(), and agg()
* Merging DataFrames with pd.merge()
* Concatenating DataFrames with pd.concat()

6. Intermediate Pandas

* Using map()
* Using apply()
* Using lambda
* Datetime extraction with .dt
* Pivot tables with pd.pivot_table()
* Crosstabs with pd.crosstab()

⸻

Datasets Used

This project uses three small datasets for practice:

employees.csv

Used for:

* DataFrame basics
* filtering
* cleaning
* grouping
* datetime examples
* duplicates and null handling

sales.csv

Used for:

* grouping
* revenue calculation
* pivot table examples

students.csv

Used for:

* categorical summaries
* crosstab examples

⸻

Setup Instructions

1. Clone or create the project folder

Place all project files inside a folder named pandas-training.

2. Create and activate a virtual environment (optional but recommended)

Windows

python -m venv venv
venv\Scripts\activate

macOS / Linux

python3 -m venv venv
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

⸻

How to Run

Run the main entry file

python main.py

This will show the suggested learning order for the project.

Run topic files individually

Example:

python src/01_getting_started/01_series_dataframe.py
python src/02_looking_at_data/02_info_describe.py
python src/03_selecting_filtering/04_multiple_conditions.py

⸻

Recommended Learning Order

Follow the files in this order:

Step 1 — Basics

* src/01_getting_started/01_series_dataframe.py
* src/01_getting_started/02_read_write_csv.py
* src/01_getting_started/03_dataframe_overview.py

Step 2 — Looking at Data

* src/02_looking_at_data/01_head_tail_shape.py
* src/02_looking_at_data/02_info_describe.py
* src/02_looking_at_data/03_value_counts_unique.py

Step 3 — Selection and Filtering

* src/03_selecting_filtering/01_select_columns.py
* src/03_selecting_filtering/02_loc_iloc.py
* src/03_selecting_filtering/03_filter_rows.py
* src/03_selecting_filtering/04_multiple_conditions.py

Step 4 — Cleaning and Editing

* src/04_cleaning_editing/01_find_fill_drop_nulls.py
* src/04_cleaning_editing/02_add_edit_column.py
* src/04_cleaning_editing/03_change_dtype.py
* src/04_cleaning_editing/04_drop_rename_duplicates.py
* src/04_cleaning_editing/05_string_cleaning_basics.py

Step 5 — Grouping, Sorting, and Combining

* src/05_grouping_sorting_combining/01_sort_values.py
* src/05_grouping_sorting_combining/02_groupby_basics.py
* src/05_grouping_sorting_combining/03_merge_dataframes.py
* src/05_grouping_sorting_combining/04_concat_dataframes.py

Step 6 — Intermediate Pandas

* src/06_intermediate_pandas/01_apply_map_lambda.py
* src/06_intermediate_pandas/02_datetime_basics.py
* src/06_intermediate_pandas/03_pivot_table_intro.py
* src/06_intermediate_pandas/04_crosstab_intro.py

⸻

What You Will Learn by the End

By completing this project, you should be comfortable with:

* creating and reading DataFrames
* inspecting dataset structure
* selecting rows and columns
* filtering data using conditions
* cleaning missing and duplicate values
* creating and modifying columns
* converting data types
* grouping and summarizing data
* combining multiple DataFrames
* working with dates in Pandas
* using pivot tables and crosstabs for analysis

⸻

Notes

* Each Python file focuses on one Pandas topic.
* The code is intentionally split into small examples for easier learning and revision.
* The datasets are small and readable so that Pandas behavior is easy to understand.
* You can expand this repository later by adding advanced topics such as:
    * query()
    * isin()
    * melt()
    * stack() / unstack()
    * rolling window functions
    * time series analysis
    * larger project-style datasets

⸻

Author

Created as a structured Pandas practice and revision project.