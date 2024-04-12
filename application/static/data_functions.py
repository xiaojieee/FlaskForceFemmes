def join_current_books(result_set):  # If a student is currently reading more than one book, they are joined together

    students_progress_dict = {}

    for student in result_set:
        username = student[0]
        reading_level = student[1]
        current_book = student[2]
        books_week = student[3]
        total_books = student[4]

        # Create a new progress dictionary if the username is not already in the dictionary
        if username not in students_progress_dict:
            progress = {
                'username': username,
                'reading_level': reading_level,
                'current_books': [current_book],
                'books_week': books_week,
                'total_books': total_books
            }
            students_progress_dict[username] = progress
        else:
            # If the username is already in the dictionary, append the current_book
            students_progress_dict[username]['current_books'].append(current_book)

    students_progress_list = list(students_progress_dict.values())

    for progress in students_progress_list:
        progress['current_books'] = ', '.join(progress['current_books'])

    return students_progress_list

