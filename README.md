# Clonando um repositório

Qualquer repositório disponível publicamente no GitHub pode ser clonado, ou seja, uma versão especificada é copiada para um repositório local, onde pode ser usada(caso de softwares ou arquivos de build), modificada(alterar algum parâmetro, renomear arquivos) e melhorada(contribuições open-source, implementar novas funções e recursos, criar novos arquivos).

## Módulo math_utils.py

Pequeno módulo com funções matemáticas para exemplificar o ciclo de desenvolvimento open-source

Cada participante deverá:

1. Clonar este repositório usando o GitHub Desktop.
2. Criar um novo *branch*.
3. Adicionar ou modificar funções e recursos.
4. Fazer *commit* das alterações.
5. Fazer um *merge* com o branch `master`
6. Criar um Pull Request no GitHub para sugerir as mudanças realizadas.

### Sugestões de funções

- is_prime(n): Retorna true se o número é primo.
- fibonnacci(n): Retorna o enésimo número de fibonacci
- factorial(n): Operação de fatorial
- nCr(n, r): Faz a combinação simples de n objetos para r opções
- is_even(n): Retorna true se o número é par
- is_div(n, i): Retorna true se n é divisível por i
- pow_int(n, p): Calcula n elevado à p, ambos inteiros

## Módulo tests.py

Módulo de testes para as funções do módulo math_utils.py

Caso implementada alguma função `math_func`, implementar também a função de teste `test_math_func` nesse módulo
