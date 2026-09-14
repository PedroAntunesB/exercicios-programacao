UPDATE usuarios
SET nome = 'Carlos'
WHERE id_usuario = 1;

UPDATE emprestimos
SET data_devolucao = '2026-09-14'
WHERE id_emprestimo = 1;

UPDATE emprestimos
SET data_devolucao = '2026-09-14'
WHERE id_emprestimo = 2;

SELECT * FROM emprestimos
WHERE id_usuario = 1;

DELETE FROM emprestimos
WHERE id_usuario = 1;

DELETE FROM usuarios
WHERE id_usuario = 1;

SELECT * FROM emprestimos
WHERE id_livro = 1;

DELETE FROM livros
WHERE id_livro = 1;