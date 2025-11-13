#### **Database Homework 2 Submission**



This submission contains the deliverables for Homework 2, involving SQL generation by Kimi K2 and execution using DuckDB via Python.



1\. Submission Structure and Organization

The submission is organized by query into five folders (Q1 through Q5). This structure is based on the minimal files necessary to execute each individual query.



File Path Execution Note

The Python scripts (Qx.py) were placed in subdirectories. To guarantee successful execution, only the specific CSV files explicitly referenced in the SQL for that query were included in its corresponding folder.



For example:



Q1 Folder contains: Q1.py, Q1\_Kimi\_SQL.png, Q1\_out.png, project.csv, student\_team.csv, and team\_member.csv.



Q3 Folder contains: Q3.py, Q3\_Kimi\_SQL.png, Q3\_out.png, instructor.csv, and rating.csv.



The grader should run the Python scripts directly from within their respective folders (e.g., run python Q1.py while inside the Q1 folder).



2\. Query Logic and Data Scope

The assignment required data from 9 total CSV files across all five questions. The data correctly reflects the logical model created by the AI.



Below is a summary of the five questions and the underlying logic, which verifies the structure of the CSV files and the purpose of the SQL queries.



Question: Course with most students.

Key Files Used: project, student\_team, team\_member.

Logic: Assumed "course" means Project. Counts unique students enrolled in projects.



Question: Most popular instructor (by students taught).

Key Files Used: 6 files (instructor, class\_schedule, student, project, student\_team, team\_member).

Logic: Attendance is inferred: a student is counted as "taught" if they are on a project running in the same week as the scheduled class.



Question: Most popular instructor (by rating).

Key Files Used: instructor, rating.

Logic: Calculates the Average Star Rating from the rating.csv where rated\_type = 'instructor'.



Question: Enrollment listing (class name and count).

Key Files Used: 6 files (Same set as Q2).

Logic: Uses the same complex attendance inference as Q2 to count students for all coding classes.



Question: Given an instructor X, how much was he/she paid?

Key Files Used: instructor, class\_schedule, project\_supervision.

Technical Note: The SQL was fixed in the Python script to use DuckDB's native functions (strptime and date\_part) to correctly calculate teaching hours, resolving a technical incompatibility issue with the AI-generated SQL.

