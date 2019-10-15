DROP TABLE users;

CREATE TABLE users (
    id          INTEGER         NOT NULL     PRIMARY KEY   autoincrement,
    email       VARCHAR(50)     NOT NULL,
    password    VARCHAR(50)     NOT NULL
);