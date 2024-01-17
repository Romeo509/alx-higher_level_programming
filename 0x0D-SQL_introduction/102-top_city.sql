-- Display the top 3 cities' temperatures during July and August, ordered by temperature (descending)
SELECT city, AVG(temperature) AS avg_temp
FROM temperature_data
WHERE month IN ('July', 'August')
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
