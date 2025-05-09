CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO usuarios (name, email) VALUES
('João Silva', 'joao@exemplo.com'),
('Maria Souza', 'maria@exemplo.com'),
('Carlos Pereira', 'carlos@exemplo.com');