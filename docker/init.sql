CREATE TABLE IF NOT EXISTS venda (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    genero VARCHAR(50),
    data TIMESTAMP,
    valor DECIMAL(10, 2),
    quantidade INT,
    produto VARCHAR(255)
);