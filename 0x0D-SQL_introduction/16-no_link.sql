-- Don't list rows without  name value
SELECT score, name FROM second_table
WHERE NOT name=""
ORDER BY score DESC;
