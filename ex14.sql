INSERT INTO autores (id_autor, nome) VALUES
(1, 'Machado de Assis'),
(2, 'Clarice Lispector'),
(3, 'George Orwell'),
(4, 'J. K. Rowling'),
(5, 'J. R. R. Tolkien');

INSERT INTO livros (id_livro, titulo, ano_publicacao, id_autor) VALUES
(1, 'Dom Casmurro', 1899, 1),
(2, 'A Hora da Estrela', 1977, 2),
(3, '1984', 1949, 3),
(4, 'Harry Potter e a Pedra Filosofal', 1997, 4),
(5, 'O Hobbit', 1937, 5);

INSERT INTO usuarios (id_usuario, nome, email) VALUES
(1, 'Pedro', 'pedro@email.com'),
(2, 'Maria', 'maria@email.com'),
(3, 'João', 'joao@email.com');

INSERT INTO emprestimos 
(id_emprestimo, id_livro, id_usuario, data_emprestimo, data_devolucao) 
VALUES
(1, 1, 1, '2026-09-01', NULL),
(2, 3, 2, '2026-09-03', NULL),
(3, 5, 3, '2026-09-05', '2026-09-10');

SELECT * FROM livros;

SELECT livros.titulo, autores.nome AS autor
FROM livros
JOIN autores ON livros.id_autor = autores.id_autor;

SELECT livros.titulo
FROM livros
JOIN autores ON livros.id_autor = autores.id_autor
WHERE autores.nome = 'Machado de Assis';

SELECT * FROM livros
ORDER BY titulo ASC;

SELECT livros.titulo
FROM livros
WHERE livros.id_livro NOT IN (
    SELECT id_livro
    FROM emprestimos
    WHERE data_devolucao IS NULL
);