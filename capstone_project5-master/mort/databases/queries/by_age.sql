SELECT COUNT(*),
       icd_code
FROM cdc_mortality
WHERE age_code == '1'
  AND age == ?
GROUP BY icd_code
ORDER BY 1 DESC LIMIT 10
