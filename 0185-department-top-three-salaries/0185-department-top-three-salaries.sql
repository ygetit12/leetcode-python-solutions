# Write your MySQL query statement below

with cte as (
    select e.name as e,d.name as d,e.salary,DENSE_RANK() OVER(partition by departmentId order by salary desc) as rnk
    from Employee e join Department d on e.departmentId=d.id
)
select d as Department,e as Employee, salary from cte where rnk in (1,2,3);