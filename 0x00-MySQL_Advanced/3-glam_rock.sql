-- script that lists all bands with Glam rock as their main style, ranked by their longevity
SELECT name,
  longevity
FROM bands
  JOIN styles ON bands.style_id = styles.id
WHERE styles.name = 'Glam rock'
ORDER BY longevity DESC;
