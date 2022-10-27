CREATE TABLE pizzas AS
  SELECT "Pizzahhh" AS name, 12 AS open, 15 AS close UNION
  SELECT "La Val's"        , 11        , 22          UNION
  SELECT "Sliver"          , 11        , 20          UNION
  SELECT "Cheeseboard"     , 16        , 23          UNION
  SELECT "Emilia's"        , 13        , 18;

CREATE TABLE meals AS
  SELECT "breakfast" AS meal, 11 AS time UNION
  SELECT "lunch"            , 13         UNION
  SELECT "dinner"           , 19         UNION
  SELECT "snack"            , 22;


-- Pizza places that open before 1pm in alphabetical order
CREATE TABLE opening AS
SELECT name FROM pizzas WHERE open < 13 ORDER BY name;


-- Two meals at the same place
CREATE TABLE double AS

SELECT a.meal, b.meal, c.name FROM meals AS a, meals AS b, pizzas AS c WHERE b.time - a.time > 6 AND c.open <= a.time AND c.close >= b.time;

