# Write your MySQL query statement below
with cte as(
select e.name as e,d.name as d,e.salary, DENSE_RANk () over (partition by e.departmentId order by e.Salary desc) as rnk 
from Employee e join Department d on e.departmentId=d.id 
)
select c.e as Department,c.d as Employee,c.salary from cte c where rnk=1;