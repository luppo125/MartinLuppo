-- Crear tabla OT
CREATE TABLE IF NOT EXISTS OT (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Codigo TEXT,
    Version TEXT,
    MantenimientoCorrectivo TEXT,
    Fecha TEXT,
    Planta TEXT,
    Sector TEXT,
    Parte TEXT,
    Nave TEXT,
    Equipo TEXT,
    Elemento TEXT,
    NombreSolicitante TEXT,
    Area TEXT,
    DescripcionDefecto TEXT,
    Observaciones TEXT,
    Prioridad TEXT,
    Solucion TEXT,
    FechaCierreOT TEXT,
    DescripcionSolucion TEXT,
    MaterialUtilizado TEXT,
    NombreRealizo TEXT,
    AproboSolicitante TEXT,
    AproboMant TEXT,
    AproboCalidad TEXT
);

-- Crear tabla partediario
CREATE TABLE IF NOT EXISTS partediario (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Fecha TEXT,
    Turno TEXT,
    Operador TEXT,
    Actividad TEXT,
    Observaciones TEXT
);
