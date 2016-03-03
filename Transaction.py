# Auto Transaction - allows the officer to enter infomaion to complete the transacion
# details of seller, buyer, date and price
#  s_date      date,
#  price       numeric(9,2),
#  t_id        CHAR(15),
#  seller_id   CHAR(15),
#  buyer_id    CHAR(15),
#  vehicle_id  CHAR(15),
#  officer_id  CHAR(15),
#  PRIMARY KEY (t_id),
#  FOREIGN KEY (seller_id) REFERENCES people(sin),
#  FOREIGN KEY (buyer_id) REFERENCES people(sin),
#  FOREIGN KEY (vehicle_id) REFERENCES vehicle(serial_no),
#  FOREIGN KEY (officer_id) REFERENCES registering_officer(id)
# Jen
