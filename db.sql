BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "akinhto" (
	"akinito_id"	INTEGER,
	"surface_area"	REAL,
	"area"	VARCHAR(255),
	"area_coords"	VARCHAR(255),
	"description"	TEXT,
	"extra"	TEXT,
	PRIMARY KEY("akinito_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "melos" (
	"melos_id"	INTEGER,
	"username"	VARCHAR(64),
	"passwork"	VARCHAR(64),
	"email"	VARCHAR(64),
	"first_name"	VARCHAR(64),
	"last_name"	VARCHAR(64),
	"is_endiaferomenos"	BOOL,
	"is_pwlhths"	BOOL,
	PRIMARY KEY("melos_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "aggelia" (
	"aggelia_id"	INTEGER,
	"akinito_id"	INTEGER,
	"pwlhths_id"	INTEGER,
	"price"	REAL,
	"aggelia_type"	TINYINT(1),
	"created_on"	DATETIME,
	"modified_on"	DATETIME,
	"closed_on"	DATETIME,
	"available"	BOOL,
	"available_since"	DATETIME,
	"text"	TEXT,
	PRIMARY KEY("aggelia_id" AUTOINCREMENT),
	FOREIGN KEY("akinito_id") REFERENCES "akinhto"("akinito_id"),
	FOREIGN KEY("pwlhths_id") REFERENCES "m_pwlhths"("melos_id")
);
CREATE TABLE IF NOT EXISTS "m_endiaferomenos_endiaferetai" (
	"melos_id"	INTEGER,
	"aggelia_id"	INTEGER,
	PRIMARY KEY("melos_id","aggelia_id")
);
CREATE TABLE IF NOT EXISTS "a_epaggelmatikos_xwros" (
	"akinito_id"	INTEGER,
	"parking_spot"	BOOL,
	"construnction_year"	YEAR,
	"internal"	TEXT,
	"external"	TEXT,
	PRIMARY KEY("akinito_id"),
	FOREIGN KEY("akinito_id") REFERENCES "akinhto"("akinito_id")
);
CREATE TABLE IF NOT EXISTS "a_gh" (
	"akinito_id"	INTEGER,
	"building_coeff"	REAL,
	"external"	TEXT,
	PRIMARY KEY("akinito_id"),
	FOREIGN KEY("akinito_id") REFERENCES "akinhto"("akinito_id")
);
CREATE TABLE IF NOT EXISTS "a_katoikia" (
	"akinito_id"	INTEGER,
	"katoikia_type"	TINYINT(1),
	"heating_system"	TINYINT(1),
	"bathrooms"	INTEGER,
	"floor"	INTEGER,
	"construction_year"	YEAR,
	"internal"	TEXT,
	"external"	TEXT,
	PRIMARY KEY("akinito_id"),
	FOREIGN KEY("akinito_id") REFERENCES "akinhto"("akinito_id")
);
CREATE TABLE IF NOT EXISTS "idiokthths" (
	"afm"	VARCHAR(255),
	"first_name"	VARCHAR(255),
	"last_name"	VARCHAR(255),
	"is_pwlhths"	BOOL,
	PRIMARY KEY("afm")
);
CREATE TABLE IF NOT EXISTS "idiokthths_exei" (
	"akinito_id"	INTEGER,
	"idiokthths_afm"	VARCHAR(255),
	PRIMARY KEY("akinito_id","idiokthths_afm"),
	FOREIGN KEY("idiokthths_afm") REFERENCES "idiokthths"("afm"),
	FOREIGN KEY("akinito_id") REFERENCES "akinhto"("akinito_id")
);
CREATE TABLE IF NOT EXISTS "m_endiaferomenos" (
	"melos_id"	INTEGER,
	PRIMARY KEY("melos_id" AUTOINCREMENT),
	FOREIGN KEY("melos_id") REFERENCES "melos"("melos_id")
);
CREATE TABLE IF NOT EXISTS "m_pwlhths" (
	"melos_id"	INTEGER,
	"afm"	VARCHAR(255) UNIQUE,
	"telephone"	VARCHAR(255),
	"is_mesiths"	BOOL,
	PRIMARY KEY("melos_id"),
	FOREIGN KEY("melos_id") REFERENCES "melos"("melos_id")
);
CREATE TABLE IF NOT EXISTS "mesiths" (
	"afm"	VARCHAR(255),
	"brand_name"	VARCHAR(255),
	"brand_address"	VARCHAR(255),
	PRIMARY KEY("afm"),
	FOREIGN KEY("afm") REFERENCES "m_pwlhths"("melos_id")
);
COMMIT;
