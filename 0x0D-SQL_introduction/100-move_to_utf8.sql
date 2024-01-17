-- Convert the hbtn_0c_0 database to UTF8
ALTER DATABASE
	hbtn_0c_0
	CHARACTER SET = utf8mb4
	COLLATE = utf8mb4_unicode_ci;

-- Convert the first_table table and the name field to UTF8
ALTER TABLE
	hbtn_0c_0.first_table
      CHARACTER SET utf8mb4
      COLLATE utf8mb4_unicode_ci;

-- converts the column 'name' to UTF8
ALTER TABLE
	hbtn_0c_0.first_table
	MODIFY name
	VARCHAR(256)
	CHARACTER SET utf8mb4
	COLLATE utf8mb4_unicode_ci;
