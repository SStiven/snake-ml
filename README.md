Simple Snake Game

A simple snake game implemented in Python using Pygame.

Installation

Installing Python and Pip
If you don't have Python installed, download and install it from the official website. Pip is included as a part of Python installations from Python 3.10.
Python official website: https://www.python.org/downloads/

To verify the installation, open a terminal/command prompt and type:


$ python --version
$ pip --version

You should see the versions of installed Python and Pip.

Setting up a Virtual Environment

Go to your project directory and create a new virtual environment:

$ cd path/to/project
$ python -m venv env

Activate the virtual environment:

On Windows, run:

$ .\env\Scripts\activate

On Unix or MacOS, run:

$ source env/bin/activate

The name of the current virtual environment will now appear on the left of the prompt to let you know that it's active.

Installing Dependencies

After activating the virtual environment, install the project dependencies:

$ pip install -r requirements.txt

Running the Game

Once you've set up your environment and installed the dependencies, you can run the game:

$ python main.py
