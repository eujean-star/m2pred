# plpred
     predict a protein subcellular location

## Project Structure 

- `environment.yml`: Arquivo relacionado com as especificações do ambiente que são necessário  para rodar o projeto. 

- `requirement.txt`:Caso não esteja usando um gerenciador de ambientes, utilize o código ``` pip install - r requirements``` para iinstalar as biblíotecas que serão usadas pelo Python.

- `Makefile` Arquivo útil para configurar o ambiente de maneira mais fácil, utilize o comando:
    ```
     $ make setup
    ```
- `data/`: pasta contendo os dados utilizados no programa.
     - `raw`: dados brutos
     - `processed`: dados processados 
     