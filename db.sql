BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "akinhto" (
	"akinhto_id" INTEGER,
	"surface_area" REAL,
	"area" TEXT,
	"area_coords" TEXT,	
	"description" TEXT,
	"extra"	TEXT,
	"diaxhrizetai_pwlhths_id" INTEGER,
	"first_name_idiokthth" TEXT,
	"last_name_idiokthth" TEXT,
	"akinhto_type" TEXT
	    CHECK(akinhto_type = "epaggelmatikos_xwros" or akinhto_type = "gh" or akinhto_type = "katoikia"),
	PRIMARY KEY("akinhto_id" AUTOINCREMENT),
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
	"is_mod" INTEGER,
	PRIMARY KEY("melos_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "aggelia" (
	"aggelia_id" INTEGER,
	"akinhto_id" INTEGER,
	"pwlhths_id" INTEGER,
	"price"	REAL,
	"aggelia_type" TEXT 
        CHECK(aggelia_type = "enoikiazetai" or aggelia_type = "pwleitai"),
	"created_on" TEXT,
	"modified_on" TEXT,
	"closed_on"	TEXT,
	"available"	INTEGER,
	"available_since" TEXT,
	"text"	TEXT,
	PRIMARY KEY("aggelia_id" AUTOINCREMENT),
	FOREIGN KEY("akinhto_id") REFERENCES "akinhto"("akinhto_id") ON DELETE CASCADE,
	FOREIGN KEY("pwlhths_id") REFERENCES "m_pwlhths"("melos_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "m_endiaferomenos_endiaferetai" (
	"melos_id" INTEGER,
	"aggelia_id" INTEGER,
	PRIMARY KEY("melos_id","aggelia_id"),
    FOREIGN KEY("melos_id") REFERENCES "melos"("melos_id") ON DELETE CASCADE, 
    FOREIGN KEY("aggelia_id") REFERENCES "aggelia"("aggelia_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "a_epaggelmatikos_xwros" (
	"akinhto_id" INTEGER,
	"parking_spot" INTEGER,
	"construction_year" INTEGER,
	"internal" TEXT,
	"external" TEXT,
	PRIMARY KEY("akinhto_id"),
	FOREIGN KEY("akinhto_id") REFERENCES "akinhto"("akinhto_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "a_gh" (
	"akinhto_id" INTEGER,
	"building_coeff" REAL,
	"external" TEXT,
	PRIMARY KEY("akinhto_id"),
	FOREIGN KEY("akinhto_id") REFERENCES "akinhto"("akinhto_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "a_katoikia" (
	"akinhto_id" INTEGER,
	"katoikia_type"	TEXT
        CHECK(katoikia_type = "monokatoikia" or katoikia_type = "polykatoikia"),
	"heating_system" TEXT
        CHECK(heating_system = "autonomh" or heating_system = "kentrikh"),
	"bathrooms"	INTEGER,
	"floor"	INTEGER,
	"construction_year"	INTEGER,
	"internal" TEXT,
	"external" TEXT,
	PRIMARY KEY("akinhto_id"),
	FOREIGN KEY("akinhto_id") REFERENCES "akinhto"("akinhto_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "m_endiaferomenos" (
	"melos_id" INTEGER,
	PRIMARY KEY("melos_id" AUTOINCREMENT),
	FOREIGN KEY("melos_id") REFERENCES "melos"("melos_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "m_pwlhths" (
	"melos_id" INTEGER,
	"telephone"	TEXT,
	"mesitiko_grafeio_afm" INTEGER,
	PRIMARY KEY("melos_id"),
	FOREIGN KEY("melos_id") REFERENCES "melos"("melos_id") ON DELETE CASCADE,
	FOREIGN KEY("mesitiko_grafeio_afm") REFERENCES "mesitiko_grafeio"("afm") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "mesitiko_grafeio" (
	"afm" INTEGER,
	"brand_name" TEXT,
	"brand_address" TEXT,
	PRIMARY KEY("afm")
);
COMMIT;
