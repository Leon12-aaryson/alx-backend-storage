-- id, integer, never null, auto increment and primary key
-- email varchar not null
-- name varchar

CREATE TABLE IF NOT EXISTS users (
      id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
      email VARCHAR(255) NOT NULL UNIQUE,
      name VARCHAR(255)
);
