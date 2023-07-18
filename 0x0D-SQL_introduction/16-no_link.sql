--Don't list rows without  name value
SELECT score, name FROM second_table
WHERE NOT name=null
ORDER BY score DESC;
