CREATE DATABASE IF NOT EXISTS balance_game_db;
USE balance_game_db;

CREATE TABLE IF NOT EXISTS games (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    votes_a INT DEFAULT 0,
    votes_b INT DEFAULT 0,
    image_url TEXT,
    is_closed BOOLEAN DEFAULT 0,
    start_date DATETIME
);

