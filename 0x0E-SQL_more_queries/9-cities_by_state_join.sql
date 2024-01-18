-- Use INNER JOIN
SELECT cities.id AS city_id, cities.name AS city_name, states.name AS state_name
FROM hbtn_0d_usa.cities
JOIN hbtn_0d_usa.states ON cities.state_id = states.id
ORDER BY cities.id ASC;
