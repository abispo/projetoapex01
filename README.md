# Projeto de cálculo de notas de alunos

* Nesse projeto, você vai criar uma página onde irá cadastrar o nome de alunos e 3 notas que esses alunos tiraram em provas.
* Portanto, nesse formulário haverá 4 campos do tipo `text`: nome_do_aluno, nota1, nota2 e nota3.
* Haverá também um botão de `enviar`, que enviará o usuário para uma página contendo a mensagem `Notas registradas com sucesso`.
* Nessa página de mensagem, haverá 2 links: 1 que levará o usuário de volta a página de cadastro de notas e outro que enviará o usuário para uma página de resultados
* Essa página de resultados mostrará as notas e as médias de todos os alunos que foram cadastrados, e também uma mensagem mostrando se o aluno foi aprovado ou não. Considere como aprovado um aluno com a nota igual ou maior que 7. Por exemplo:
    ```
    Aluno: Maria
    N1: 7
    N2: 8
    N3: 9
    Média final: 8
    O aluno foi aprovado.
    
    Aluno: João
    N1: 5
    N2: 5
    N3: 8
    Média final: 6
    O aluno foi reprovado.
    ```
  
## Passos
* Configurar a IDE para usar o git bash
* Abrir o terminal e instalar o Django: `pipenv install`
* Entrar no diretório `notas` pelo terminal (`cd notas`) e digitar o comando `python manage.py startapp grades`
* Verificar se está tudo ok digitando `python manage.py runserver`.