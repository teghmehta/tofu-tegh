CREATE TABLE `listings` (
  id int(11) NOT NULL AUTO_INCREMENT,
  title varchar(255) NOT NULL,
  description text NOT NULL,
  company varchar(255) NOT NULL,
  deadline datetime NOT NULL,
  created_at datetime NOT NULL,
  updated_at datetime NOT NULL,
  PRIMARY KEY (id)
)