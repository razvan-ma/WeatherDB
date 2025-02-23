-- Create the Tari table
CREATE TABLE IF NOT EXISTS Tari (
    id SERIAL PRIMARY KEY,
    nume_tara VARCHAR(100) UNIQUE NOT NULL,
    latitudine FLOAT NOT NULL,
    longitudine FLOAT NOT NULL
);

-- Create the Orase table
CREATE TABLE IF NOT EXISTS Orase (
    id SERIAL PRIMARY KEY,
    idtara INT NOT NULL,
    nume_oras VARCHAR(100) NOT NULL,
    latitudine FLOAT NOT NULL,
    longitudine FLOAT NOT NULL,
    UNIQUE (idtara, nume_oras),
    CONSTRAINT fk_tara FOREIGN KEY (idtara) REFERENCES Tari(id) ON DELETE CASCADE
);

-- Create the Temperaturi table
CREATE TABLE IF NOT EXISTS Temperaturi (
    id SERIAL PRIMARY KEY,
    valoare FLOAT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    idoras INT NOT NULL,
    UNIQUE (idoras, timestamp),
    CONSTRAINT fk_oras FOREIGN KEY (idoras) REFERENCES Orase(id) ON DELETE CASCADE
);