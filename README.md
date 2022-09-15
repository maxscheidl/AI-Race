# AI-Race

This is a 2D - Racing game played by AI. 
The application lets you train your own neuronal network and visualizes the results.

There are two applications which can be used:  

### AI - Evolution

In this application everything is self-implemented.  
The class **Evolution** is used to train the cars iteratively by evolving and mutating the best neuronal networks.

If you start the program an already trained network is used to drive the cars. If you want to start the training from zero 
you have to comment the self.load_best_network() function in the constructor of the evolution class.

#### Controls

There are some keyboard interaction which can be used while running the program:

- To save the current best network the library **pickle** is used. With the keys 1, 2 and 3 you can save a 
network to one of three pickle files and use them again later.
- To in- or decrease the mutation rate simply press + or - and it will chance by 0.01.

#### Roads

In the class **road** you can switch between different roads and also create your own ones. The roads are
build of different segments which can be put together easily - take a look at the predefined tracks.
To change the road you have to initialize another road in the constructor. 

#### Try to drive the car yourself

It is also possible to drive a car on your own. Therefore, you have to edit the code in **main.py**.  
simply uncomment the line 28 and comment lines 30 and 31. To control the car the keys Up, Down, Left, Right are used.


### AI - Neat

This application uses the library **Python Neat** to train the AI.
To configure the algorithm simply make changes in **config_file.txt** .
