SET SQL_SAFE_UPDATES = 0; -- Permanently changes config file variable. Only need to run once.

-- * (star) ~ means all columns
SELECT * FROM my_zoo.visitors;
-- SELECT * FROM my_zoo.visitors WHERE id <= 2;
-- SELECT * FROM my_zoo.visitors ORDER BY id DESC LIMIT 1; -- get last item in table
-- INSERT INTO visitors (first_name, last_name, is_premium) VALUES ("bob", "builder", false);
-- INSERT INTO visitors (first_name, last_name, is_premium) VALUES ("gwen", "smith", true),("steve", "minecraft", false);


-- UPDATE visitors SET is_premium = FALSE;

-- delete FROM visitors where id = 2;
-- delete FROM visitors;