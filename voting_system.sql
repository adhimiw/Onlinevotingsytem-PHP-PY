-- Create the 'voting_system' database
CREATE DATABASE IF NOT EXISTS voting_system;

-- Switch to the 'voting_system' database
USE voting_system;

-- Create the 'voters' table to store voter information
CREATE TABLE IF NOT EXISTS voters (
    id INT AUTO_INCREMENT PRIMARY KEY,
    aadhar VARCHAR(20) NOT NULL,
    name VARCHAR(50) NOT NULL,
    birth_date VARCHAR(15) NOT NULL
);

-- Insert sample data (optional)
INSERT INTO voters (aadhar, name, birth_date) VALUES
('10001', 'adhi', '01-12-2004'),
('10002', 'Goutam Kumar Bhadani', '01-01-1999'),
('10003', 'Gautam Kumar', '12-10-1999'),
('10004', 'Kundan Kumar', '08-12-1999'),
('10005', 'Aniket Arora', '28-08-1999'),
('10006', 'Dipika Singh', '20-10-2000'),
('10007', 'Avinash Kumar', '02-03-1999'),
('10008', 'Ravi Raj', '26-12-1999'),
('10009', 'Shubham Kumar', '02-01-1999'),
('10010', 'Subham Kumar', '03-01-1999');
