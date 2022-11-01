-- convert database and tables to utf8mb4
ALTER DATABASE hbtn_0c_0
	CHARACTER SET utf8mb4
	COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table
	CONVERT TO CHARACTER SET utf8mb4
	COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table
	CHANGE name name
	varchar(256)
	CHARACTER SET utf8mb4
	COLLATE utf8mb4_unicode_ci;
