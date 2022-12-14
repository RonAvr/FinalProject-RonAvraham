import json
import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation as R

RAD_TO_DEG = 57.2957795

FILE_NAME = 'RonTest'
data_file = f'output_files/{FILE_NAME}.json'


def quat_to_rpy(quat, pos):
    """

    Args:
        quat: a quat array
        pos: 1 - for roll, 2 - for pitch, 3 - for yaw

    Returns: return roll/pitch/yaw in degrees

    """
    r = R.from_quat(quat)
    s = r.as_rotvec(degrees=True)
    return(s[pos])

# Loading the data.json file and extracting the pos and time data
f = open(data_file)
data = json.load(f)
pos_data = data['pos_data']
actuators_data = data['actuators_data']
joints_data = data['joints_data']
time = data['time_data']

# Extracting the position data from the data.json file
x_pos = list(map(lambda x:x[0]*1000, pos_data))
y_pos = list(map(lambda x:x[1]*1000, pos_data))
z_pos = list(map(lambda x:x[2]*1000, pos_data))
roll = list(map(lambda x:quat_to_rpy(x[3],0)  , pos_data))
pitch = list(map(lambda x:quat_to_rpy(x[3],1) , pos_data))
yaw = list(map(lambda x:quat_to_rpy(x[3],2) , pos_data))

# Extracting the actuators data from the data.json file
# Data of the right actuator
right_actuator_force = list(map(lambda x:x['actuator_force'][0], actuators_data))
right_actuator_length = list(map(lambda x:x['actuator_length'][0] * 1000, actuators_data))
right_actuator_velocity = list(map(lambda x:x['actuator_velocity'][0], actuators_data))
# Data of the left actuator
left_actuator_force = list(map(lambda x:x['actuator_force'][1], actuators_data))
left_actuator_length = list(map(lambda x:x['actuator_length'][1] * 1000, actuators_data))
left_actuator_velocity = list(map(lambda x:x['actuator_velocity'][1], actuators_data))
# Data of the center actuator
center_actuator_force = list(map(lambda x:x['actuator_force'][2], actuators_data))
center_actuator_length = list(map(lambda x:x['actuator_length'][2] * 1000, actuators_data))
center_actuator_velocity = list(map(lambda x:x['actuator_velocity'][2], actuators_data))
# Extracting the joints data from the data.json file
right_proximal_joint_pos = list(map(lambda x:x['right_proximal'][0] * RAD_TO_DEG, joints_data))
right_proximal_joint_vel = list(map(lambda x:x['right_proximal'][1], joints_data))
right_distal_joint_pos = list(map(lambda x:x['right_distal'][0] * RAD_TO_DEG, joints_data))
right_distal_joint_vel = list(map(lambda x:x['right_distal'][1], joints_data))

left_proximal_joint_pos = list(map(lambda x:x['left_proximal'][0] * RAD_TO_DEG, joints_data))
left_proximal_joint_vel = list(map(lambda x:x['left_proximal'][1], joints_data))
left_distal_joint_pos = list(map(lambda x:x['left_distal'][0] * RAD_TO_DEG, joints_data))
left_distal_joint_vel = list(map(lambda x:x['left_distal'][1], joints_data))

center_proximal_joint_pos = list(map(lambda x:x['center_proximal'][0] * RAD_TO_DEG, joints_data))
center_proximal_joint_vel = list(map(lambda x:x['center_proximal'][1], joints_data))
center_distal_joint_pos = list(map(lambda x:x['center_distal'][0] * RAD_TO_DEG, joints_data))
center_distal_joint_vel = list(map(lambda x:x['center_distal'][1], joints_data))


def plot_graphs():
    fig, axs = plt.subplots(2, 3)
    axs[0, 0].plot(x_pos, linewidth=4)
    axs[0, 0].grid()
    axs[0, 0].set_ylabel('Position, mm', fontsize=15)
    axs[0, 0].set_title('x position')

    axs[0, 1].plot(y_pos, linewidth=4)
    axs[0, 1].grid()
    axs[0, 1].set_title('y position')

    axs[0, 2].plot(z_pos, linewidth=4)
    axs[0, 2].grid()
    axs[0, 2].set_title('z position')

    axs[1, 0].plot(roll, linewidth=4)
    axs[1, 0].grid()
    axs[1, 0].set_ylabel('deg', fontsize=15)
    axs[1, 0].set_title('roll')

    axs[1, 1].plot(pitch, linewidth=4)
    axs[1, 1].grid()
    axs[1, 1].set_title('pitch')
    axs[1, 1].set_xlabel('Steps', fontsize=15)

    axs[1, 2].plot(yaw, linewidth=4)
    axs[1, 2].grid()
    axs[1, 2].set_title('yaw')

    labels = [FILE_NAME]
    fig.suptitle(f'Simulation Output', fontsize=30)
    fig.legend(labels=labels, loc="center right", ncol=1)
    plt.show()


plot_graphs()