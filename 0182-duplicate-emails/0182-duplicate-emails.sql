# Write your MySQL query statement below
Select email as Email  from Person p group by email having count(id)>1;