SELECT usuarios.nome, livros.titulo
FROM emprestimos
JOIN usuarios ON emprestimos.id_usuario = usuarios.id_usuario
JOIN livros ON emprestimos.id_livro = livros.id_livro;

SELECT 
    emprestimos.id_emprestimo,
    usuarios.nome AS usuario,
    livros.titulo,
    emprestimos.data_emprestimo,
    emprestimos.data_devolucao
FROM emprestimos
JOIN usuarios ON emprestimos.id_usuario = usuarios.id_usuario
JOIN livros ON emprestimos.id_livro = livros.id_livro;

SELECT 
    usuarios.nome,
    livros.titulo,
    emprestimos.data_emprestimo
FROM emprestimos
JOIN usuarios ON emprestimos.id_usuario = usuarios.id_usuario
JOIN livros ON emprestimos.id_livro = livros.id_livro
WHERE emprestimos.data_devolucao IS NULL;

SELECT 
    usuarios.nome,
    COUNT(emprestimos.id_emprestimo) AS quantidade_emprestimos
FROM usuarios
LEFT JOIN emprestimos 
    ON usuarios.id_usuario = emprestimos.id_usuario
GROUP BY usuarios.id_usuario, usuarios.nome;

SELECT livros.titulo
FROM livros
LEFT JOIN emprestimos 
    ON livros.id_livro = emprestimos.id_livro
WHERE emprestimos.id_emprestimo IS NULL;