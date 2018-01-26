#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""LIS3DH: MEMS digital output motion sensor ultra low-power high performance 3-axes 'nano' accelerometer"""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["ST Microelectronics"]
__license__    = "TBD"
__version__    = "Version 0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

#
#   THIS FILE IS AUTOMATICALLY CREATED
#    D O     N O T     M O D I F Y  !
#

class REG:
	STATUS_REG_AUX = 7
	OUT_ADC1_L = 8
	OUT_ADC2_L = 10
	OUT_ADC3_L = 12
	WHO_AM_I = 15
	CTRL_REG0 = 30
	TEMP_CFG_REG = 31
	CTRL_REG1 = 32
	CTRL_REG2 = 33
	CTRL_REG3 = 34
	CTRL_REG4 = 35
	CTRL_REG5 = 35
	CTRL_REG6 = 37
	REFERENCE = 38
	STATUS_REG = 39
	OUT_X_L = 40
	OUT_Y_L = 42
	OUT_Z_L = 44
	FIFO_CTRL_REG = 46
	FIFO_SRC_REG = 47
	INT1_CFG = 48
	INT1_SRC = 49
	INT1_THS = 50
	INT1_DURATION = 51
	INT2_CFG = 52
	INT2_SRC = 53
	INT2_THS = 54
	INT2_DURATION = 55
	CLICK_CFG = 56
	CLICK_SRC = 57
	CLICK_THS = 58
	TIME_LIMIT = 59
	TIME_LATENCY = 60
	TIME_WINDOW = 61
	ACT_THS = 62
