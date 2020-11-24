Premise:
You have a table with one column, `original_date`, of datatype string
 ORIGINAL_DATE 
20190825
20190826
20190827
20190828
20190829
20190830
20190831
20190901

Question:
Write a SQL query to calculate two more columns –

    `end_of_week ` - the date of the next Sunday from `original_date`. If `original_date` is already a Sunday, this field should be the same value
    `end_of_month ` - the value of the end of month date

An acceptable solution is one which works for any valid date in the string format of `original_date`.
With end_of_month and end_of_week computed  ORIGINAL_DATE  	 END_OF_WEEK  	 END_OF_MONTH 
20190825 	20190825 	20190831
20190826 	20190901 	20190831
20190827 	20190901 	20190831
20190828 	20190901 	20190831
20190829 	20190901 	20190831
20190830 	20190901 	20190831
20190831 	20190901 	20190831
20190901 	20190901 	20190930

Additional Info:

20190825 is a Sunday, so the `end_of_week` for that value is still that same date.

20190827 is a Tuesday, and the next Sunday is on 20190901

 

 
Database
CREATE TABLE random_dates ( 
  original_date VARCHAR(8) NOT NULL 
);
INSERT INTO random_dates(original_date) values('20190825');
INSERT INTO random_dates(original_date) values('20190826');
INSERT INTO random_dates(original_date) values('20190827');
INSERT INTO random_dates(original_date) values('20190828');
INSERT INTO random_dates(original_date) values('20190829');
INSERT INTO random_dates(original_date) values('20190830');
INSERT INTO random_dates(original_date) values('20190831');
INSERT INTO random_dates(original_date) values('20190901');

Expected Output
20190825	2019-08-25	2019-08-31

20190826	2019-09-01	2019-08-31

20190827	2019-09-01	2019-08-31

20190828	2019-09-01	2019-08-31

20190829	2019-09-01	2019-08-31

20190830	2019-09-01	2019-08-31

20190831	2019-09-01	2019-08-31

20190901	2019-09-01	2019-09-30



SELECT 
original_date,
    case 
        when MOD(TO_CHAR(TO_DATE(original_date,'yyyymmdd'), 'J'), 7) + 1 =7 
            then TO_CHAR(TO_DATE(original_date,'yyyymmdd'),'yyyy-mm-dd') 
        else 
            TO_CHAR(TRUNC(TO_DATE(original_date,'yyyymmdd'), 'D') + 7, 'yyyy-mm-dd')
    end "END_OF_WEEK",
TO_CHAR(LAST_DAY(TO_DATE(original_date,'yyyymmdd')), 'yyyy-mm-dd') "END_OF_MONTH"
     FROM random_dates; 













================================== 

=================================

Restaurants in the area serve various food to customers. As long as customers keep showing up to a restaurant regularly, that restaurant will keep serving the same dish. If no customers visit a restaurant for more than 3 days, then that restaurant will serve a new type of food starting when the next customer visits. Unfortunately, some ingredients were contaminated and caused a few customers to suffer from food poisoning. The restaurants know which food was affected and are now trying to figure out which customers were affected. The restaurants keep their own catalogue of customers, so there is no guarantee that a customer has the same customer ID at each restaurant. All restaurants serve food in the same order. Figure out which customer ate which food.

Sample Data:

Restaurant:
restaurant_id 	customer_id 	visit_date
1 	1 	2020-01-01
2 	1 	2020-01-01
1 	2 	2020-01-03
3 	1 	2020-01-04
2 	2 	2020-01-14
3 	1 	2020-01-11
2 	3 	2020-01-14

Food:
food_id 	food_name
1 	Spaghetti
2 	Chicken and Rice
3 	Tacos

 

Desired:
Restaurant 	Customer 	Visit 	Food
1 	1 	2020-01-01 	Spaghetti
2 	1 	2020-01-01 	Spaghetti
1 	2 	2020-01-03 	Spaghetti
3 	1 	2020-01-04 	Spaghetti
2 	2 	2020-01-10 	Chicken and Rice
3 	1 	2020-01-11 	Chicken and Rice
2 	3 	2020-01-14 	Tacos

 

 

 
Database
drop table if exists restaurant;

CREATE TABLE restaurant ( 
  restaurant_id INTEGER NOT NULL,
  customer_id INTEGER NOT NULL,
  visit_date date NOT NULL
);

drop table if exists food;

CREATE TABLE food ( 
  food_id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
  food_name VARCHAR(60) NOT NULL
);

#reference data for food names
insert into food values (null, 'Spaghetti');
insert into food values (null, 'Chicken and rice');
insert into food values (null, 'Tacos');
insert into food values (null, 'Green chile stew');
insert into food values (null, 'Frito, apple, cherry, blueberry, and pumpkin pies');
insert into food values (null, 'BLT');
insert into food values (null, 'Barbecue ribs');
insert into food values (null, 'Indian frybread');
insert into food values (null, 'Buffalo wings');
insert into food values (null, 'Lobster');
insert into food values (null, 'Spaghetti');
insert into food values (null, 'New Mexican flat enchiladas');
insert into food values (null, 'New England clam chowder');
insert into food values (null, 'Fried chicken and waffles');
insert into food values (null, 'Peanut butter sandwich');
insert into food values (null, 'Cioppino');
insert into food values (null, 'Cheeseburger');
insert into food values (null, 'Maryland crabcakes');
insert into food values (null, 'Macaroni and cheese');
insert into food values (null, 'Chili with beans');
insert into food values (null, 'Grits');
insert into food values (null, 'Meatloaf');
insert into food values (null, 'Wild Alaska salmon');
insert into food values (null, 'Chicken fried steak');
insert into food values (null, 'Smithfield ham');
insert into food values (null, 'Jambalaya');
insert into food values (null, 'Reuben sandwich');
insert into food values (null, 'Fajitas');
insert into food values (null, 'Pot roast');
insert into food values (null, 'Cobb salad');
insert into food values (null, 'Hot dogs');
insert into food values (null, 'Philly cheese steak');
insert into food values (null, 'Nachos and cheese');

insert into restaurant values (1, 1, cast('2020-01-01' as date));
insert into restaurant values (2, 1, cast('2020-01-01' as date));
insert into restaurant values (1, 2, cast('2020-01-03' as date));
insert into restaurant values (3, 1, cast('2020-01-04' as date));
insert into restaurant values (2, 2, cast('2020-01-10' as date));
insert into restaurant values (4, 1, cast('2020-01-11' as date));
insert into restaurant values (3, 1, cast('2020-01-11' as date));
insert into restaurant values (2, 3, cast('2020-01-14' as date));

insert into restaurant values (5, 1, cast('2010-01-01' as date));
insert into restaurant values (5, 2, cast('2012-01-01' as date));
insert into restaurant values (5, 3, cast('2014-01-01' as date));
insert into restaurant values (5, 4, cast('2016-01-01' as date));
insert into restaurant values (5, 5, cast('2018-01-01' as date));
insert into restaurant values (5, 6, cast('2020-01-01' as date));

insert into restaurant values (6, 1, cast('2019-12-04' as date));
insert into restaurant values (6, 2, cast('2019-12-04' as date));
insert into restaurant values (6, 1, cast('2019-12-04' as date));
insert into restaurant values (6, 1, cast('2019-12-07' as date));
insert into restaurant values (6, 1, cast('2019-12-10' as date));
insert into restaurant values (6, 1, cast('2019-12-10' as date));
insert into restaurant values (6, 3, cast('2019-12-10' as date));
insert into restaurant values (6, 1, cast('2019-12-13' as date));

insert into restaurant values( 7, 10, cast('2019-06-04' as date));
insert into restaurant values( 7, 11, cast('2019-06-08' as date));
insert into restaurant values( 7, 12, cast('2019-06-13' as date));
insert into restaurant values( 7, 13, cast('2019-06-19' as date));
insert into restaurant values( 7, 14, cast('2019-06-24' as date));
insert into restaurant values( 7, 15, cast('2019-06-28' as date));
insert into restaurant values( 7, 16, cast('2019-07-03' as date));
insert into restaurant values( 7, 17, cast('2019-07-09' as date));
insert into restaurant values( 7, 18, cast('2019-07-14' as date));
insert into restaurant values( 7, 19, cast('2019-07-18' as date));
insert into restaurant values( 7, 20, cast('2019-07-23' as date));
insert into restaurant values( 7, 21, cast('2019-07-29' as date));
insert into restaurant values( 7, 22, cast('2019-08-03' as date));
insert into restaurant values( 7, 23, cast('2019-08-07' as date));
insert into restaurant values( 7, 24, cast('2019-08-12' as date));
insert into restaurant values( 7, 25, cast('2019-08-18' as date));
insert into restaurant values( 7, 26, cast('2019-08-23' as date));
insert into restaurant values( 7, 27, cast('2019-08-27' as date));
insert into restaurant values( 7, 28, cast('2019-09-01' as date));
insert into restaurant values( 7, 29, cast('2019-09-07' as date));
insert into restaurant values( 7, 30, cast('2019-09-12' as date));
insert into restaurant values( 7, 31, cast('2019-09-16' as date));

insert into restaurant values( 8, 1, cast('2019-06-04' as date));
insert into restaurant values( 8, 2, cast('2019-06-05' as date));
insert into restaurant values( 8, 2, cast('2019-06-05' as date));
insert into restaurant values( 8, 2, cast('2019-06-05' as date));
insert into restaurant values( 8, 2, cast('2019-06-05' as date));
insert into restaurant values( 8, 1, cast('2019-06-07' as date));
insert into restaurant values( 8, 1, cast('2019-06-10' as date));
insert into restaurant values( 8, 2, cast('2019-06-11' as date));
insert into restaurant values( 8, 2, cast('2019-06-11' as date));
insert into restaurant values( 8, 2, cast('2019-06-14' as date));
insert into restaurant values( 8, 2, cast('2019-06-17' as date));
insert into restaurant values( 8, 3, cast('2019-06-18' as date));
insert into restaurant values( 8, 2, cast('2019-06-20' as date));
insert into restaurant values( 8, 2, cast('2019-06-23' as date));
insert into restaurant values( 8, 2, cast('2019-06-23' as date));
insert into restaurant values( 8, 2, cast('2019-06-23' as date));
insert into restaurant values( 8, 2, cast('2019-06-26' as date));
insert into restaurant values( 8, 1, cast('2019-06-28' as date));
insert into restaurant values( 8, 1, cast('2019-06-28' as date));
insert into restaurant values( 8, 3, cast('2019-06-30' as date));
insert into restaurant values( 8, 2, cast('2019-07-02' as date));
insert into restaurant values( 8, 2, cast('2019-07-02' as date));
insert into restaurant values( 8, 1, cast('2019-07-04' as date));
insert into restaurant values( 8, 3, cast('2019-07-06' as date));
insert into restaurant values( 8, 3, cast('2019-07-09' as date));
insert into restaurant values( 8, 1, cast('2019-07-10' as date));
insert into restaurant values( 8, 1, cast('2019-07-13' as date));
insert into restaurant values( 8, 1, cast('2019-07-16' as date));
insert into restaurant values( 8, 1, cast('2019-07-19' as date));
insert into restaurant values( 8, 3, cast('2019-07-21' as date));
insert into restaurant values( 8, 3, cast('2019-07-21' as date));
insert into restaurant values( 8, 3, cast('2019-07-24' as date));
insert into restaurant values( 8, 3, cast('2019-07-27' as date));
insert into restaurant values( 8, 2, cast('2019-07-29' as date));
insert into restaurant values( 8, 1, cast('2019-07-31' as date));
insert into restaurant values( 8, 1, cast('2019-07-31' as date));
insert into restaurant values( 8, 1, cast('2019-07-31' as date));
insert into restaurant values( 8, 1, cast('2019-07-31' as date));
insert into restaurant values( 8, 1, cast('2019-08-03' as date));
insert into restaurant values( 8, 1, cast('2019-08-06' as date));
insert into restaurant values( 8, 3, cast('2019-08-08' as date));
insert into restaurant values( 8, 1, cast('2019-08-09' as date));
insert into restaurant values( 8, 2, cast('2019-08-10' as date));
insert into restaurant values( 8, 3, cast('2019-08-11' as date));
insert into restaurant values( 8, 3, cast('2019-08-11' as date));
insert into restaurant values( 8, 3, cast('2019-08-14' as date));
insert into restaurant values( 8, 3, cast('2019-08-14' as date));
insert into restaurant values( 8, 3, cast('2019-08-17' as date));
insert into restaurant values( 8, 1, cast('2019-08-18' as date));
insert into restaurant values( 8, 1, cast('2019-08-21' as date));
insert into restaurant values( 8, 3, cast('2019-08-23' as date));
insert into restaurant values( 8, 3, cast('2019-08-26' as date));
insert into restaurant values( 8, 3, cast('2019-08-26' as date));
insert into restaurant values( 8, 2, cast('2019-08-28' as date));
insert into restaurant values( 8, 2, cast('2019-08-28' as date));
insert into restaurant values( 8, 2, cast('2019-08-28' as date));
insert into restaurant values( 8, 1, cast('2019-08-30' as date));
insert into restaurant values( 8, 1, cast('2019-08-30' as date));
insert into restaurant values( 8, 1, cast('2019-09-02' as date));
insert into restaurant values( 8, 2, cast('2019-09-03' as date));
insert into restaurant values( 8, 1, cast('2019-09-05' as date));
insert into restaurant values( 8, 2, cast('2019-09-06' as date));
insert into restaurant values( 8, 3, cast('2019-09-07' as date));
insert into restaurant values( 8, 3, cast('2019-09-10' as date));

insert into restaurant values( 9, 1, cast('2020-01-20' as date));
insert into restaurant values( 9, 2, cast('2020-01-20' as date));
insert into restaurant values( 9, 3, cast('2020-01-20' as date));
insert into restaurant values( 9, 4, cast('2020-01-20' as date));
insert into restaurant values( 9, 5, cast('2020-01-20' as date));
insert into restaurant values( 9, 6, cast('2020-01-20' as date));
insert into restaurant values( 9, 7, cast('2020-01-20' as date));
insert into restaurant values( 9, 8, cast('2020-01-20' as date));
insert into restaurant values( 9, 9, cast('2020-01-20' as date));
insert into restaurant values( 9, 10, cast('2020-01-20' as date));
insert into restaurant values( 9, 11, cast('2020-01-20' as date));
insert into restaurant values( 9, 12, cast('2020-01-20' as date));
insert into restaurant values( 9, 13, cast('2020-01-20' as date));
insert into restaurant values( 9, 14, cast('2020-01-20' as date));
insert into restaurant values( 9, 15, cast('2020-01-20' as date));
insert into restaurant values( 9, 16, cast('2020-01-20' as date));
insert into restaurant values( 9, 17, cast('2020-01-20' as date));
insert into restaurant values( 9, 18, cast('2020-01-20' as date));
insert into restaurant values( 9, 19, cast('2020-01-20' as date));
insert into restaurant values( 9, 20, cast('2020-01-20' as date));
insert into restaurant values( 9, 21, cast('2020-01-20' as date));
insert into restaurant values( 9, 22, cast('2020-01-20' as date));
insert into restaurant values( 9, 23, cast('2020-01-20' as date));
insert into restaurant values( 9, 24, cast('2020-01-20' as date));
insert into restaurant values( 9, 25, cast('2020-01-20' as date));
insert into restaurant values( 9, 26, cast('2020-01-20' as date));
insert into restaurant values( 9, 27, cast('2020-01-20' as date));
insert into restaurant values( 9, 28, cast('2020-01-20' as date));
insert into restaurant values( 9, 29, cast('2020-01-20' as date));
insert into restaurant values( 9, 30, cast('2020-01-20' as date));
insert into restaurant values( 9, 31, cast('2020-01-20' as date));
insert into restaurant values( 9, 32, cast('2020-01-20' as date));
insert into restaurant values( 9, 33, cast('2020-01-20' as date));
insert into restaurant values( 9, 34, cast('2020-01-20' as date));
insert into restaurant values( 9, 35, cast('2020-01-20' as date));
insert into restaurant values( 9, 36, cast('2020-01-20' as date));
insert into restaurant values( 9, 37, cast('2020-01-20' as date));
insert into restaurant values( 9, 38, cast('2020-01-20' as date));
insert into restaurant values( 9, 39, cast('2020-01-20' as date));
insert into restaurant values( 9, 40, cast('2020-01-20' as date));
insert into restaurant values( 9, 41, cast('2020-01-20' as date));
insert into restaurant values( 9, 42, cast('2020-01-20' as date));
insert into restaurant values( 9, 43, cast('2020-01-20' as date));
insert into restaurant values( 9, 44, cast('2020-01-20' as date));
insert into restaurant values( 9, 45, cast('2020-01-20' as date));
insert into restaurant values( 9, 46, cast('2020-01-20' as date));
insert into restaurant values( 9, 47, cast('2020-01-20' as date));
insert into restaurant values( 9, 48, cast('2020-01-20' as date));
insert into restaurant values( 9, 49, cast('2020-01-20' as date));
insert into restaurant values( 9, 50, cast('2020-01-20' as date));
insert into restaurant values( 9, 51, cast('2020-01-20' as date));
insert into restaurant values( 9, 52, cast('2020-01-20' as date));
insert into restaurant values( 9, 53, cast('2020-01-20' as date));
insert into restaurant values( 9, 54, cast('2020-01-20' as date));
insert into restaurant values( 9, 55, cast('2020-01-20' as date));
insert into restaurant values( 9, 56, cast('2020-01-20' as date));
insert into restaurant values( 9, 57, cast('2020-01-20' as date));
insert into restaurant values( 9, 58, cast('2020-01-20' as date));
insert into restaurant values( 9, 59, cast('2020-01-20' as date));
insert into restaurant values( 9, 60, cast('2020-01-20' as date));
insert into restaurant values( 9, 61, cast('2020-01-20' as date));
insert into restaurant values( 9, 62, cast('2020-01-20' as date));
insert into restaurant values( 9, 63, cast('2020-01-20' as date));
insert into restaurant values( 9, 64, cast('2020-01-20' as date));
insert into restaurant values( 9, 65, cast('2020-01-20' as date));
insert into restaurant values( 9, 66, cast('2020-01-20' as date));
insert into restaurant values( 9, 67, cast('2020-01-20' as date));
insert into restaurant values( 9, 68, cast('2020-01-20' as date));
insert into restaurant values( 9, 69, cast('2020-01-20' as date));
insert into restaurant values( 9, 70, cast('2020-01-20' as date));
insert into restaurant values( 9, 71, cast('2020-01-20' as date));
insert into restaurant values( 9, 72, cast('2020-01-20' as date));
insert into restaurant values( 9, 73, cast('2020-01-20' as date));
insert into restaurant values( 9, 74, cast('2020-01-20' as date));
insert into restaurant values( 9, 75, cast('2020-01-20' as date));
insert into restaurant values( 9, 76, cast('2020-01-20' as date));
insert into restaurant values( 9, 77, cast('2020-01-20' as date));
insert into restaurant values( 9, 78, cast('2020-01-20' as date));
insert into restaurant values( 9, 79, cast('2020-01-20' as date));
insert into restaurant values( 9, 80, cast('2020-01-20' as date));
insert into restaurant values( 9, 81, cast('2020-01-20' as date));
insert into restaurant values( 9, 82, cast('2020-01-20' as date));
insert into restaurant values( 9, 83, cast('2020-01-20' as date));
insert into restaurant values( 9, 84, cast('2020-01-20' as date));
insert into restaurant values( 9, 85, cast('2020-01-20' as date));
insert into restaurant values( 9, 86, cast('2020-01-20' as date));
insert into restaurant values( 9, 87, cast('2020-01-20' as date));
insert into restaurant values( 9, 88, cast('2020-01-20' as date));
insert into restaurant values( 9, 89, cast('2020-01-20' as date));
insert into restaurant values( 9, 90, cast('2020-01-20' as date));
insert into restaurant values( 9, 91, cast('2020-01-20' as date));
insert into restaurant values( 9, 92, cast('2020-01-20' as date));
insert into restaurant values( 9, 93, cast('2020-01-20' as date));
insert into restaurant values( 9, 94, cast('2020-01-20' as date));
insert into restaurant values( 9, 95, cast('2020-01-20' as date));
insert into restaurant values( 9, 96, cast('2020-01-20' as date));
insert into restaurant values( 9, 97, cast('2020-01-20' as date));
insert into restaurant values( 9, 98, cast('2020-01-20' as date));
insert into restaurant values( 9, 99, cast('2020-01-20' as date));
insert into restaurant values( 9, 100, cast('2020-01-20' as date));
Expected Output
1	1	2020-01-01	Spaghetti

1	2	2020-01-03	Spaghetti

2	1	2020-01-01	Spaghetti

2	2	2020-01-10	Chicken and rice

2	3	2020-01-14	Tacos

3	1	2020-01-04	Spaghetti

3	1	2020-01-11	Chicken and rice

4	1	2020-01-11	Spaghetti

5	1	2010-01-01	Spaghetti

5	2	2012-01-01	Chicken and rice

5	3	2014-01-01	Tacos

5	4	2016-01-01	Green chile stew

5	5	2018-01-01	Frito, apple, cherry, blueberry, and pumpkin pies

5	6	2020-01-01	BLT

6	1	2019-12-04	Spaghetti

6	2	2019-12-04	Spaghetti

6	1	2019-12-04	Spaghetti

6	1	2019-12-07	Spaghetti

6	1	2019-12-10	Spaghetti

6	1	2019-12-10	Spaghetti

6	3	2019-12-10	Spaghetti

6	1	2019-12-13	Spaghetti

7	10	2019-06-04	Spaghetti

7	11	2019-06-08	Chicken and rice

7	12	2019-06-13	Tacos

7	13	2019-06-19	Green chile stew

7	14	2019-06-24	Frito, apple, cherry, blueberry, and pumpkin pies

7	15	2019-06-28	BLT

7	16	2019-07-03	Barbecue ribs

7	17	2019-07-09	Indian frybread

7	18	2019-07-14	Buffalo wings

7	19	2019-07-18	Lobster

7	20	2019-07-23	Spaghetti

7	21	2019-07-29	New Mexican flat enchiladas

7	22	2019-08-03	New England clam chowder

7	23	2019-08-07	Fried chicken and waffles

7	24	2019-08-12	Peanut butter sandwich

7	25	2019-08-18	Cioppino

7	26	2019-08-23	Cheeseburger

7	27	2019-08-27	Maryland crabcakes

7	28	2019-09-01	Macaroni and cheese

7	29	2019-09-07	Chili with beans

7	30	2019-09-12	Grits

7	31	2019-09-16	Meatloaf

8	1	2019-06-04	Spaghetti

8	2	2019-06-05	Spaghetti

8	2	2019-06-05	Spaghetti

8	2	2019-06-05	Spaghetti

8	2	2019-06-05	Spaghetti

8	1	2019-06-07	Spaghetti

8	1	2019-06-10	Spaghetti

8	2	2019-06-11	Spaghetti

8	2	2019-06-11	Spaghetti

8	2	2019-06-14	Spaghetti

8	2	2019-06-17	Spaghetti

8	3	2019-06-18	Spaghetti

8	2	2019-06-20	Spaghetti

8	2	2019-06-23	Spaghetti

8	2	2019-06-23	Spaghetti

8	2	2019-06-23	Spaghetti

8	2	2019-06-26	Spaghetti

8	1	2019-06-28	Spaghetti

8	1	2019-06-28	Spaghetti

8	3	2019-06-30	Spaghetti

8	2	2019-07-02	Spaghetti

8	2	2019-07-02	Spaghetti

8	1	2019-07-04	Spaghetti

8	3	2019-07-06	Spaghetti

8	3	2019-07-09	Spaghetti

8	1	2019-07-10	Spaghetti

8	1	2019-07-13	Spaghetti

8	1	2019-07-16	Spaghetti

8	1	2019-07-19	Spaghetti

8	3	2019-07-21	Spaghetti

8	3	2019-07-21	Spaghetti

8	3	2019-07-24	Spaghetti

8	3	2019-07-27	Spaghetti

8	2	2019-07-29	Spaghetti

8	1	2019-07-31	Spaghetti

8	1	2019-07-31	Spaghetti

8	1	2019-07-31	Spaghetti

8	1	2019-07-31	Spaghetti

8	1	2019-08-03	Spaghetti

8	1	2019-08-06	Spaghetti

8	3	2019-08-08	Spaghetti

8	1	2019-08-09	Spaghetti

8	2	2019-08-10	Spaghetti

8	3	2019-08-11	Spaghetti

8	3	2019-08-11	Spaghetti

8	3	2019-08-14	Spaghetti

8	3	2019-08-14	Spaghetti

8	3	2019-08-17	Spaghetti

8	1	2019-08-18	Spaghetti

8	1	2019-08-21	Spaghetti

8	3	2019-08-23	Spaghetti

8	3	2019-08-26	Spaghetti

8	3	2019-08-26	Spaghetti

8	2	2019-08-28	Spaghetti

8	2	2019-08-28	Spaghetti

8	2	2019-08-28	Spaghetti

8	1	2019-08-30	Spaghetti

8	1	2019-08-30	Spaghetti

8	1	2019-09-02	Spaghetti

8	2	2019-09-03	Spaghetti

8	1	2019-09-05	Spaghetti

8	2	2019-09-06	Spaghetti

8	3	2019-09-07	Spaghetti

8	3	2019-09-10	Spaghetti

9	1	2020-01-20	Spaghetti

9	2	2020-01-20	Spaghetti

9	3	2020-01-20	Spaghetti

9	4	2020-01-20	Spaghetti

9	5	2020-01-20	Spaghetti

9	6	2020-01-20	Spaghetti

9	7	2020-01-20	Spaghetti

9	8	2020-01-20	Spaghetti

9	9	2020-01-20	Spaghetti

9	10	2020-01-20	Spaghetti

9	11	2020-01-20	Spaghetti

9	12	2020-01-20	Spaghetti

9	13	2020-01-20	Spaghetti

9	14	2020-01-20	Spaghetti

9	15	2020-01-20	Spaghetti

9	16	2020-01-20	Spaghetti

9	17	2020-01-20	Spaghetti

9	18	2020-01-20	Spaghetti

9	19	2020-01-20	Spaghetti

9	20	2020-01-20	Spaghetti

9	21	2020-01-20	Spaghetti

9	22	2020-01-20	Spaghetti

9	23	2020-01-20	Spaghetti

9	24	2020-01-20	Spaghetti

9	25	2020-01-20	Spaghetti

9	26	2020-01-20	Spaghetti

9	27	2020-01-20	Spaghetti

9	28	2020-01-20	Spaghetti

9	29	2020-01-20	Spaghetti

9	30	2020-01-20	Spaghetti

9	31	2020-01-20	Spaghetti

9	32	2020-01-20	Spaghetti

9	33	2020-01-20	Spaghetti

9	34	2020-01-20	Spaghetti

9	35	2020-01-20	Spaghetti

9	36	2020-01-20	Spaghetti

9	37	2020-01-20	Spaghetti

9	38	2020-01-20	Spaghetti

9	39	2020-01-20	Spaghetti

9	40	2020-01-20	Spaghetti

9	41	2020-01-20	Spaghetti

9	42	2020-01-20	Spaghetti

9	43	2020-01-20	Spaghetti

9	44	2020-01-20	Spaghetti

9	45	2020-01-20	Spaghetti

9	46	2020-01-20	Spaghetti

9	47	2020-01-20	Spaghetti

9	48	2020-01-20	Spaghetti

9	49	2020-01-20	Spaghetti

9	50	2020-01-20	Spaghetti

9	51	2020-01-20	Spaghetti

9	52	2020-01-20	Spaghetti

9	53	2020-01-20	Spaghetti

9	54	2020-01-20	Spaghetti

9	55	2020-01-20	Spaghetti

9	56	2020-01-20	Spaghetti

9	57	2020-01-20	Spaghetti

9	58	2020-01-20	Spaghetti

9	59	2020-01-20	Spaghetti

9	60	2020-01-20	Spaghetti

9	61	2020-01-20	Spaghetti

9	62	2020-01-20	Spaghetti

9	63	2020-01-20	Spaghetti

9	64	2020-01-20	Spaghetti

9	65	2020-01-20	Spaghetti

9	66	2020-01-20	Spaghetti

9	67	2020-01-20	Spaghetti

9	68	2020-01-20	Spaghetti

9	69	2020-01-20	Spaghetti

9	70	2020-01-20	Spaghetti

9	71	2020-01-20	Spaghetti

9	72	2020-01-20	Spaghetti

9	73	2020-01-20	Spaghetti

9	74	2020-01-20	Spaghetti

9	75	2020-01-20	Spaghetti

9	76	2020-01-20	Spaghetti

9	77	2020-01-20	Spaghetti

9	78	2020-01-20	Spaghetti

9	79	2020-01-20	Spaghetti

9	80	2020-01-20	Spaghetti

9	81	2020-01-20	Spaghetti

9	82	2020-01-20	Spaghetti

9	83	2020-01-20	Spaghetti

9	84	2020-01-20	Spaghetti

9	85	2020-01-20	Spaghetti

9	86	2020-01-20	Spaghetti

9	87	2020-01-20	Spaghetti

9	88	2020-01-20	Spaghetti

9	89	2020-01-20	Spaghetti

9	90	2020-01-20	Spaghetti

9	91	2020-01-20	Spaghetti

9	92	2020-01-20	Spaghetti

9	93	2020-01-20	Spaghetti

9	94	2020-01-20	Spaghetti

9	95	2020-01-20	Spaghetti

9	96	2020-01-20	Spaghetti

9	97	2020-01-20	Spaghetti

9	98	2020-01-20	Spaghetti

9	99	2020-01-20	Spaghetti

9	100	2020-01-20	Spaghetti



CREATE TABLE restaurant(
restaurant_id number(10),
customer_id number(10),
visit_date date
);

insert into restaurant(restaurant_id,customer_id,visit_date) values(1,1,TO_DATE('2020-01-01','yyyy-mm-dd'));
insert into restaurant(restaurant_id,customer_id,visit_date) values(2,1,TO_DATE('2020-01-01','yyyy-mm-dd'));
insert into restaurant(restaurant_id,customer_id,visit_date) values(1,2,TO_DATE('2020-01-03','yyyy-mm-dd'));
insert into restaurant(restaurant_id,customer_id,visit_date) values(3,1,TO_DATE('2020-01-04','yyyy-mm-dd'));
insert into restaurant(restaurant_id,customer_id,visit_date) values(2,2,TO_DATE('2020-01-14','yyyy-mm-dd'));
insert into restaurant(restaurant_id,customer_id,visit_date) values(3,1,TO_DATE('2020-01-11','yyyy-mm-dd'));
insert into restaurant(restaurant_id,customer_id,visit_date) values(2,3,TO_DATE('2020-01-14','yyyy-mm-dd'));
commit;
CREATE TABLE food(
food_id number,
food_name varchar(50)
);

insert into food(food_id,food_name) values(1,'Spaghetti');
insert into food(food_id,food_name) values(2,'Chicken and Rice');
insert into food(food_id,food_name) values(3,'Tacos');
commit;

select r.*, f.food_name, 
    count(*) over(PARTITION BY restaurant_id,customer_id,visit_date) food 
    from restaurant r, food f 
        group by restaurant_id,customer_id,visit_date,food_name;




===================================================
333333333333333333333333333333333333333333333333333
===================================================



Premise:

Tracy has a file that contains a list of actors and the movies in which they acted. She wants to know the top 3 ranked actors from her list whom have acted/appeared in the most movies.
ACTOR_NAME 	MOVIE_NAME
Leonardo DiCaprio 	The Revenant
Christian Bale 	Vice
Morgan Freeman 	Shawshank Redemption
Leonardo DiCaprio 	The Great Gatsby
Christian Bale 	American Psycho
Morgan Freeman 	The Dark Knight
Christian Bale 	The Dark Knight
Samuel L. Jackson 	Pulp Fiction

Question:
Write code in Java/Scala/Python to display the top 3 ranked actors appearing in the most movies based on the count of movies in which they have acted. If there are less than 3 actors in her list, display all of them.

Consider all scenarios - such as, if two actors have acted in the same number of movies, they will have the same rank.

Input Explanation

The first line of input is always an integer denoting how many lines to read after the first line. In our sample test case, we have 7 in the first line and 7 lines after the first line, each having an actor name and movie name. 

In each data line, the actor name and movie name are separated by a ','(comma).

Input

8
Leonardo DiCaprio,The Revenant
Christian Bale,Vice
Morgan Freeman,Shawshank Redemption
Leonardo DiCaprio,The Great Gatsby
Christian Bale,American Psycho
Morgan Freeman,The Dark Knight
Christian Bale,The Dark Knight
Samuel L. Jackson,Pulp Fiction

 

Output Explanation

Print the top actor names to standard output in alphabetical order. You should not have counts in the output, only actor names

Output

Christian Bale
Leonardo DiCaprio
Morgan Freeman




import sys

actor_count = {}
actors = []
movies = []
actor_movie = {}
#For each line
n = int(sys.stdin.readline())
for i in range(n):
    line = sys.stdin.readline().rstrip()
    actors.append(line.split(',')[0])
    movies.append(line.split(',')[1])

#print("act: " ,  actors)
#print("mov: " , movies)

for act in range(len(actors)):
  #print( act, actors[act], movies[act]  )
  if not actors[act] in actor_count.keys():
    actor_count[actors[act]] = 1
    actor_movie[actors[act]] = [ movies[act] ]
  else:
    actor_count[actors[act]] += 1
    actor_movie[actors[act]].append(movies[act])
    
actor_count = sorted(actor_count.keys(), key=lambda x: x[1], reverse=True)

for act in sorted( actor_count )[:3]:
  print( act) 
  #print(act, actor_movie[act])
  
  
  
  
=====================================================================
44444444444444444444444444444444444444444444444444444444444444444
======================================================================

Premise:

Adam is so good at playing arcade games that he will win at every game he plays. One fine day as he was walking on the street, he discovers an arcade store that pays real cash for every game that the player wins - however, the store will only pay out once per game. The store has some games for which they will pay winners, and each game has its own completion time and payout rate. Thrilled at the prospect of earning money for his talent, Adam walked into the store only to realize that the store closes in 2 hours (exactly 120 minutes). Knowing that he cannot play all the games in that time, he decides to pick the games that maximize his earnings 
Sample game board at the arcade GAME 	COMPLETION_TIME
(in minutes) 	PAYOUT_RATE
Pac-man 	90 	400
Mortal Kombat 	10 	30
Super Tetris 	25 	100
Pump it Up 	10 	40
Street Fighter II 	90 	450
Speed Racer 	10 	40


An acceptable solution is the one where it still picks the best earnings even when the list of games or completion times or payout rates change. 

Question:
Write code in Java/Scala/Python to help Adam pick the sequence(s) of games that earn him the most money.

Then, assume you have a variable list of games and their payout rates. What is the best way to pick the games that earn you the most?

Input Explanation

The first line of input is always an integer denoting many lines to read after the first line. In our sample test case, we have 6 in the first line and 6 lines after the first line, each having a game, completion_time and payout_rate. 

In each data line, the game, completion_time and payout_rate are separated by a ','(comma).

The games board may change but the store still closes in 120 minutes. 

Input

6
Pac-man,80,400
Mortal Kombat,10,30
Super Tetris,25,100
Pump it Up,10,40
Street Fighter II,90,450
Speed Racer,10,40

Output Explanation

Print the game names that earn him the most into the standard output in alphabetical order

Output

Mortal Kombat
Pump it Up
Speed Racer
Street Fighter II



import sys
import itertools

n = int(sys.stdin.readline())

games = {}
for i in range(n):
    line = sys.stdin.readline().rstrip().split(',')
    games[line[0]] =  (int(line[1]), int(line[2]))

result = ()
mpay = 0

for k in range(1, n):
    for z in itertools.combinations(games, k):
        time = 0
        pay = 0
        for x in z:
            time += games[x][0]
            if time > 120:
                break
            pay +=  games[x][1]
        if time <= 120 and pay > mpay:
            result = z
            mpay = pay

print('\n'.join(sorted(list(result))))