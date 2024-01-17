-- Display the max temperature of each state, ordered by state name
SELECT state, MAX(temperature) AS max_temp
FROM temperature_data
GROUP BY state
ORDER BY state;
