SELECT
    case
        WHEN a + b <= c OR a + c <= b OR b + c <= a THEN 'Not A Triangle'
        WHEN a=b and a=c and b=c then 'Equilateral'
        when a<>b and b<>c and a<>c then 'Scalene'
        else 'Isosceles'
     end
from TRIANGLES;