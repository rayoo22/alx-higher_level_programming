-- creates table unique_id with the id field being
-- the unique idedentifier for records
CREATE TABLE IF NOT EXISTS unique_id(
	id int PRIMARY KEY DEFAULT 1,
	name VARCHAR(256)
	);
