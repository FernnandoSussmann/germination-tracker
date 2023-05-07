# germination-tracker
Faz um tempo que tenho cuidado de plantas e por isso eu queria acompanhar o processo de germinação mais de perto.

# Como funciona
Ele tira uma foto de uma webcam ou outro dispositivo (como um telescopio eletronico no meu caso) e salva no destino que desejar.

Exemplo:
```sh
poetry run python main.py --cam_index 2 --destination_folder /local/de/destino/do/aquivo/ --filename amostra
```
Resultado:\
![Seeds](https://github.com/FernnandoSussmann/germination-tracker/blob/main/samples/sample_2023-04-26%2011:35:55.568844.png?raw=true)

Também é possível criar um gif das imagens coletadas:
Example:
```sh
poetry run python gif.py -sf /local/que/possui/as/imagens/capturadas/ -df /local/de/destino/do/gif/ -fn sample -imf png
```

Output:\
![SeedsGrowing](https://github.com/FernnandoSussmann/germination-tracker/blob/creating_gif_from_images/samples/sample.gif?raw=true)

###### Aviso
Os diretórios de destino devem existir quando a execução ocorrer.

# Como executar
###### Todo script tem a opção -h ou --help para descrever seus argumentos 
Você deve instalar o [poetry](https://python-poetry.org/). Dentro da pasta raiz do projeto execute o seguinte comando para atualizar as dependencias:
```sh
poetry update
```
Depois rode:
```sh
poetry run python main.py --cam_index [valor inteiro] --destination_folder [path] --filename [string]
```

## Criando gif das suas imagens
Para criar gif das imagens coletadas você precisa executar o script `gif.py` da seguinte maneira:
```sh
poetry run python gif.py --source_folder [path] --destination_folder [path] --filename [valor str] --images_format [valor str] --duration [valor int (opcional)] --loops [valor int (opcional)]
```


## Como testar
Execute:
```sh
poetry run pytest
```

# Nota
Esse projeto só foi testado em distribuições Debian
