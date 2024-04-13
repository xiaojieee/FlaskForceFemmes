USE book_tracker;

CREATE PROCEDURE book_tracker.get_books()
select book_list.book_id,
	   book_list.title,
       author.name as author,
       genre.name as genre,
       book_list.pages,
       reading_level.level as reading_level,
       book_list.book_image,
       book_list.blurb
from book_list
JOIN author on book_list.author_id = author.author_id
JOIN genre on book_list.genre_id = genre.genre_id
JOIN reading_level on book_list.reading_level_id = reading_level.reading_level_id
order by Title;

CALL book_tracker.get_books(); -- Returns all books with data from foreign keys and titles in alphabetical order

DROP PROCEDURE IF EXISTS book_tracker.get_books;


CREATE PROCEDURE book_tracker.get_students_progress()
SELECT account_.username, -- specifies columns to include in the result set, selects username column from account_ table
	   reading_level.level as reading_level, -- a column alias
GROUP_CONCAT( -- concatenates values from multiple rows into a single string
	DISTINCT COALESCE(
    -- distinct only considers unique values (unique book titles), coalesce function returns the first non-null value
        CASE
            WHEN reading_progress.completed_date IS NULL THEN book_list.title -- when there's no completed date, return the title
        END,
        'None' -- for rows where condition is not met (all user's books have a completed date)
    )
    ORDER BY book_list.title
    SEPARATOR ', '
) AS current_books,
SUM( -- calculates the sum of current books read this week
    CASE
        WHEN WEEK(reading_progress.completed_date, 1) = WEEK(CURDATE(), 1)
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
GROUP BY account_.username, reading_level.level -- Groups the result set by unique combinations of username and reading level (required by aggregate functions)
ORDER BY account_.username;

CALL book_tracker.get_students_progress();

-- DROP PROCEDURE IF EXISTS book_tracker.get_students_progress;
