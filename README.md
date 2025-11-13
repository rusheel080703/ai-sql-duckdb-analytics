# 🤖 AI SQL DuckDB Analytics

**Bridging Large Language Models and High-Performance Analytics using DuckDB and Python.**

This repository documents an analytical project focused on using an **AI model (Kimi K2)** to generate complex SQL queries and executing them efficiently using the **DuckDB** in-process OLAP database.

The project demonstrates the practical application of AI in generating complex business logic, particularly for calculating metrics like attendance (via project/class week correlation) and payroll.

---

## 📋 Table of Contents

1.  [🧠 Methodology: AI-Generated SQL](#-methodology-ai-generated-sql)
2.  [🛠 Tech Stack](#-tech-stack)
3.  [📊 Analytics Queries (Q1 - Q5)](#-analytics-queries-q1---q5)
4.  [💻 Setup & Execution](#-setup--execution)
5.  [📁 Project Structure](#-project-structure)

---

## 🧠 Methodology: AI-Generated SQL

The core of this project is the integration of an AI model (Kimi K2) to generate five complex SQL queries required for the college's analytics.

### LLM Integration & Adaptation

* **SQL Generation:** Kimi K2 provided the underlying logic for all five queries (Q1-Q5).
* **Execution:** The queries are executed in Python using the **DuckDB** library, which reads data directly from the local CSV files (e.g., `instructor.csv`, `class_schedule.csv`).
* **Technical Fix (Q5):** The AI-generated SQL for payroll calculation (Q5) required a manual fix in the Python script to use DuckDB's native functions (`strptime` and `date_part`) to correctly calculate the difference between `start_time` and `end_time` in hours.

---

## 🛠 Tech Stack

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Database** | **DuckDB** | High-performance, in-process analytical processing (OLAP). |
| **SQL Generation** | Kimi K2 (AI Model) | Generates complex analytical query logic. |
| **Driver** | Python | Orchestrates SQL execution and data presentation. |
| **Data Source** | CSV Files (9 total) | Raw data files used as tables (e.g., `instructor.csv`, `rating.csv`). |

---

## 📊 Analytics Queries (Q1 - Q5)

The project solves five key analytical questions about the coding curriculum, demonstrating complex join logic across tables.

| Query | Question | Core Logic & Key Files Used |
| :--- | :--- | :--- |
| **Q1** | Course with the most students. | Counts unique students enrolled in **Project** teams. (Files: `project`, `student_team`, `team_member`). |
| **Q2** | Most popular instructor (by students taught). | Infers "students taught" by counting unique students on a project in the **same week** as a scheduled class taught by the instructor. |
| **Q3** | Most popular instructor (by rating). | Calculates the **Average Star Rating** from the `rating.csv` where `rated_type = 'instructor'`. |
| **Q4** | Enrollment listing (class name and count). | Uses the same complex **attendance inference logic** as Q2 to count students for all coding classes. |
| **Q5** | Total pay for an instructor X (Grace Hopper, ID 1). | Calculates total pay as (Teaching Hours \* Teaching Rate) + (Supervision Hours \* Supervision Rate). |

---

## 💻 Setup & Execution

The project files are structured by query (Q1-Q5). To execute any query, you must navigate to its specific folder (`Qx/`) as the Python scripts reference the CSV files located in their respective subdirectories.

### 1️⃣ Prerequisites

You must have **Python** and the **DuckDB** library installed:

```bash
pip install duckdb
```
### 2️⃣ Execution
To run the query for Question 1 (as an example):
```bash
# Navigate to the subdirectory
cd Q3

# Execute the Python script
python Q3.py

```

Execute the Python script

<img width="500" height="150" alt="image" src="https://github.com/user-attachments/assets/753ac124-f646-424b-8adb-53109ab680a3" />



### 📁 Project Structure
The repository is organized by query into five folders (Q1-Q5), each containing the minimum set of files required for its individual execution.
<img width="1345" height="425" alt="image" src="https://github.com/user-attachments/assets/31080cc9-c70a-4be4-8ad3-a0be3777b35a" />


### 🧑‍💻 Author
Rusheel Vijay Sable3
Role: AI & Data Science Engineer
Focus: Data Analytics, LLM-based Workflow Automation, and High-Performance Databases.

