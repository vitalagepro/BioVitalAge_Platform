-- Creazione del database principale
DROP DATABASE IF EXISTS LoginRegister;
CREATE DATABASE LoginRegister;
USE LoginRegister;

-- Creazione della tabella Utenti
DROP TABLE IF EXISTS Utenti;

CREATE TABLE Utenti (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    data_registrazione TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Creazione della procedura di login
DELIMITER //
CREATE PROCEDURE login_utente(IN p_email VARCHAR(100), IN p_password VARCHAR(255), OUT esito_login BOOLEAN)
BEGIN
    DECLARE password_match INT;
    SET password_match = (SELECT COUNT(*) FROM utenti WHERE email = p_email AND password = SHA2(p_password, 256));

    IF password_match = 1 THEN
        SET esito_login = TRUE;
    ELSE
        SET esito_login = FALSE;
    END IF;
END //
DELIMITER ;

-- Creazione della tabella Persona
CREATE TABLE IF NOT EXISTS Persona (
id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    dob DATE NOT NULL,
    gender CHAR(1) NOT NULL CHECK (gender IN ('M', 'F')),
    place_of_birth VARCHAR(100) NOT NULL,
    codice_fiscale VARCHAR(16) NOT NULL,
    
    -- Campi per il calcolo dell'età biologica
    chronological_age INT NOT NULL,
    obri_index FLOAT NOT NULL,
    d_roms FLOAT NOT NULL,
    aa_epa FLOAT NOT NULL,
    aa_dha FLOAT NOT NULL,
    homa_test FLOAT NOT NULL,
    cardiovascular_risk FLOAT NOT NULL,
    osi FLOAT NOT NULL,
    pat FLOAT NOT NULL,
    
    -- Risultati dei test dei globuli bianchi
    wbc FLOAT NULL,
    baso FLOAT NULL,
    eosi FLOAT NULL,
    lymph FLOAT NULL,
    mono FLOAT NULL,
    neut FLOAT NULL,

    -- Risultati dei test dei globuli rossi
    rbc FLOAT NULL,
    hct FLOAT NULL,
    hgb FLOAT NULL,
    mch FLOAT NULL,
    mchc FLOAT NULL,
    mcv FLOAT NULL,

    -- Altri marker chiave
    glucose FLOAT NULL,
    creatinine FLOAT NULL,
    ferritin FLOAT NULL,
    albumin FLOAT NULL,
    protein FLOAT NULL,
    bilirubin FLOAT NULL,
    uric_acid FLOAT NULL,

    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;