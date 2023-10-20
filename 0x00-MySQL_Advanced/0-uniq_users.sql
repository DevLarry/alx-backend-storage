-- 3 first students in the Batch
-- because Batch 3 is the best!
CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    PRIMARY KEY (id)
) IF NOT EXISTS;