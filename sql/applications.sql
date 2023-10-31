CREATE TABLE `applications` (
  id int(11) NOT NULL AUTO_INCREMENT,
  candidate_id int(11) NOT NULL,
  listing_id int(11) NOT NULL,
  resume varchar(255) NOT NULL,
  status ENUM('pending', 'reviewed', 'hired', 'rejected') NOT NULL DEFAULT 'pending',
  created_at datetime NOT NULL,
  updated_at datetime NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY (candidate_id, listing_id),
  FOREIGN KEY (candidate_id) REFERENCES candidates(id),
  FOREIGN KEY (listing_id) REFERENCES listings(id),
)