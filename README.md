# germination-tracker
I have been taking care of plants for some time and I wish to observe closely germination proccess.

# How it works
It takes a picture with a connected webcam or similar device (like a eletronic microscope in my case) and saves it in a destination you have informed.

Example:
```sh
poetry run python main.py --cam_index 2 --destination_folder /path/where/you/want/to/save/the/image/ --filename sample
```
Output:
![Seeds](samples/sample_2023-04-26 11:35:55.568844.png?raw=true)

###### Warning
Path must exists when running the application.

# How to run
You must have [poetry](https://python-poetry.org/) installed. Inside project's root directory run the following to update poetry dependencies:
```sh
poetry update
```
Afterwards run:
```sh
poetry run python main.py --cam_index [int value] --destination_folder [path] --filename [string]
```

## How to test
Run:
```sh
poetry run pytest
```

# Note
This project is currently only tested in Debian based distros
