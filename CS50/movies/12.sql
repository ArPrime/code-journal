SELECT movies.title
FROM movies
JOIN stars ON stars.movie_id = movies.id
JOIN people ON stars.person_id = people.id
WHERE people.name in ('Bradley Cooper', 'Jennifer Lawrence')
GROUP BY movies.title
HAVING COUNT(people.name) = 2;
