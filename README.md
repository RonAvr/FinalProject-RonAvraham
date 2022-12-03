# Ron Avraham - Final Project

## write_xml_file.py
With this file you can create a new xml file. <br/>
The xml files are saved in the path - gym/envs/mujoco/assets . <br/>
Make sure to change the path of the stl directory under the variable - PATH_TO_MODEL_O_STL_FILES <br/>

## Main.py
Main file to run the simulation. <br/>
In this files, you have 4 inputs the user need to define - 
1. The env you want to load to run the simulation ("Torque" for torque motors, "Pose" for position motors).
2. The output file name (string).
3. The number of the iterations the simulation needs to do (number).
4. The input for the motors (Array size of 3).
<br/>
The output of this simuations are stored in "output_file" directory

<br/>

## Creating a new env -
In order to create a new environment, a class file needs to be created in - gym/envs/mujoco/ <br/>
In this project, We created two new classes. The files can be found in this directory under the names - <br/>

1. [torque_control.py](https://github.com/RonAvr/Ron_Avraham_FInal_Project/blob/master/gym/envs/mujoco/torque_control.py)
2. [position_control.py](https://github.com/RonAvr/Ron_Avraham_FInal_Project/blob/master/gym/envs/mujoco/position_control.py)

In the __init__  method of every class, you need to define the xml file you want to be loaded in this class, the name of the env is the name of the class. <br/>
An example can be found in the next code snippet - 
```python
class Torque(MuJocoPyEnv, utils.EzPickle):
        def __init__(self, **kwargs):
                observation_space = Box(
                    low=-np.inf, high=np.inf, shape=(111,), dtype=np.float64
                )
                MuJocoPyEnv.__init__(
                    self, "torque.xml", 5, observation_space=observation_space, **kwargs
                )
                utils.EzPickle.__init__(self)
```

The xml files needs to be saved in assets directory (gym/envs/mujoco/assets).

<br/>
<br/>

After creating the new Env, we need to declare about this new env in two files - <br/>
in the [init file](https://github.com/RonAvr/Ron_Avraham_FInal_Project/blob/master/gym/envs/mujoco/__init__.py) of the mujoco env we need to import the new class we created in the env
```python
    from gym.envs.mujoco.torque_control import Torque
```

<br/>

And in the [init file](https://github.com/RonAvr/Ron_Avraham_FInal_Project/blob/master/gym/envs/__init__.py) of the envs we need to register this new env - 
```python
    register(
        id="Torque",
        entry_point="gym.envs.mujoco.torque_control:Torque",
        max_episode_steps=1000,
        reward_threshold=9100.0,
    )
```
