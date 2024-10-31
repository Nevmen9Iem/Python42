# SELECT
# db.user_id,
# db.`level` ,
# db.period
# FROM itstep_bot.data_tb as db
# WHERE db.period = 1 and `level` =  1

# SELECT
# COUNT(*) as countRow
# FROM itstep_bot.data_tb as db

# SELECT
# --COUNT(*) as countRow
# distinct(db.period)
# FROM itstep_bot.data_tb as db
# order by 1 ASC

# SELECT
# --COUNT(*) as countRow
# count(distinct(db.period) )
# FROM itstep_bot.data_tb as db
# order by 1 ASC

# SELECT
# --COUNT(*) as countRow
# distinct(db.period)
# FROM itstep_bot.data_tb as db
# WHERE db.period in (1,5,10,22,30)
# order by 1 ASC / desc
# -- count user period => 5,10,15,25, level = 2, 3

# SELECT
# --COUNT(*) as countRow
# --distinct(db.period)
# count(db.user_id) as countUsers,
# round(count(db.user_id)) AS iniqUsers,
# FROM itstep_bot.data_tb as db
# WHERE db.period in (1,5,10,15,20,25) AND db.`level`  IN (2,3)
# --order by 1 ASC
#
# -- count user period => 5,10,15,25, level = 2, 3
# select
# round(max(db.payment_sum),2) as maxPrice,
# min(db.payment_sum) as sumPrice
# FROM itstep_bot.data_tb as db
#
# --2 count user period => 5,10,15,20,25, level = 2,3 => sum => avg sum
# SELECT
# count(db.user_id) as countUsers,
# count(DISTINCT (db.user_id)) as uniqUsers,
# round(sum(db.payment_sum),2) as sumUser,
# round(sum(db.payment_sum)/count(DISTINCT (db.user_id)),2) as avgsumUser,
# round(AVG(db.payment_sum),2) as avgAVG
# --distinct(db.period)
# FROM itstep_bot.data_tb as db
# WHERE db.period in (5,10,15,20,25) and db.`level` in (2,3)

SELECT
# --COUNT(*) as countRow
# --distinct(db.period)
# count(db.user_id) as countUsers,
# round(count(db.user_id)) AS iniqUsers,
# FROM itstep_bot.data_tb as db
# WHERE db.period in (1,5,10,15,20,25) AND db.`level`  IN (2,3)
# --order by 1 ASC / desc
#
# -- count user period => 5,10,15,25, level = 2, 3
# select
# round(max(db.payment_sum),2) as maxPrice,
# min(db.payment_sum) as sumPrice
# FROM itstep_bot.data_tb as db
#
# --2 count user period => 5,10,15,20,25, level = 2,3 => sum => avg sum
# SELECT
# count(db.user_id) as countUsers,
# count(DISTINCT (db.user_id)) as uniqUsers,
# round(sum(db.payment_sum),2) as sumUser,
# round(sum(db.payment_sum)/count(DISTINCT (db.user_id)),2) as avgsumUser,
# round(AVG(db.payment_sum),2) as avgAVG
# --distinct(db.period)
# FROM itstep_bot.data_tb as db
# WHERE db.period in (5,10,15,20,25) and db.`level` in (2,3)
#
# ---------------------
# SELECT
# round(sum(db.payment_sum),2) AS sumSum,
# round(sum(db.payment_sum)/2,2) AS divideSum,
# round(sum(db.payment_sum)*2,2) AS multiSum,
# round(POWER(sum(db.payment_sum),2),2) AS powerSum,
# round(SQRT(sum(db.payment_sum)),2) AS sqrtSum,
# FROM itstep_bot.data_tb AS db
#
# ---------------------
# SELECT
# db.period ,
# COUNT(db.period) AS countPeriod,
# round(sum(db.payment_sum),2) AS sumPayment
# FROM itstep_bot.data_tb AS db
# GROUP BY db.period
# ORDER BY 2 DESC
# --LIMIT 5
#
# -------------------------------
# --group by => period, level => user_id
# --top 10 count user 10
# SELECT
# db.period ,
# db.`level` ,
# COUNT(db.user_id) AS countPeriod,
# round(sum(db.payment_sum),2) AS sumPayment
# FROM itstep_bot.data_tb AS db
# GROUP BY db.period, db.`level`
# ORDER BY 1, 3 DESC
# LIMIT 10
#
# ----------------------------------
# SELECT *
# DATETIME
# date_format(db.pay_date,"%y")
# FROM itstep_bot.data_tb AS db