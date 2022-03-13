# Clash-Clash

## Setup

1. colorama is required for the app to run. To install colorama,

```bash
pip3 install colorama
```

2. To run the game,

```bash
python3 game.py
```

3. To view replays,
```bash
python3 replay.py
```

## The Game

### I. Starting the Game

When the user runs the game, they will be greeted by a welcome screen. Some really cool background music has also been added as an extra creative feature. From here, the user can press <kbd>S</kbd> to start the game, or <kbd>Q</kbd> to quit.

### II. Battle

At any point in the game, pressing <kbd>Q</kbd> will allow the user to quit the game.

#### The King

The village is a grid of squares. The user controls the King, who starts in the top left corner, and can move around the grid by using the following keys.

<kbd>W</kbd> - Move up<br>
<kbd>A</kbd> - Move left<br>
<kbd>S</kbd> - Move down<br>
<kbd>D</kbd> - Move right<br>

The village consists of 1 Town Hall, 3 Cannons and 5 Huts, as well as walls surrounding the Town Hall to protect it. The King can only move to a square that is not occupied by a building. The King can attack in 2 different ways.

<kbd>Space</kbd> - Targeted attack on the square directly next to the King.<br>
<kbd>L</kbd> - Perform a Leviathan Axe attack, unleashing splash damage in an area of 10x10 around the King.<br>

#### Barbarians

Barbarians are troops that can be used to assist the king in battle. They can be spawned by pressing <kbd>1</kbd>, <kbd>2</kbd> or <kbd>3</kbd>, which spawns them at one of the 3 spawning points in the village accordingly. They target the nearest building, moving towards it and attack it.

The nearest distance is calculated using Manhattan distance, which is `|x1 - x2| + |y1 - y2|`.

#### The Cannons

While the Huts, Town Hall and Walls are static buildings, the Cannons are buildings that defend the village by shooting at player troops. The range of a cannon is 5x5 around the Cannon. The Cannons attack periodically after a certain number of iterations of the game loop.

#### Spells

Spells can be cast to boost your troops and give you the extra edge.

<kbd>R</kbd> - Activates the Rage spell, which doubles the speed and damage of your troops.

<kbd>H</kbd> - Activates the Heal spell, which increases the current health of each active troop by 150%.

The above spells can only be used once per game.

### III. End of the Game

Once your active troops are all killed, you lose the game. If all buildings have been destroyed, you win the game.

## OOPS Concepts Implemented

### I. Inheritance

1. The Building class serves as the base class, from which the Town Hall, Wall, Cannon and Hut classes inherit.

2. The King and Barbarian classes inherit from the Troop class.

### II. Abstraction

Two examples of abstraction are the `move()` and `attack()` methods of the Barbarian class. The inner details and implementation of movement and attacking are hidden from the user, and the user can simply add them to the code in the game loop to implement the function.

### III. Encapsulation

In this game, all functions or variables pertaining to a particular game entity are bundled under a single class. The functionality can then be accessed by simply calling the method via the class object.

### IV. Polymorphism

The Troop class has an `attack()` method. However, the Barbarian class has its specific `attack()` method that overrides the default Troop's `attack()` method.