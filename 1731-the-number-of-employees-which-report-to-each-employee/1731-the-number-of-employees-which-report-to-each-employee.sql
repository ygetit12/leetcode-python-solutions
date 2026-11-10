-- # Write your MySQL query statement below
-- Select e1.employee_id,e1.name,e2.count(e2.employee_id) as reports_count,
-- round(AVG(e2.age)) as average_age from Employees e1 join Employees e2 using e1.employee_id =e2.reports_to group by e1.employee_id,e1.name order b e1.employee_id;

SELECT e1.employee_id, e1.name,COUNT(e2.employee_id) AS reports_count,ROUND(AVG(e2.age)) AS average_age FROM Employees e1 JOIN Employees e2 ON e1.employee_id = e2.reports_to
GROUP BY e1.employee_id, e1.name ORDER BY e1.employee_id;