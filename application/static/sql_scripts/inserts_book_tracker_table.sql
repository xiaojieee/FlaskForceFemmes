USE book_tracker;

INSERT INTO Author (Name) 
VALUES 
('David MacPhail'),
('Cathryn Constable'),
('Lincoln Peirce'),
('Nicola Skinner'),
('Matt Haig'),
('Shane Hegarty'),
('Tom Palmer'),
('Vince Cross'),
('Phil Earle'),
('Katie Tsang'),
('Kevin Tsang'),
('Dashe Roberts'),
('Justin Davies'),
('MG Leonard'),
('Sam Sedgman'),
('Sarah Todd Taylor'),
('Anne Miller'),
('Rashmi Sirdeshpande'),
('Imogen Russell Williams'),
('Pat Jacobs'),
('Laura Ellen Anderson'),
('Dav Pilkey'),
('James Stayte'),
('Various'),
('Hilda Offen'),
('Various'),
('Judy Blume'),
('Malorie Blackman'),
('Barbara Eurphan Todd'),
('Nick East'),
('David Baddiel'),
('Alan MacDonald');

Select * from author;

INSERT INTO Genre (Name) 
VALUES 
('Adventure'),
('Fantasy'),
('Sport'),
('Horror'),
('Mystery'),
('Non-Fiction'),
('Graphic'),
('Poetry'),
('Classics'),
('Humour');

Select * from genre;

INSERT INTO Reading_Level (Level) 
VALUES 
('Lime'),
('Gold'),
('Orange');

Select * from Reading_Level;

INSERT INTO Book_List (Title, Author_ID, Genre_ID, Pages, Reading_Level_ID, Book_image, Blurb, Recommended) VALUES
('Thorfinn and the Putrid Potion', 1, 1, 256, 1, 'https://shop.shetlandtimes.co.uk/cdn/shop/products/ThorfinnPutridPotion_470x.jpg?v=1660294622', 'Join Thorfinn, a young Viking warrior, on a hilarious and adventurous quest as he sets out to find a cure for a putrid potion gone wrong. With his friends by his side, Thorfinn faces challenges and comedic mishaps in this action-packed tale.', True),
('The Pearl in the Ice', 2, 1, 240, 1, 'https://cdn.waterstones.com/bookjackets/large/9781/9126/9781912626519.jpg', 'Discover a captivating story of friendship and mystery as Sylvie embarks on a thrilling adventure to unravel the secrets of a hidden world within a frozen castle. With courage and determination, Sylvie uncovers the truth behind the pearl in the ice.', True),
('Max and the Midknights', 3, 1, 288, 2, 'https://readingwithyourkids.com/wp-content/uploads/2019/03/Max-and-the-Midknights.jpg', 'Enter a medieval world of knights, quests, and humor with Max, a spirited troubadour, and his friends. When Max dreams of becoming a knight, they embark on a daring adventure filled with excitement, friendship, and unexpected challenges.', True),
('Bloom', 4, 2, 288, 3, 'https://sevenoaksbookshop.co.uk/wp-content/uploads/2021/05/9780008297404.jpg', 'Sorrel discovers a magical plant that grows human-sized vegetables, leading to unexpected challenges and discoveries in her town. With humor and heart, Sorrel navigates friendship, family, and the power of believing in the extraordinary.', NULL),
('Evie and the Animals', 5, 2, 256, 2, 'https://cgassets-1d48b.kxcdn.com/site/assets/files/422029/getimage.600x0.jpg', 'Evie has a unique ability to understand and communicate with animals, leading to wild adventures and heartfelt connections. Join Evie on a heartwarming journey of friendship, empathy, and the wonders of the natural world.', NULL),
('The Rusty Rescue', 6, 2, 288, 2, 'https://www.hachette.co.uk/wp-content/uploads/2019/08/hbg-title-9781444949407-47.jpg?w=450', 'When Rusty, a mischievous robot, goes missing, siblings Polly and Jack embark on a daring mission to find him. Along the way, they encounter futuristic challenges and learn valuable lessons about teamwork and perseverance.', NULL),
('From the Ashes', 7, 3, 320, 1, 'https://cdn.waterstones.com/bookjackets/large/9781/7810/9781781087831.jpg', 'Set during World War II, this gripping story follows Lizzie''s journey as she navigates the challenges of war-torn London and uncovers secrets about her family''s past. Through adversity, Lizzie finds strength and resilience.', NULL),
('Berlin Olympics', 8, 3, 240, 2, 'https://pictures.abebooks.com/isbn/9781407130354-uk.jpg', 'Join Alfie and his family as they experience the excitement and tensions of the 1936 Berlin Olympics. Against the backdrop of history, Alfie learns valuable lessons about courage, friendship, and standing up against injustice.', NULL),
('The Unlucky Eleven', 9, 3, 224, 2, 'https://cdn.waterstones.com/bookjackets/large/9781/7811/9781781128503.jpg', 'When Stanleys football team faces challenges on and off the field, they must come together to turn their luck around and prove they are winners in their own right. This uplifting story celebrates teamwork, determination, and sportsmanship.', NULL),
('Sam Wu is Not Afraid of Zombies', 10, 4, 240, 1, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkp5oMr1Kl5k0pIXCwvJH_TL-tZnTSPdQ63He-zj2joKx-6Qv2', 'Sam Wu faces his fear of zombies as he navigates spooky challenges and hilarious mishaps in this fun-filled adventure. With his friends by his side, Sam learns that bravery comes in many forms.', NULL),
('The Bigwoof Conspiracy', 12, 4, 288, 2, 'https://m.media-amazon.com/images/I/51guiNNUrLL._SY445_SX342_.jpg', 'Join Ben and his extraordinary dog Bigwoof as they uncover a mysterious conspiracy in their neighborhood. With humor and suspense, this story explores friendship, loyalty, and the thrill of solving a puzzling mystery.', NULL),
('Whoa! I Spy a Werewolf', 13, 4, 288, 1, 'https://m.media-amazon.com/images/I/51FtT8YosbL._SY445_SX342_.jpg', 'When Connor discovers his teacher might be a werewolf, he embarks on a hilarious and hair-raising investigation to uncover the truth. Get ready for a howling good time filled with humor and unexpected twists.', NULL),
('The Highland Falcon Thief', 14, 5, 352, 2, 'https://ik.imagekit.io/panmac/tr:f-auto,di-placeholder_portrait_aMjPtD9YZ.jpg,w-270/edition/9781529013061.jpg', 'All aboard the Highland Falcon, a luxurious train on a thrilling journey through the Scottish Highlands! When a precious jewel goes missing, Hal and his friend Lenny embark on a daring adventure to catch the thief and solve the mystery.', NULL),
('The Catnap Caper', 16, 5, 160, 2, 'https://www.madeleinelindley.com/media/catalog/product/cache/8140e74dc9ef78367b40656eb7156d0f/t/h/thumbnail_9277_66.jpg', 'Detective Cat and Officer Mouse are on the case when precious jewels vanish from a museum. Join this dynamic duo as they use their detective skills and teamwork to unravel clues and catch the cunning thief in this charming and suspenseful tale.', NULL),
('Mickey and the Animal Spies', 17, 5, 192, 3, 'https://pictures.abebooks.com/isbn/9780192773630-uk.jpg', 'When Mickey''s hamster is stolen, she teams up with a group of animal spies to solve the mystery. Join Mickey and her furry friends as they uncover clues, outsmart villains, and embark on a thrilling adventure filled with espionage and friendship.', NULL),
('How to Be Extraordinary', 18, 6, 320, 3, 'https://m.media-amazon.com/images/I/61U2wVAH8dL._SX342_SY445_.jpg', 'Discover the inspiring stories of ordinary people who achieved extraordinary feats in various fields, from science and sports to activism and creativity. This book celebrates resilience, determination, and the power of believing in oneself.', NULL),
('The Big Book of the UK', 19, 6, 192, 3, 'https://cdn.penguin.co.uk/dam-assets/books/9780241382608/9780241382608-jacket-large.jpg', 'Dive into a comprehensive guide to the United Kingdom, exploring its history, culture, landmarks, and fascinating facts. From famous cities to scenic landscapes, this book offers a colorful journey across the UK''s rich tapestry.', NULL),
('Unusual Pets', 20, 6, 208, 3, 'https://m.media-amazon.com/images/I/51D3fBymIfL._SX342_SY445_.jpg', 'Explore the world of unusual and exotic pets in this fascinating book. From miniature pigs and hedgehogs to chameleons and sugar gliders, discover unique animals and learn about their care, habitats, and interesting characteristics.', NULL),
('Winging It', 21, 7, 304, 3, 'https://m.media-amazon.com/images/I/51OJeKZlC1L._SY466_.jpg', 'Join Mimi, a young bird, on a delightful journey of self-discovery and friendship. With colorful illustrations and heartwarming storytelling, this book celebrates the joys of embracing one''s uniqueness and spreading kindness.', NULL),
('Brawl of the Wild', 22, 7, 256, 3, 'https://productimages.worldofbooks.com/1407191942.jpg', 'Get ready for an epic battle in the wild as Dog Man faces off against his nemesis Petey the Cat in a hilarious and action-packed adventure. With graphic novel fun and quirky characters, this book is sure to entertain readers of all ages.', NULL),
('The Mightiest Chef in the Universe!', 23, 7, 288, 2, 'https://m.media-amazon.com/images/I/51JTlKcbu2L._SY445_SX342_.jpg', 'Enter a culinary galaxy with Captain Elephant and his crew as they compete in a cooking contest to determine the mightiest chef in the universe. With whimsical illustrations and a dash of humor, this book serves up a deliciously imaginative tale.', NULL),
('Be the Change', 24, 8, 176, 3, 'https://productimages.worldofbooks.com/1782403280.jpg', 'This poetry collection inspires young readers to make a positive impact in the world. Through poems that celebrate kindness, diversity, and resilience, this book encourages children to embrace empathy and be agents of change.', NULL),
('How Many Points for a Panda?', 25, 8, 40, 3, 'https://m.media-amazon.com/images/I/61+OUJwU3lL._SY445_SX342_.jpg', 'Join Eric and friends as they navigate the world of tabletop gaming, from dragons to dungeons and epic quests. With humor and adventure, this book celebrates the joy of gaming and friendship.', NULL),
('A Caribbean Dozen', 26, 8, 128, 3, 'https://d3ddkgxe55ca6c.cloudfront.net/assets/t1614783055/a/9f/0f/208178-ml-1995735.jpg', 'Explore the rich culture and vibrant landscapes of the Caribbean through a collection of poetry from diverse Caribbean voices. From folklore to everyday life, these poems capture the essence of the region and its people.', NULL),
('Freckle Juice', 27, 9, 64, 2, 'https://m.media-amazon.com/images/I/41yd55ciwxL._SY445_SX342_.jpg', 'Andrew wants freckles more than anything, so he buys Sharon''s secret recipe for freckle juice. But things don''t go exactly as planned in this humorous and relatable story about self-acceptance and the consequences of wishing for what you don''t have.', NULL),
('Hacker', 28, 9, 400, 3, 'https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1320496916i/369967.jpg', 'Vicky is a talented hacker who gets caught up in a dangerous online world of secrets and intrigue. As she navigates virtual challenges and real-life consequences, Vicky must use her skills wisely to protect herself and those she cares about.', NULL),
('Worzel Gummidge', 29, 9, 176, 3, 'https://m.media-amazon.com/images/I/51Xo2bw5VQL._AC_UF894,1000_QL80_.jpg', 'Step into the whimsical world of Worzel Gummidge, the talking scarecrow with a knack for mischief and adventure. Join Worzel and his friends in this classic tale filled with rural charm and magical escapades.', NULL),
('Agent Weasel and the Abominable Dr Snow', 30, 10, 192, 3, 'https://m.media-amazon.com/images/I/61RfZblQL1L._SY445_SX342_.jpg', 'Join Agent Weasel and his friends as they face off against the notorious Dr. Snow in a thrilling adventure full of espionage, gadgets, and daring escapades. With humor and suspense, this book is a delight for young readers.', NULL),
('The Taylor Turbochaser', 31, 10, 400, 3, 'https://covers.borrowbox.com/backend/covers/HCU_687313?w=427', 'When Amy and her friend take the Taylor TurboChaser—an amazing car with jet engines—on a road trip, they embark on an exhilarating journey of speed, friendship, and unexpected twists. Buckle up for a high-speed adventure like no other!', NULL),
('Trouble!', 32, 10, 400, 3, 'https://www.village-books.co.uk/wp-content/uploads/2020/11/9781788950251.jpg', 'Hannah''s life is turned upside down when her sister''s rebellious behavior leads to unforeseen consequences. As secrets unravel and tensions rise, Hannah navigates family dynamics, friendship, and the complexities of teenage life in this gripping story.', NULL);



-- Try adding this book in the front end on the webpage
-- Title: Unexpected Super Spy
-- Author: Zanib Mian
-- Humour
-- Pages: 208
-- Image: https://cdn.waterstones.com/bookjackets/large/9781/4449/9781444951271.jpg 
-- Blurb: When private investigator Teagan Frost discovers she has superpowers, her life takes a thrilling turn as she becomes an unexpected super spy. With action-packed missions, quirky characters, and a dash of humour, Teagan navigates a world of intrigue and danger.

-- When adding a book with the same author, the python function should take into account and will not do a double
-- Try this!!
-- Title: The Voyage of the Dawn Dreader
-- Author: C.S. Lewis
-- Classics
-- Pages: 240
-- Image: https://cdn.waterstones.com/bookjackets/large/9780/0086/9780008663094.jpg
-- Blurb: Edmund and Lucy, along with their cousin Eustace, embark on a thrilling sea voyage aboard the Dawn Treader to distant lands. Join them in this classic tale of courage, discovery, and the search for hidden treasures and adventures.
--
-- And this!!
-- Title: The Horse and His Boy
-- Author: C.S. Lewis
-- Classics
-- Pages: 224
-- Image: https://cdn.waterstones.com/bookjackets/large/9780/0086/9780008663070.jpg
-- Blurb: Follow the story of Shasta, a young boy raised as a fisherman's son, who discovers his true identity and destiny in the magical land of Narnia. This tale of courage, friendship, and destiny unfolds amidst the backdrop of a vast and enchanting world.


Select * FROM book_list;

INSERT INTO Book_Author (Book_ID, Author_ID) 
VALUES 
(10, 11);


INSERT INTO Book_Author (Book_ID, Author_ID) 
VALUES 
(13, 15);

Select * FROM Book_Author;

INSERT INTO Account_type (Account_type)
VALUES
('Teacher'),
('Student');

select * FROM Account_type;


-- THIS IS NO LONGER NEEDED, USE THE FRONT END PAGE TO REGISTER FOR A NEW ACCOUNT
-- INSERT INTO Account_ (Account_type_id, Username, Password_)
-- VALUES
-- (1, 'Teacher Bear', 'Bear'),
-- (2, 'Ziggy the Zebra', 'Zebra'),
-- (2, 'Leo the Lion', 'Lion'),
-- (2, 'Polly the Penguin', 'Penguin'),
-- (2, 'Benny the Bunny', 'Bunny'),
-- (2, 'Sammy the Sloth', 'Sloth'),
-- (2, 'Coco the Chameleon', 'Chameleon'),
-- (2, 'Gigi the Giraffe', 'Giraffe'),
-- (2, 'Rocky the Raccoon', 'Raccoon'),
-- (2, 'Lily the Llama', 'Llama'),
-- (2, 'Freddie the Fox', 'Fox');

select * FROM account_;


-- NOTE: Create 3 accounts using the add_student page and then run this insert for the reading_progress table

-- INSERT INTO Reading_progress (Account_id, Book_ID, Start_Date, Current_page, Completed_Date, Rating)
-- VALUES 
-- (2, 4, '2024-04-15', 36, NULL, NULL),
-- (3, 8, '2024-04-14', 120, NULL, NULL),
-- (1, 12, NULL, 80, '2024-04-16', 4),
-- (2, 16, '2024-04-17', 50, NULL, NULL),
-- (3, 20, NULL, NULL, NULL, NULL),
-- (1, 24, '2024-04-13', 20, NULL, NULL),
-- (2, 28, NULL, 150, NULL, NULL),
-- (3, 30, '2024-04-16', 100, '2024-04-17', 5),
-- (1, 6, NULL, NULL, NULL, NULL),
-- (2, 14, '2024-04-12', 180, '2024-04-17', 4);

select * FROM Reading_progress;

