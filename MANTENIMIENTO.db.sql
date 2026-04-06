BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "OT" (
	"ID"	INTEGER,
	"Codigo"	TEXT,
	"Version"	TEXT,
	"Mantenimiento correctivo"	TEXT,
	"Fecha"	TEXT,
	"Planta"	TEXT,
	"Sector"	TEXT,
	"parte"	TEXT,
	"nave"	TEXT,
	"Equipo"	TEXT,
	"elemento"	TEXT,
	"Nombre del solicitante"	TEXT,
	"Area"	TEXT,
	"Descripcion del defecto"	TEXT,
	"Observaciones"	TEXT,
	"Prioridad"	TEXT,
	"Solucion"	TEXT,
	"Fecha cierre ot"	TEXT,
	"Descripcion solucion"	TEXT,
	"material utilizado"	TEXT,
	"nombrerealizo"	TEXT,
	"aprobo solicitante"	TEXT,
	"aprobo mant"	TEXT,
	"aprobo calidad"	TEXT,
	"Realizada"	TEXT,
	PRIMARY KEY("ID")
);
CREATE TABLE IF NOT EXISTS "Partediario" (
	"ID"	INTEGER,
	"Fecha"	TEXT,
	"Nombre"	TEXT,
	"Turno"	TEXT,
	"Codigo maquina"	TEXT,
	"Reporte"	TEXT,
	PRIMARY KEY("ID")
);
CREATE TABLE IF NOT EXISTS "mecanicos" (
	"id"	INTEGER,
	"nombre"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "sectores" (
	"id"	INTEGER,
	"nombre"	TEXT NOT NULL,
	"planta"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
COMMIT;
