-- Write query to get number of graded assignments for each student:
select student_id, count(*) as no_graded 
from assignments 
where state = 'GRADED' 
group by student_id;