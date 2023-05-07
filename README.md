# germination-tracker
I have been taking care of plants for some time and I wish to observe closely germination proccess.

# How it works
It takes a picture with a connected webcam or similar device (like a eletronic microscope in my case) and saves it in a destination you have informed.

Example:
```sh
poetry run python main.py --cam_index 2 --destination_folder /path/where/you/want/to/save/the/image/ --filename sample
```
Output:\
![Seeds](https://github.com/FernnandoSussmann/germination-tracker/blob/main/samples/sample_2023-04-26%2011:35:55.568844.png?raw=true)

It is also possible to create a gif image with all those images you have took with the previous step:
Example:
```sh
poetry run python gif.py -sf /path/where/you/have/saved/your/images/ -df /path/where/you/want/to/save/gif/image/ -fn sample -imf png
```

Output:\
![SeedsGrowing](https://github.com/FernnandoSussmann/germination-tracker/blob/creating_gif_from_images/samples/sample.gif?raw=true)

###### Warning
Path must exists when running the application.

# How to run
###### Every executable script has -h or --help to explain it's arguments 
You must have [poetry](https://python-poetry.org/) installed. Inside project's root directory run the following to update poetry dependencies:
```sh
poetry update
```
Afterwards run:
```sh
poetry run python main.py --cam_index [int value] --destination_folder [path] --filename [string]
```

## Creating gif from images
To create a gif of the set of images you have generated you can run `gif.py` utility in the following way:
```sh
poetry run python gif.py --source_folder [path] --destination_folder [path] --filename [str value] --images_format [str value] --duration [int value (optional)] --loops [int value (optional)]
```


## How to test
Run:
```sh
poetry run pytest
```

# Note
This project is currently only tested in Debian based distros
