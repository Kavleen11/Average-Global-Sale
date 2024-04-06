# Average-Global-Sale
**Project Title:**
Analyzing Video Game Sales Data from MySQL Database

**Short Description:** 
This Python script connects to a MySQL database, retrieves video game sales data, performs analysis using pandas, and prints the results. The analysis includes calculating average global sales before and after the year 2005, and categorizing games into pre-2005 and post-2005 eras based on their release years.

**Getting Started:**

**Prerequisites:**

Python installed on  machine 
Required libraries: pandas, sqlalchemy, pymysql

**Installing:** 
You can install the required libraries using pip: pip install pandas sqlalchemy pymysql

**Running the Script:** 
You can run the Python script by executing the following command:

python analyze_video_game_sales.py

**Breakdown of Script:**
Connects to a MySQL database using SQLAlchemy and pymysql. Retrieves video game sales data from the 'vgsales_2016' table in the 'data1202' database. Calculates the average global sales before and after the year 2005. Adds a new column 'Era' to categorize games into pre-2005 and post-2005 eras. Prints the results, including the average global sales and the DataFrame with the 'Era' column.

**Deployment:** 
This script can be deployed on any machine with Python installed to analyze video game sales data stored in a MySQL database.

**Author:**
Kavleen Kaur

**License:** 
This project is licensed under the xyz License - see the LICENSE file for details.

**Acknowledgement**:

The data used in this analysis is sourced from a MySQL database. This script is inspired by various class tutorials and examples provided by Professor.
