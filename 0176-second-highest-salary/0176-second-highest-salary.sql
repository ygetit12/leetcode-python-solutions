# Write your MySQL query statement below
/*Select max(salary) as SecondHighestSalary 
from Employee where salary < (select max(salary) from Employee);

*/
with cte as 
(select *,DENSE_RANK() Over( order by salary desc) as rnk from Employee
) 
select 
MAX(salary)
as SecondHighestSalary from cte where rnk =2;