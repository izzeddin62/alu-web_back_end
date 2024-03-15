-- Title: Time Together
SELECT
    band_name,
    CASE
        WHEN split IS NULL THEN YEAR(curdate()) - COALESCE(formed, YEAR(curdate()))
        ELSE COALESCE(split, YEAR(curdate())) - COALESCE(formed, YEAR(curdate()))
    END AS time_together
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY time_together DESC;