SELECT COUNT(*),
       icd_code
FROM cdc_mortality
WHERE race == ?
GROUP BY icd_code
ORDER BY 1 DESC LIMIT 10
