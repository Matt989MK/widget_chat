DROP TABLE IF EXISTS company;
CREATE TABLE company (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  owner_name TEXT NOT NULL,
  address TEXT NOT NULL,
  owner_phone TEXT NOT NULL,
  email TEXT NOT NULL,
  website TEXT NOT NULL,
  instagram TEXT NOT NULL,
  facebook TEXT NOT NULL,
  twitter TEXT NOT NULL,
  opening_time TEXT NOT NULL,
  closing_time TEXT NOT NULL,
  ppf_price REAL NOT NULL,
  ceramic_coating_price REAL NOT NULL,
  full_detail_price REAL NOT NULL,
  interior_detail_price REAL NOT NULL,
  exterior_detail_price REAL NOT NULL,
  headlight_restoration_price REAL NOT NULL,
  windshield_repair_price REAL NOT NULL,
  odor_removal_price REAL NOT NULL,
  discount_rules TEXT NOT NULL
);