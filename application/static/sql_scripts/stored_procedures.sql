DELIMITER // -- START HIGHLIGHT (Delimiter allows multiple semicolons in stored procedure)
CREATE PROCEDURE book_tracker.remove_account(IN id_parameter INT)
BEGIN
    DELETE FROM reading_progress WHERE account_id = id_parameter;
    DELETE FROM account_ WHERE account_id = id_parameter;
END -- END HIGHLIGHT
DELIMITER ;

-- CALL book_tracker.remove_account();

-- DROP PROCEDURE IF EXISTS book_tracker.remove_account;



DELIMITER // -- START HIGHLIGHT
CREATE PROCEDURE book_tracker.update_reading_level(IN id_parameter INT, IN colour_parameter VARCHAR(20))
BEGIN
    DECLARE level_id INT;
    -- Retrieve the reading_level_id based on the colour_parameter
    SELECT reading_level_id INTO level_id FROM reading_level WHERE level = colour_parameter;

    -- Update the account_ table with the obtained reading_level_id
    UPDATE account_ SET reading_level_id = level_id WHERE account_id = id_parameter;
END -- END HIGHLIGHT
DELIMITER ;

-- CALL book_tracker.update_reading_level(1, 'gold');

-- DROP PROCEDURE IF EXISTS book_tracker.update_reading_level;



DELIMITER // -- START HIGHLIGHT
CREATE PROCEDURE book_tracker.add_reading_progress(
	IN username_p VARCHAR(100), 
    IN book_id_p INT, 
    IN start_date_p DATE, 
    IN current_page_p INT, 
    IN completed_date_p DATE, 
    IN rating_p ENUM('1', '2', '3', '4', '5'))
BEGIN
    DECLARE student_id INT; -- create a variable
    
	-- Retrieve the account_id based on the username parameter
    SELECT account_id INTO student_id FROM account_ WHERE Username = username_p;

    INSERT INTO reading_progress (account_id, book_id, start_date, current_page, completed_date, rating) 
	VALUES (student_id, book_id_p, start_date_p, current_page_p, completed_date_p, rating_p);
END -- END HIGHLIGHT
DELIMITER ;

CALL book_tracker.add_reading_progress('cat', 3, NULL, NULL, NULL, NULL);

-- DROP PROCEDURE IF EXISTS book_tracker.add_reading_progress;



DELIMITER // -- START HIGHLIGHT
CREATE PROCEDURE book_tracker.get_student_books(IN username_p VARCHAR(100))
BEGIN
	DECLARE student_id INT;
    SELECT account_id INTO student_id FROM account_ WHERE Username = username_p;
    SELECT reading_progress.account_id,
		   username_p as username,
		   reading_progress.book_id,
           reading_progress.start_date,
           reading_progress.current_page,
           reading_progress.completed_date,
           reading_progress.rating
FROM reading_progress
JOIN account_ on reading_progress.account_id = account_.account_id
WHERE reading_progress.account_id = student_id;
END -- END HIGHLIGHT
DELIMITER ;

-- CALL book_tracker.get_student_books('cat');

-- DROP PROCEDURE IF EXISTS book_tracker.get_student_books;



CREATE PROCEDURE book_tracker.get_books() -- START HIGHLIGHT
select book_list.book_id,
	   book_list.title,
       author.name as author,
       genre.name as genre,
       book_list.pages,
       reading_level.level as reading_level,
       book_list.book_image,
       book_list.blurb,
       book_list.Recommended
from book_list
JOIN author on book_list.author_id = author.author_id
JOIN genre on book_list.genre_id = genre.genre_id
JOIN reading_level on book_list.reading_level_id = reading_level.reading_level_id
order by Title; -- END HIGHLIGHT

-- CALL book_tracker.get_books(); -- Returns all books with data from foreign keys and titles in alphabetical order

-- DROP PROCEDURE IF EXISTS book_tracker.get_books;



CREATE PROCEDURE book_tracker.get_students_progress() -- START HIGHLIGHT
SELECT account_.account_id,
	   account_.username, -- specifies columns to include in the result set, selects username column from account_ table
	   reading_level.level as reading_level, -- a column alias
GROUP_CONCAT( -- concatenates values from multiple rows into a single string
	DISTINCT CASE
    -- distinct only considers unique values (unique book titles)
		WHEN reading_progress.start_date IS NOT NULL AND reading_progress.completed_date IS NULL
		THEN book_list.title -- when there's a start date and no completed date, return the title
	END
    ORDER BY book_list.title
    SEPARATOR ', '
) AS current_books,
SUM( -- calculates the sum of current books read this week
    CASE
        WHEN WEEK(reading_progress.completed_date) = WEEK(CURDATE())
        -- Week function gets week number (53 weeks/year) from a date and 1 parameter starts the week on Sunday (default Monday)
        THEN 1 ELSE 0
    END
) AS books_read_week,
COUNT(reading_progress.completed_date) AS total_books_read -- counts the number of non-null values in the completed_date column
FROM account_ -- retrieve data from account_ table (usernames and reading_level_id)
JOIN reading_level on account_.reading_level_id = reading_level.reading_level_id
-- matches rows in the account_ table where the reading_level_id matches rows in the reading_level table
LEFT JOIN reading_progress on reading_progress.account_id = account_.account_id
-- includes all rows from account_ table and matching rows from reading_progress table, based on account_id column
LEFT JOIN book_list on reading_progress.book_id = book_list.book_id
-- includes all rows from reading_progress table and matching rows from book_list table, based on book_id column
WHERE account_.account_type_id <> 1
-- filters the rows from the result set where the account_type_id in the account_ table is not equal to 1 (teacher account)
GROUP BY account_.account_id, account_.username, reading_level.level -- Groups the result set by unique combinations of account_id, username and reading level (required by aggregate functions)
ORDER BY account_.username; -- END HIGHLIGHT

CALL book_tracker.get_students_progress();

-- DROP PROCEDURE IF EXISTS book_tracker.get_students_progress;



DELIMITER //

CREATE PROCEDURE book_tracker.save_book_for_user(
    IN username_param VARCHAR(100),
    IN book_id_param INT
)
BEGIN
    DECLARE user_id INT;

    -- Get the user ID based on the username
    SELECT account_id INTO user_id FROM account_ WHERE Username = username_param;

    -- Insert the book into the reading progress table
    INSERT INTO reading_progress (account_id, book_id)
    VALUES (user_id, book_id_param);
END 

DELIMITER ;


