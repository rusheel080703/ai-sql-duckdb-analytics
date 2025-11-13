
# 🤖 AI SQL DuckDB Analytics

**Bridging Large Language Models and High-Performance Analytics using DuckDB and Python.**

This repository documents an analytical project focused on using an **AI model (Kimi K2)** to generate complex SQL queries and executing them efficiently using the **DuckDB** in-process OLAP database.

The project demonstrates the application of AI in generating business logic, particularly for calculating metrics like attendance and payroll.

---

## 📋 Table of Contents

1.  [🧠 Methodology: AI-Generated SQL](#-methodology-ai-generated-sql)
2.  [🛠 Tech Stack](#-tech-stack)
3.  [📊 Analytics Queries (Q1 - Q5)](#-analytics-queries-q1---q5)
4.  [💻 Setup & Execution](#-setup--execution)
5.  [📁 Project Structure](#-project-structure)
6.  [🧑‍💻 Author](#-author)

---

## 🧠 Methodology: AI-Generated SQL

The project's core involves generating five complex SQL queries (Q1-Q5) using an AI model and executing them against a relational data set loaded from local CSV files.

### Key Analytical Logic

* **Attendance/Enrollment (Q2, Q4):** A student's class attendance is **inferred** if they are on a project team that runs in the **same week** as the scheduled class session.
* **Payroll Calculation (Q5):** The total pay is calculated by summing teaching pay and supervision pay. The AI-generated SQL required a manual fix in the Python script to use DuckDB's native functions (`strptime` and `date_part`) to correctly calculate teaching hours from the time strings.

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

| Query | Question | Core Logic |
| :--- | :--- | :--- |
| **Q1** | Course with the most students. | Counts unique students enrolled in **Project** teams. |
| **Q2** | Most popular instructor (by students taught). | Counts unique students whose project attendance is inferred by **week number** matching class schedule. |
| **Q3** | Most popular instructor (by rating). | Calculates the **Average Star Rating** from the `rating.csv` where `rated_type = 'instructor'`. |
| **Q4** | Enrollment listing (class name and count). | Uses the same complex **attendance inference logic** as Q2 for all coding classes. |
| **Q5** | Total pay for an instructor X. | Calculates (Teaching Hours \* Rate) + (Supervision Hours \* Rate) using corrected DuckDB functions. |

---

## 💻 Setup & Execution

The project is designed to be executed directly from the respective query folders (`Qx/`) to ensure the Python scripts correctly find the necessary local CSV files.

### 1️⃣ Prerequisites

You must have **Python** and the **DuckDB** library installed:

```bash
pip install duckdb
````

### 2️⃣ Execution

To run the query for **Question 3** (as an example):

```bash
# Navigate to the subdirectory
cd Q3

# Execute the Python script
python Q3.py
```

**Example Output (Q3: Most Popular Instructor by Rating):**

```text
┌───────────────┬────────────┬───────────┬──────────────────────┐
│ instructor_id │ first_name │ last_name │      avg_rating      │
│     int64     │  varchar   │  varchar  │        double        │
├───────────────┼────────────┼───────────┼──────────────────────┤
│             1 │ Grace      │ Hopper    │ 4.666666666666667    │
└───────────────┴────────────┴───────────┴──────────────────────┘
```

-----

## 📁 Project Structure

The repository is organized by query into five folders (Q1-Q5), each containing the minimum set of files required for its individual script to run successfully.

| File | Description |
| :--- | :--- |
| `Qx/Qx.py` | Python script containing the final SQL and DuckDB execution logic. |
| `Qx/Qx_Kimi_SQL.png` | Screenshot of the original AI-generated SQL query. |
| `Qx/Qx_out.png` | Screenshot of the query result. |
| `Qx/*.csv` | The required data files for the specific query (e.g., `Q3/instructor.csv`, `Q3/rating.csv`). |

-----

## 🧑‍💻 Author

**Rusheel Vijay Sable**

  * **Role:** AI & Data Science Engineer
  * **Focus:** Data Analytics, LLM-based Workflow Automation, and High-Performance Databases.

<!-- end list -->

```
```

