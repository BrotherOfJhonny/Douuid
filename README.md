# Gerador de UUID a partir de CPFs ou CNPJs

Este é um simples script em Python que lê um arquivo contendo uma lista de CPFs ou CNPJs, um por linha, e gera UUIDs Version 1 a partir desses números. O UUID gerado é baseado no hash MD5 dos dígitos do CPF ou CNPJ.

## Requisitos

- Python 3.x (https://www.python.org/downloads/)

## Como usar

1. Certifique-se de que o Python 3.x está instalado no seu sistema.

2. Coloque o script `Douuid.py` e o arquivo contendo a lista de CPFs ou CNPJs no mesmo diretório.

3. Execute o script `Douuid.py` digitando o seguinte comando no terminal:

python Douuid.py


4. O script irá solicitar o nome do arquivo contendo a lista de CPFs ou CNPJs. Digite o nome do arquivo e pressione Enter.

5. O script irá gerar os UUIDs Version 1 a partir dos CPFs ou CNPJs e salvá-los em um arquivo chamado `uuid_list.txt` no mesmo diretório.

6. A lista de UUIDs gerada estará disponível no arquivo `uuid_list.txt`.

## Observações

- Certifique-se de que o arquivo contendo a lista de CPFs ou CNPJs esteja no mesmo diretório do script. Caso contrário, forneça o caminho completo do arquivo durante a execução do script.

- O script removerá os caracteres não numéricos do CPF ou CNPJ antes de calcular o UUID. Caso algum CPF ou CNPJ não tenha dígitos após a remoção desses caracteres, o UUID correspondente será considerado inválido e não será incluído na lista final.

- Os UUIDs gerados pelo script são do tipo Version 1 (baseados no tempo), utilizando os dígitos do CPF ou CNPJ como identificador de nó (node).

## Aviso Legal

Este script foi criado com o propósito de ser utilizado em um ambiente controlado e hipotético, para fins educacionais e de demonstração. Não é recomendado o uso deste script para fins maliciosos ou ilegais. O autor não se responsabiliza pelo uso indevido deste script ou por qualquer consequência decorrente de seu uso.

