select sc.课程 from SC
group by sc.课程
having count(*) > 5