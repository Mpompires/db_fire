	BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "akinhto" (
	"akinito_id" INTEGER,
	"surface_area" REAL,
	"area" TEXT,
	"area_coords" TEXT,	
	"description" TEXT,
	"extra"	TEXT,
	"diaxhrizetai_pwlhths_id" INTEGER,
	PRIMARY KEY("akinito_id" AUTOINCREMENT),
	FOREIGN KEY("diaxhrizetai_pwlhths_id") REFERENCES "m_pwlhths"("melos_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "melos" (
	"melos_id" INTEGER,
	"username" TEXT UNIQUE,
	"password" TEXT,	
	"email"	TEXT,
	"first_name" TEXT,
	"last_name"	TEXT,
	"is_endiaferomenos"	INTEGER,
	"is_pwlhths" INTEGER,
	PRIMARY KEY("melos_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "aggelia" (
	"aggelia_id" INTEGER,
	"akinito_id" INTEGER,
	"pwlhths_id" INTEGER,
	"price"	REAL,
	"aggelia_type" TEXT 
        CHECK(aggelia_type = "enoikiazetai" or aggelia_type = "pwlhtai"),
	"created_on" TEXT,
	"modified_on" TEXT,
	"closed_on"	TEXT,
	"available"	INTEGER,
	"available_since" TEXT,
	"text"	TEXT,
	PRIMARY KEY("aggelia_id" AUTOINCREMENT),
	FOREIGN KEY("akinito_id") REFERENCES "akinhto"("akinito_id") ON DELETE CASCADE,
	FOREIGN KEY("pwlhths_id") REFERENCES "m_pwlhths"("melos_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "m_endiaferomenos_endiaferetai" (
	"melos_id" INTEGER,
	"aggelia_id" INTEGER,
	PRIMARY KEY("melos_id","aggelia_id")
    FOREIGN KEY("melos_id") REFERENCES "melos"("melos_id") ON DELETE CASCADE, 
    FOREIGN KEY("aggelia_id") REFERENCES "aggelia"("aggelia_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "a_epaggelmatikos_xwros" (
	"akinito_id" INTEGER,
	"parking_spot" INTEGER,
	"construnction_year" TEXT,
	"internal" TEXT,
	"external" TEXT,
	PRIMARY KEY("akinito_id"),
	FOREIGN KEY("akinito_id") REFERENCES "akinhto"("akinito_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "a_gh" (
	"akinito_id" INTEGER,
	"building_coeff" REAL,
	"external" TEXT,
	PRIMARY KEY("akinito_id"),
	FOREIGN KEY("akinito_id") REFERENCES "akinhto"("akinito_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "a_katoikia" (
	"akinito_id" INTEGER,
	"katoikia_type"	TEXT
        CHECK(katoikia_type = "monokatoikia" or katoikia_type = "polykatoikia"),
	"heating_system" TEXT
        CHECK(heating_system = "autonomh" or heating_system = "kentrikh"),
	"bathrooms"	INTEGER,
	"floor"	INTEGER,
	"construction_year"	TEXT,
	"internal" TEXT,
	"external" TEXT,
	PRIMARY KEY("akinito_id"),
	FOREIGN KEY("akinito_id") REFERENCES "akinhto"("akinito_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "idiokthths" (
	"afm" TEXT,
	"first_name" TEXT,
	"last_name"	TEXT,
	PRIMARY KEY("afm")
);
CREATE TABLE IF NOT EXISTS "idiokthths_exei" (
	"akinito_id" INTEGER,
	"idiokthths_afm" TEXT,
	PRIMARY KEY("akinito_id","idiokthths_afm"),
	FOREIGN KEY("idiokthths_afm") REFERENCES "idiokthths"("afm") ON DELETE CASCADE, 
	FOREIGN KEY("akinito_id") REFERENCES "akinhto"("akinito_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "m_endiaferomenos" (
	"melos_id" INTEGER,
	PRIMARY KEY("melos_id" AUTOINCREMENT),
	FOREIGN KEY("melos_id") REFERENCES "melos"("melos_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "m_pwlhths" (
	"melos_id" INTEGER,
	"afm" INTEGER UNIQUE,
	"telephone"	TEXT,
	"is_mesiths" INTEGER,
	PRIMARY KEY("melos_id"),
	FOREIGN KEY("melos_id") REFERENCES "melos"("melos_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "mesiths" (
	"afm" TEXT,
	"brand_name" TEXT,
	"brand_address" TEXT,
	PRIMARY KEY("afm"),
	FOREIGN KEY("afm") REFERENCES "m_pwlhths"("melos_id") ON DELETE CASCADE
);
COMMIT;
