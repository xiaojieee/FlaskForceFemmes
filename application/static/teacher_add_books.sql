DELIMITER //

CREATE PROCEDURE AddBook(
    IN p_title VARCHAR(255),
    IN p_author_id INT,
    IN p_genre_id INT,
    IN p_pages INT,
    IN p_reading_level_id INT,
    IN p_image_url VARCHAR(255),
    IN p_blurb TEXTbook_list
)
BEGIN
    -- Insert the new book into the Book_List table
    INSERT INTO Book_List (Title, Author_ID, Genre_ID, Pages, Reading_Level_ID, Book_image, Blurb)
    VALUES (p_title, p_author_id, p_genre_id, p_pages, p_reading_level_id, p_image_url, p_blurb);
END //

DELIMITER ;

