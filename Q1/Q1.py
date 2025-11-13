# Q1.py - What is the course with the most number of students?

import duckdb

# SQL adapted to use CSV file names
KIMI_SQL_Q1 = """
SELECT T3.project_id,
       T3.title AS course_title,
       COUNT(DISTINCT T1.student_id) AS student_count
FROM 'team_member.csv' AS T1
JOIN 'student_team.csv' AS T2 
  ON T1.team_id = T2.team_id
JOIN 'project.csv' AS T3 
  ON T2.project_id = T3.project_id
GROUP BY T3.project_id, T3.title
ORDER BY student_count DESC
LIMIT 1;
"""

con = duckdb.connect()
print("--- Running DuckDB Query for Q1: Most Enrolled Course (Project) ---")

# Execute the SQL query
result = con.sql(KIMI_SQL_Q1)
result.show()

con.close()