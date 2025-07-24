   
## Configuration Parameters

Below are the parameters that can be manually modified to configure the model. These parameters allow you to set up the anthropometric characteristics and control options for the URDF model:
<div align="center">
   
| Parameter        | Description                                                                                                                                 |  
|:----------------:|:-------------------------------------------------------------------------------------------------------------------------------------------:|
| H                | Total height [m]                                                                                             |
| m                | Total body mass [Kg]                                                                                         |
| Neck [X, Y]         | Circumference of the neck [m]                                                                                                                        |
| Chest [X] = TopLumbar [X] =  MidLumbar [X] =  BottomLumbar [X] | Depth of the trunk [m]                                                                                                                  |
| base [X]       | Depth of the pelvis [m]                                                                                                                      |
| Shoulder [Z]  | Width of the shoulder [m]                                                                                                                       |
| UpperArm [X, Z]  | Circumference of the upper arm [m]                                                                                                                   |
| ForeArm [X, Z]   | Circumference of the fore arm [m]                                                                                                                 |
| UpperLeg [X, Y]  | Circumference of the upper leg [m]                                                                                                                 |
| LowerLeg  [X, Y] | Circumference of the lower leg [m]                                                                                                                 |
| Hand [Z]         | Height of the hand [m]                                                                                                                          |
| Hand [X]         | Width of the hand [m]                                                                                                                         |

</div>


## How to measure:
Ensure to follow these guidelines carefully to obtain accurate measurements for configuring the model correctly.

![image](https://github.com/user-attachments/assets/64f9bf63-60d9-4dd0-b1f5-4d0172818581)

![image](https://github.com/user-attachments/assets/587f930b-9473-4871-8934-d5c421b3b131)

![image](https://github.com/user-attachments/assets/52c3a9d7-9760-4c3a-a8bb-090b880a1cd1)

![image](https://github.com/user-attachments/assets/11529104-0c91-4b3c-8bba-7e647215350e)


![image](https://github.com/user-attachments/assets/883d6a65-3af3-40b2-bef7-770703ec37a1)

![image](https://github.com/user-attachments/assets/8347fbce-6097-49ec-8937-f54af9d359f9)

![image](https://github.com/user-attachments/assets/8f1dbaec-45f1-471c-be9a-453fd5edbd11)





## Additional Options

These options provide further customization for the model's consistency check, movement type, and visualization settings:
<div align="center">
   
| Option                              | Value               | Description                                                  |
|:-----------------------------------:|:-------------------:|:-------------------------------------------------------------|
| OPT_CHECK_CONSISTENCY_MODEL         | `True` or `False`   | Check the consistency of the model                         |
| OPT_VISUALIZZATION_MODEL            | `True` or `False`   | Visualize the movement                                      |
| OPT_VISUALIZZATION_MEASUREOFCONTROL | `True` or `False`   | Visualize the measure of control                           |
| OPT_VISUALIZATION_MESH | `True` or `False`   | Visualize the meshes of the model                           |
| OPT_VISUALIZATION_MUSCLES | `True` or `False`   | Visualize the muscles meshes of the model                           |
| OPT_VISUALIZATION_SPINALCORD | `True` or `False`   | Visualize the spinal cord meshes of the model                           |
| OPT_COLOR_LINK_MESH                 | `[R, G, B, alpha]`  | Defines the RGBA color of the link mesh for visualization, with alpha transparency factor   |
| OPT_COLOR_MUSCLE_MESH               | `[R, G, B, alpha]`  | Defines the RGBA color of the muscle mesh for visualization, with alpha transparency factor  |
| OPT_COLOR_SPINALCORD_MESH               | `[R, G, B, alpha]`  | Defines the RGBA color of the spinal cord mesh for visualization, with alpha transparency factor  |



</div>


