CREATE DATABASE IF NOT EXISTS tofu_service;
USE tofu_service;

CREATE USER 'tofu_db_user'@'localhost' IDENTIFIED BY 'tofu';
GRANT ALL ON tofu_service.* TO 'tofu_db_user'@'localhost';

-- Create `candidates` table first
CREATE TABLE `candidates` (
  id int(11) NOT NULL AUTO_INCREMENT,
  name varchar(255) NOT NULL,
  phone varchar(255) NOT NULL,
  email varchar(255) NOT NULL,
  resume varchar(255) NOT NULL,
  created_at datetime NOT NULL DEFAULT NOW(),
  updated_at datetime NOT NULL DEFAULT NOW(),
  PRIMARY KEY (id),
  UNIQUE KEY (email)
);

-- Create `listings` table next
CREATE TABLE `listings` (
  id int(11) NOT NULL AUTO_INCREMENT,
  title varchar(255) NOT NULL,
  description text NOT NULL,
  company varchar(255) NOT NULL,
  deadline datetime NOT NULL,
  created_at datetime NOT NULL DEFAULT NOW(),
  updated_at datetime NOT NULL DEFAULT NOW(),
  PRIMARY KEY (id)
);

-- Now `applications`
CREATE TABLE `applications` (
  id int(11) NOT NULL AUTO_INCREMENT,
  candidate_id int(11) NOT NULL,
  listing_id int(11) NOT NULL,
  resume varchar(255) NOT NULL,
  status ENUM('pending', 'reviewed', 'hired', 'rejected') NOT NULL DEFAULT 'pending',
  created_at datetime NOT NULL DEFAULT NOW(),
  updated_at datetime NOT NULL DEFAULT NOW(),
  PRIMARY KEY (id),
  UNIQUE KEY (candidate_id, listing_id),
  FOREIGN KEY (candidate_id) REFERENCES candidates(id),
  FOREIGN KEY (listing_id) REFERENCES listings(id)
);

-- Finally `tracking`
CREATE TABLE `tracking` (
  id int(11) NOT NULL AUTO_INCREMENT,
  application_id int(11) NOT NULL,
  status ENUM('pending', 'reviewed', 'hired', 'rejected') NOT NULL DEFAULT 'pending',
  previous_status ENUM('pending', 'reviewed', 'hired', 'rejected') NOT NULL DEFAULT 'pending',
  created_at datetime NOT NULL DEFAULT NOW(),
  updated_at datetime NOT NULL  DEFAULT NOW(),
  PRIMARY KEY (id),
  FOREIGN KEY (application_id) REFERENCES applications(id)
);

-- Inserting data
INSERT INTO candidates (name, phone, email, resume, created_at, updated_at) VALUES
('Alice', '555-1234', 'alice@email.com', 'resume_alice.pdf', NOW(), NOW()),
('Bob', '555-1235', 'bob@email.com', 'resume_bob.pdf', NOW(), NOW()),
('Charlie', '555-1236', 'charlie@email.com', 'resume_charlie.pdf', NOW(), NOW());

INSERT INTO listings (title, description, company, deadline, created_at, updated_at) VALUES
('Software Engineer', 'Develop full-stack applications', 'TechCorp', '2023-12-31', NOW(), NOW()),
('Data Scientist', 'Analyze large datasets', 'DataRUs', '2023-11-30', NOW(), NOW()),
('Product Manager', 'Manage software products', 'ProdMgmt', '2023-11-15', NOW(), NOW());

INSERT INTO applications (candidate_id, listing_id, resume, status, created_at, updated_at) VALUES
(1, 1, 'resume_alice.pdf', 'pending', NOW(), NOW()),
(2, 1, 'resume_bob.pdf', 'reviewed', NOW(), NOW()),
(3, 2, 'resume_charlie.pdf', 'rejected', NOW(), NOW());

INSERT INTO tracking (application_id, status, previous_status, created_at, updated_at) VALUES
(1, 'pending', 'pending', NOW(), NOW()),
(2, 'reviewed', 'pending', NOW(), NOW()),
(3, 'rejected', 'pending', NOW(), NOW());
