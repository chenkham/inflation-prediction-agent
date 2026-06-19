CREATE DATABASE IF NOT EXIST InflationDB;
USE InflationDB;
CREATE TABLE IF NOT EXISTS InflationData (
    id INT AUTO_INCREMENT PRIMARY KEY,
    target_year INT NOT NULL,
    target_month INT NOT NULL,
    wpi_index DOUBLE NOT NULL,
    oil_price_usd DOUBLE NOT NULL,
    usd_inr_rate DOUBLE NOT NULL,
    iip_index DOUBLE NOT NULL,
    predicted_inflation_rate DOUBLE NOT NULL,
    execution_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)ENGINE=InnoDB;