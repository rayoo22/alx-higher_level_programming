-- displays top 3 cities between July and August
SELECT temperatures.city, AVG(temperatures.value) AS avg_temp FROM temperatures WHERE temperatures.month in (7, 8) GROUP BY temperatures.city ORDER BY avg_temp DESC LIMIT 3;
