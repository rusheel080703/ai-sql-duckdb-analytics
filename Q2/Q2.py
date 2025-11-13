# Q2.py - Who is the most popular instructor (teaches the most students)?

import duckdb

# SQL adapted to use CSV file names
KIMI_SQL_Q2 = """
SELECT T1.instructor_id,
       T1.first_name,
       T1.last_name,
       COUNT(DISTINCT T2.student_id) AS students_taught
FROM 'instructor.csv' AS T1
JOIN 'class_schedule.csv' AS T3
  ON T3.instructor_id = T1.instructor_id
JOIN (
    /* Subquery T2: Finds distinct students (S.student_id) 
       that are on a project team (ST) in the same week (P.week_number) 
       as a class schedule item (CS3.schedule_id). 
       This serves as the 'attendance' fact table. */
    SELECT DISTINCT T4.student_id, T5.schedule_id
    FROM 'student.csv' AS T4
    JOIN 'team_member.csv' AS TM ON TM.student_id = T4.student_id
    JOIN 'student_team.csv' AS ST ON ST.team_id = TM.team_id
    JOIN 'project.csv' AS P ON P.project_id = ST.project_id
    JOIN 'class_schedule.csv' AS T5 -- Aliased as T5 here for clarity
         ON T5.week_number = P.week_number   -- Same week
) AS T2 ON T2.schedule_id = T3.schedule_id
GROUP BY T1.instructor_id, T1.first_name, T1.last_name
ORDER BY students_taught DESC
LIMIT 1;
"""

con = duckdb.connect()
print("--- Running DuckDB Query for Q2: Most Popular Instructor (Students Taught) ---")

# Execute the SQL query
result = con.sql(KIMI_SQL_Q2)
result.show()

con.close()