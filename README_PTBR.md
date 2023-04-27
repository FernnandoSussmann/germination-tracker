# germination-tracker
Faz um tempo que tenho cuidado de plantas e por isso eu queria acompanhar o processo de germinação mais de perto.

# Como funciona
Ele tira uma foto de uma webcam ou outro dispositivo (como um telescopio eletronico no meu caso) e salva no destino que desejar.

Exemplo:
```sh
poetry run python main.py --cam_index 2 --destination_folder /local/de/destino/do/aquivo/ --filename amostra
```
Resultado:
![Seeds](samples/sample_2023-04-26 11:35:55.568844.png?raw=true)

###### Aviso
O diretório de destino deve existir quando a execução ocorrer.

# Como executar
Você deve instalar o [poetry](https://python-poetry.org/). Dentro da pasta raiz do projeto execute o seguinte comando para atualizar as dependencias:
```sh
poetry update
```
Depois rode:
```sh
poetry run python main.py --cam_index [valor inteiro] --destination_folder [path] --filename [string]
```

## Como testar
Execute:
```sh
poetry run pytest
```

# Nota
Esse projeto só foi testado em distribuições Debian
