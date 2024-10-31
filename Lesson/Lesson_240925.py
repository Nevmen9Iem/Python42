SELECT *
FROM itstep_bot.data_tb as db
WHERE db.cnt_click_contacts >= 100 and db.cnt_click_contacts <= 500


SELECT *
im.manager_id
from itstep_bot.id_manager as im


SELECT *
from itstep_bot.data_tb as db
WHERE db.period in (
SELECT DISTINCT(im.manager_id) from itstep_bot.id_manager as im WHERE im.manager_id = 3
)
and db.`level` > 10


--Перевірити чи є співпадіння по user_id в базах dta_base і base_tb (user_id/id_client => data_base and data_tb)

SELECT *
FROM itstep_bot.data_tb as dt


SELECT *
from itstep_bot.data_tb as db



SELECT *
FROM 
(
	SELECT DISTINCT(dt.user_id) AS IDuser1
	FROM itstep_bot.data_tb  as dt
) t1
INNER Join(
	SELECT DISTINCT(db.id_client) AS IDuser2
	FROM itstep_bot.data_base as db
) AS t2 on t1.IDuser1 = t2.IDuser2


SELECT count(t1.IDuser)
FROM
(
	SELECT DISTINCT(dt.user_id) AS IDuser
	FROM itstep_bot.data_tb as dt
) t1
INNER JOIN (
	SELECT DISTINCT(db.id_client) AS IDuser
	FROM itstep_bot.data_base as db
) AS t2 ON t1.IDuser= t2.IDuser

------------------------------------------------

SELECT *
FROM 
	(
		SELECT DISTINCT(dt.user_id) AS IDuser1
		FROM itstep_bot.data_tb  as dt
	) AS t1
INNER Join
	(
		SELECT DISTINCT(db.id_client) AS IDuser2
		FROM itstep_bot.data_base as db
	) AS t2 
ON t1.IDuser1 = t2.IDuser2
WHERE t2.IDuser2 IS NOT NULL 
ORDER  BY 1 ASC

------------------------------------------------

-- user_id/id_client => data_base (id_city) and data_tb (payment_sum)

SELECT t1.IDuser1,t1.sumTotal,t2.UserCity
FROM
		(
			SELECT DISTINCT(dt.user_id) AS IDuser1,
			sum(dt.payment_sum) AS sumTotal
			FROM itstep_bot.data_tb as dt
			GROUP BY IDuser1
			--HAVING IDuser1=10849
		) AS t1
INNER JOIN
		(
			SELECT DISTINCT(db.id_client) AS IDuser2,
			db.id_city AS UserCity
			FROM itstep_bot.data_base as db
			--WHERE db.id_client=10849
		) AS t2
ON t1.IDuser1 = t2.IDuser2
--WHERE t2.IDuser2 IS NOT NULL
ORDER BY 1 asc


----------------------------------------------------
--з якогог міста користувачів найбільше

SELECT
t2.UserCity,
count(t2.UserCity) AS countUserbyCity
FROM
		(
			SELECT DISTINCT(dt.user_id) AS IDuser1,
			sum(dt.payment_sum) AS sumTotal
			FROM itstep_bot.data_tb as dt
			GROUP BY IDuser1
		) AS t1
INNER JOIN
		(
			SELECT DISTINCT(db.id_client) AS IDuser2,
			db.id_city AS UserCity
			FROM itstep_bot.data_base as db
		) AS t2
ON t1.IDuser1 = t2.IDuser2
GROUP BY t2.UserCity
ORDER BY 2 desc
LIMIT 5

-----------------------------------------------------
-- визначити загальну суму по містам

SELECT
t2.UserCity,
count(t2.UserCity) AS countUserbyCity,
sum(t1.sumTotal) AS sumbyCity
FROM
		(
			SELECT DISTINCT(dt.user_id) AS IDuser1,
			sum(dt.payment_sum) AS sumTotal
			FROM itstep_bot.data_tb as dt
			GROUP BY IDuser1
		) AS t1
INNER JOIN
		(
			SELECT DISTINCT(db.id_client) AS IDuser2,
			db.id_city AS UserCity
			FROM itstep_bot.data_base as db
					) AS t2
ON t1.IDuser1= t2.IDuser2
GROUP BY t2.UserCity
ORDER BY 3 desc
LIMIT 5

------------------------------------------------------