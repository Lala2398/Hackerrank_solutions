-- Select All

SELECT * From CITY 


-- Japanese Cities' Attributes

SELECT * FROM CITY
WHERE COUNTRYCODE = 'JPN';

-- Japanese Cities' Names

SELECT NAME from CITY 
WHERE COUNTRYCODE = 'JPN';

--Weather Observation Station 1

select city, state from station;

-- Weather Observation Station 3

SELECT DISTINCT CITY
FROM STATION
WHERE MOD(ID, 2) = 0;

--Weather Observation Station 4 

SELECT (COUNT(CITY) - COUNT(DISTINCT CITY))
FROM STATION;
