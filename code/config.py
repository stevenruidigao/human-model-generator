# SPDX-FileCopyrightText: Fondazione Istituto Italiano di Tecnologia
#
# SPDX-License-Identifier: BSD-3-Clause

""" OPTIONS"""
import numpy as np

OPT_CHECK_CONSISTENCY_MODEL = True  # 'True' or 'False
OPT_VISUALIZZATION_MODEL = True  # 'True' or 'False
OPT_VISUALIZZATION_MEASUREOFCONTROL = True  # 'True' or 'False
OPT_VISUALIZATION_MESH = True  # 'True' or 'False
OPT_VISUALIZATION_MUSCLES = True  # 'True' or 'False
OPT_VISUALIZATION_SPINALCORD = True  # 'True' or 'False



OPT_COLOR_LINK_MESH = [0.9922, 0.8667, 0.7922, 1.0]
OPT_COLOR_MUSCLE_MESH = [0.9922, 0.8667, 0.7922, 1.0]
OPT_COLOR_SPINALCORD_MESH = [0.9922, 0.8667, 0.7922, 1.0]


""" ANTHROPOMETRIC MEASUREMENTS"""

H = 1.8
m = 68.0


# some neck,trunk,arm and leg dimensions in [m]
from src import linkDimensions

linkDimensions["Neck"]["X"] = linkDimensions["Neck"]["Y"] = 0.32
linkDimensions["Chest"]["X"] = linkDimensions["TopLumbar"]["X"] = linkDimensions["MidLumbar"]["X"] = linkDimensions["BottomLumbar"]["X"] = 0.19
linkDimensions["base"]["X"] = 0.225
linkDimensions["Shoulder"]["Z"] = 0.115
linkDimensions["UpperArm"]["X"] = linkDimensions["UpperArm"]["Z"] = 0.28
linkDimensions["ForeArm"]["X"] = linkDimensions["ForeArm"]["Z"] = 0.22
linkDimensions["UpperLeg"]["X"] = linkDimensions["UpperLeg"]["Y"] = 0.47
linkDimensions["LowerLeg"]["X"] = linkDimensions["LowerLeg"]["Y"] = 0.34
linkDimensions["Hand"]["Z"] = 0.025
linkDimensions["Hand"]["X"] = 0.085