CREATE TABLE companies (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    sector TEXT NOT NULL
);

CREATE TABLE reports (
    id INTEGER PRIMARY KEY,
    company_id INTEGER NOT NULL REFERENCES companies(id),
    fiscal_year INTEGER NOT NULL,
    file_name TEXT NOT NULL
);