# Q3.py - Who is the most popular instructor (highest rating)?

import duckdb

# SQL adapted to use CSV file names
KIMI_SQL_Q3 = """
SELECT T1.instructor_id,
       T1.first_name,
       T1.last_name,
       AVG(T2.stars) AS avg_rating
FROM 'instructor.csv' AS T1
JOIN 'rating.csv' AS T2
      ON T2.rated_type = 'instructor'
     AND T2.rated_id   = T1.instructor_id
GROUP BY T1.instructor_id, T1.first_name, T1.last_name
ORDER BY avg_rating DESC
LIMIT 1;
"""

con = duckdb.connect()
print("--- Running DuckDB Query for Q3: Most Popular Instructor (Rating) ---")

# Execute the SQL query
result = con.sql(KIMI_SQL_Q3)
result.show()

con.close()