-- 3 first students in the Batch
-- because Batch 3 is the best!
CREATE TABLE USER (
    ID INT NOT NULL AUTO_INCREMENT,
    EMAIL VARCHAR(255),
    NAME VARCHAR(255),
    PRIMARY KEY (ID)
) IF NOT EXISTS;