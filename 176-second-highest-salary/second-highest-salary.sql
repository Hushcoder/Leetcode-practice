# Write your MySQL query statement below

### if subquery fails to return a value it explicitly returns null
Select (
select distinct salary
from employee 
order by salary DESC
LIMIT 1 OFFSET 1)
AS SecondHighestSalary;