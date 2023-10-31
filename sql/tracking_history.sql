CREATE TABLE `tracking` (
  id int(11) NOT NULL AUTO_INCREMENT,
  application_id int(11) NOT NULL,
  status ENUM('pending', 'reviewed', 'hired', 'rejected') NOT NULL DEFAULT 'pending',
  previous_status ENUM('pending', 'reviewed', 'hired', 'rejected') NOT NULL DEFAULT 'pending',
  created_at datetime NOT NULL,
  updated_at datetime NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (application_id) REFERENCES applications(id)
)