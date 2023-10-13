-- Script that ranks country origins of bands, ordered by the number of (non-unique) fans
SELECT country,
  COUNT(*) AS fans
FROM bands
  JOIN users ON bands.fan_id = users.id
GROUP BY country
ORDER BY fans DESC;
