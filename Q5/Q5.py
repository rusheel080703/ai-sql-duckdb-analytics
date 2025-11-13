# Q5.py - Total pay for Instructor X (Grace Hopper, ID 1)

import duckdb

# Set the ID for Instructor X (Grace Hopper)
INSTRUCTOR_X_ID = 1

KIMI_SQL_Q5 = f"""
-- Total pay for instructor X (ID {INSTRUCTOR_X_ID})
SELECT T1.instructor_id,
       T1.first_name,
       T1.last_name,
       COALESCE(teach.hours, 0)  AS teaching_hours,
       COALESCE(super.hours, 0)  AS supervision_hours,
       COALESCE(teach.pay,  0)   AS teaching_pay_usd,
       COALESCE(super.pay,  0)   AS supervision_pay_usd,
       COALESCE(teach.pay, 0) + COALESCE(super.pay, 0) AS total_pay_usd
FROM 'instructor.csv' AS T1
LEFT JOIN (
    /* teaching pay */
    SELECT T2.instructor_id,
           -- FIX: Convert 'HH:MM:SS' strings to TIMESTAMP before calculating the difference in hours
           SUM(date_part('epoch', 
               (strptime('2000-01-01 ' || T2.end_time, '%Y-%m-%d %H:%M:%S') - 
                strptime('2000-01-01 ' || T2.start_time, '%Y-%m-%d %H:%M:%S'))
           )) / 3600 AS hours,
           
           SUM(date_part('epoch', 
               (strptime('2000-01-01 ' || T2.end_time, '%Y-%m-%d %H:%M:%S') - 
                strptime('2000-01-01 ' || T2.start_time, '%Y-%m-%d %H:%M:%S'))
           )) / 3600 * T3.teaching_rate_usd AS pay
    FROM 'class_schedule.csv' AS T2
    JOIN 'instructor.csv' AS T3 ON T3.instructor_id = T2.instructor_id
    GROUP BY T2.instructor_id, T3.teaching_rate_usd 
) teach ON T1.instructor_id = teach.instructor_id
LEFT JOIN (
    /* supervision pay */
    SELECT T4.instructor_id,
           SUM(T4.hours_logged) AS hours,
           SUM(T4.hours_logged) * T5.supervision_rate_usd AS pay
    FROM 'project_supervision.csv' AS T4
    JOIN 'instructor.csv' AS T5 ON T5.instructor_id = T4.instructor_id
    GROUP BY T4.instructor_id, T5.supervision_rate_usd 
) super ON T1.instructor_id = super.instructor_id
WHERE T1.instructor_id = {INSTRUCTOR_X_ID};
"""

con = duckdb.connect()
print(f"--- Running DuckDB Query for Q5: Payroll for Instructor ID {INSTRUCTOR_X_ID} ---")

# Execute the SQL query
result = con.sql(KIMI_SQL_Q5)
result.show()

con.close()