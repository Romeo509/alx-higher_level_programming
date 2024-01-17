-- Display the top 3 cities' temperatures during July and August, ordered by temperature (descending)
SELECT `city`, AVG(`value`) AS `avg_temp` FROM `temperat'ures` WHERE `month` BETWEEN 7 AND 8 GROUP BY `city` ORDER BY `avg_temp` DESC LIMIT 3;
