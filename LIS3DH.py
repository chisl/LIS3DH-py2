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

from LIS3DH_constants import *

# name:        LIS3DH
# description: MEMS digital output motion sensor ultra low-power high performance 3-axes 'nano' accelerometer
# manuf:       ST Microelectronics
# version:     Version 0.1
# url:         http://www.st.com/resource/en/datasheet/lis3dh.pdf
# date:        2018-01-26


# Derive from this class and implement read and write
class LIS3DH_Base:
	"""MEMS digital output motion sensor ultra low-power high performance 3-axes 'nano' accelerometer"""
	# Register STATUS_REG_AUX
	# 8.1 
	
	def setSTATUS_REG_AUX(self, val):
		"""Set register STATUS_REG_AUX"""
		self.write(REG.STATUS_REG_AUX, val, 8)
	
	def getSTATUS_REG_AUX(self):
		"""Get register STATUS_REG_AUX"""
		return self.read(REG.STATUS_REG_AUX, 8)
	
	# Bits OR321
	# 1, 2 and 3-axis data overrun. 
	# Bits OR3
	# 3-axis data overrun. 
	# Bits OR2
	# 2-axis data overrun. 
	# Bits OR1
	# 1-axis data overrun. 
	# Bits DA321
	# 1, 2 and 3-axis new data available. 
	# Bits DA3
	# 3-axis new data available. 
	# Bits DA2
	# 2 -axis new data available. 
	# Bits DA1
	# 1-axis new data available. 
	# Register OUT_ADC1_L
	# 8.2
	#       Auxiliary 10-bit ADC channel 1 conversion. For auxiliary ADC setting refer 
	#       to Section 3.7: Auxiliary ADC and temperature sensor. 
	
	
	def setOUT_ADC1_L(self, val):
		"""Set register OUT_ADC1_L"""
		self.write(REG.OUT_ADC1_L, val, 8)
	
	def getOUT_ADC1_L(self):
		"""Get register OUT_ADC1_L"""
		return self.read(REG.OUT_ADC1_L, 8)
	
	# Bits OUT_ADC1_L
	# Register OUT_ADC2_L
	# 8.3
	#       Auxiliary 10-bit ADC channel 2 conversion. For auxiliary ADC setting refer 
	#       to Section 3.7: Auxiliary ADC and temperature sensor. 
	
	
	def setOUT_ADC2_L(self, val):
		"""Set register OUT_ADC2_L"""
		self.write(REG.OUT_ADC2_L, val, 8)
	
	def getOUT_ADC2_L(self):
		"""Get register OUT_ADC2_L"""
		return self.read(REG.OUT_ADC2_L, 8)
	
	# Bits OUT_ADC2_L
	# Register OUT_ADC3_L
	# 8.4
	#       Auxiliary 10-bit ADC channel 3 conversion or temperature sensor data output. Refer to
	#       Section 3.7: Auxiliary ADC and temperature sensor. 
	
	
	def setOUT_ADC3_L(self, val):
		"""Set register OUT_ADC3_L"""
		self.write(REG.OUT_ADC3_L, val, 8)
	
	def getOUT_ADC3_L(self):
		"""Get register OUT_ADC3_L"""
		return self.read(REG.OUT_ADC3_L, 8)
	
	# Bits OUT_ADC3_L
	# Register WHO_AM_I
	# 8.5
	#       Device identification register. 
	
	
	def setWHO_AM_I(self, val):
		"""Set register WHO_AM_I"""
		self.write(REG.WHO_AM_I, val, 8)
	
	def getWHO_AM_I(self):
		"""Get register WHO_AM_I"""
		return self.read(REG.WHO_AM_I, 8)
	
	# Bits WHO_AM_I
	# Register CTRL_REG0
	# 8.6 
	
	def setCTRL_REG0(self, val):
		"""Set register CTRL_REG0"""
		self.write(REG.CTRL_REG0, val, 8)
	
	def getCTRL_REG0(self):
		"""Get register CTRL_REG0"""
		return self.read(REG.CTRL_REG0, 8)
	
	# Bits SDO_PU_DISC
	# Disconnect SDO/SA0 pull-up. 
	# Bits reserved_0
	# Note: Leave bits 0 through 6 at the default value in order to ensure correct 
	#           operation of the device. 
	
	# Register TEMP_CFG_REG
	# 8.7 
	
	def setTEMP_CFG_REG(self, val):
		"""Set register TEMP_CFG_REG"""
		self.write(REG.TEMP_CFG_REG, val, 8)
	
	def getTEMP_CFG_REG(self):
		"""Get register TEMP_CFG_REG"""
		return self.read(REG.TEMP_CFG_REG, 8)
	
	# Bits ADC_EN
	# ADC enable. 
	# Bits TEMP_EN
	# Temperature sensor (T) enable. 
	# Bits unused_0
	# Register CTRL_REG1
	
	
	def setCTRL_REG1(self, val):
		"""Set register CTRL_REG1"""
		self.write(REG.CTRL_REG1, val, 8)
	
	def getCTRL_REG1(self):
		"""Get register CTRL_REG1"""
		return self.read(REG.CTRL_REG1, 8)
	
	# Bits ODR
	# ODR[3:0] is used to set the power mode and ODR selection. 
	# Bits LPen
	# Low-power mode enable. 
	# Bits Zen
	# Z-axis enable. 
	# Bits Yen
	# Y-axis enable. 
	# Bits Xen
	# X-axis enable. 
	# Register CTRL_REG2
	# 8.9 
	
	def setCTRL_REG2(self, val):
		"""Set register CTRL_REG2"""
		self.write(REG.CTRL_REG2, val, 8)
	
	def getCTRL_REG2(self):
		"""Get register CTRL_REG2"""
		return self.read(REG.CTRL_REG2, 8)
	
	# Bits HPM
	# High-pass filter mode selection. 
	# Bits HPCF
	# High-pass filter cutoff frequency selection 
	# Bits FDS
	# Filtered data selection. 
	# Bits HPCLICK
	# High-pass filter enabled for CLICK function. 
	# Bits HP_IA2
	# High-pass filter enabled for AOI function on interrupt 2, 
	# Bits HP_IA1
	# High-pass filter enabled for AOI function on interrupt 1, 
	# Register CTRL_REG3
	# 8.10 
	
	def setCTRL_REG3(self, val):
		"""Set register CTRL_REG3"""
		self.write(REG.CTRL_REG3, val, 8)
	
	def getCTRL_REG3(self):
		"""Get register CTRL_REG3"""
		return self.read(REG.CTRL_REG3, 8)
	
	# Bits I1_CLICK
	# Click interrupt on INT1. 
	# Bits I1_IA1
	# IA1 interrupt on INT1. 
	# Bits I1_IA2
	# IA2 interrupt on INT1. 
	# Bits I1_ZYXDA
	# ZYXDA interrupt on INT1. 
	# Bits I1_321DA
	# 321DA interrupt on INT1. 
	# Bits I1_WTM
	# FIFO watermark interrupt on INT1. 
	# Bits I1_OVERRUN
	# FIFO overrun interrupt on INT1. 
	# Bits unused_0
	# Register CTRL_REG4
	# 8.11 
	
	def setCTRL_REG4(self, val):
		"""Set register CTRL_REG4"""
		self.write(REG.CTRL_REG4, val, 8)
	
	def getCTRL_REG4(self):
		"""Get register CTRL_REG4"""
		return self.read(REG.CTRL_REG4, 8)
	
	# Bits BDU
	# Block data update. 
	# Bits BLE
	# Big/little endian data selection.
	#           The BLE function can be activated only in high-resolution mode. 
	
	# Bits FS
	# Full-scale selection. 
	# Bits HR
	# High-resolution output mode: 
	# Bits ST
	# Self-test enable. 
	# Bits SIM
	# SPI serial interface mode selection. 
	# Register CTRL_REG5
	# 8.12 
	
	def setCTRL_REG5(self, val):
		"""Set register CTRL_REG5"""
		self.write(REG.CTRL_REG5, val, 8)
	
	def getCTRL_REG5(self):
		"""Get register CTRL_REG5"""
		return self.read(REG.CTRL_REG5, 8)
	
	# Bits BOOT
	# Reboot memory content. 
	# Bits FIFO_EN
	# FIFO enable. 
	# Bits unused_0
	# Bits LIR_INT1
	# Latch interrupt request on INT1_SRC register, with INT1_SRC (31h) register cleared 
	#         by reading INT1_SRC (31h) itself. 
	
	# Bits D4D_INT1
	# 4D enable: 4D detection is enabled on INT1 when 6D bit on INT1_CFG is set to 1. 
	# Bits LIR_INT2
	# Latch interrupt request on INT2_SRC (35h) register, with INT2_SRC (35h) 
	#           register cleared by reading INT2_SRC (35h) itself. 
	
	# Bits D4D_INT2
	# 4D enable: 4D detection is enabled on INT2 pin when 6D bit on INT2_CFG 
	#           (34h) is set to 1. 
	
	# Register CTRL_REG6
	# 8.13 
	
	def setCTRL_REG6(self, val):
		"""Set register CTRL_REG6"""
		self.write(REG.CTRL_REG6, val, 8)
	
	def getCTRL_REG6(self):
		"""Get register CTRL_REG6"""
		return self.read(REG.CTRL_REG6, 8)
	
	# Bits I2_CLICK
	# Click interrupt on INT2 pin. 
	# Bits I2_IA1
	# Enable interrupt 1 function on INT2 pin. 
	# Bits I2_IA2
	# Enable interrupt 2 function on INT2 pin. 
	# Bits I2_BOOT
	# Enable boot on INT2 pin. 
	# Bits I2_ACT
	# Enable activity interrupt on INT2 pin. 
	# Bits unused_0
	# Bits INT_POLARITY
	# INT1 and INT2 pin polarity. 
	# Bits unused_1
	# Register REFERENCE
	# Reference value for Interrupt generation. 
	
	def setREFERENCE(self, val):
		"""Set register REFERENCE"""
		self.write(REG.REFERENCE, val, 8)
	
	def getREFERENCE(self):
		"""Get register REFERENCE"""
		return self.read(REG.REFERENCE, 8)
	
	# Bits REFERENCE
	# Register STATUS_REG
	# 8.15 
	
	def setSTATUS_REG(self, val):
		"""Set register STATUS_REG"""
		self.write(REG.STATUS_REG, val, 8)
	
	def getSTATUS_REG(self):
		"""Get register STATUS_REG"""
		return self.read(REG.STATUS_REG, 8)
	
	# Bits ZYXOR
	# X, Y and Z-axis data overrun. 
	# Bits ZOR
	# Z-axis data overrun. 
	# Bits YOR
	# Y-axis data overrun. 
	# Bits XOR
	# X-axis data overrun. 
	# Bits ZYXDA
	# X, Y and Z-axis new data available. 
	# Bits ZDA
	# Z-axis new data available. 
	# Bits YDA
	# Y-axis new data available. 
	# Bits XDA
	# X-axis new data available. 
	# Register OUT_X_L
	# 8.16
	#       X-axis acceleration data. The value is expressed as two’s complement left-justified. 
	#       Please refer to Section 3.2.1: High-resolution, normal mode, low-power mode. 
	
	
	def setOUT_X_L(self, val):
		"""Set register OUT_X_L"""
		self.write(REG.OUT_X_L, val, 8)
	
	def getOUT_X_L(self):
		"""Get register OUT_X_L"""
		return self.read(REG.OUT_X_L, 8)
	
	# Bits OUT_X_L
	# Register OUT_Y_L
	# 8.17
	#       Y-axis acceleration data. The value is expressed as two’s complement left-justified. 
	#       Please refer to Section 3.2.1: High-resolution, normal mode, low-power mode. 
	
	
	def setOUT_Y_L(self, val):
		"""Set register OUT_Y_L"""
		self.write(REG.OUT_Y_L, val, 8)
	
	def getOUT_Y_L(self):
		"""Get register OUT_Y_L"""
		return self.read(REG.OUT_Y_L, 8)
	
	# Bits OUT_Y_L
	# Register OUT_Z_L
	# 8.18
	#       Z-axis acceleration data. The value is expressed as two’s complement left-justified. 
	#       Please refer to Section 3.2.1: High-resolution, normal mode, low-power mode. 
	
	
	def setOUT_Z_L(self, val):
		"""Set register OUT_Z_L"""
		self.write(REG.OUT_Z_L, val, 8)
	
	def getOUT_Z_L(self):
		"""Get register OUT_Z_L"""
		return self.read(REG.OUT_Z_L, 8)
	
	# Bits OUT_Z_L
	# Register FIFO_CTRL_REG
	# 8.19 
	
	def setFIFO_CTRL_REG(self, val):
		"""Set register FIFO_CTRL_REG"""
		self.write(REG.FIFO_CTRL_REG, val, 8)
	
	def getFIFO_CTRL_REG(self):
		"""Get register FIFO_CTRL_REG"""
		return self.read(REG.FIFO_CTRL_REG, 8)
	
	# Bits FM
	# FIFO mode selection. 
	# Bits TR
	# Trigger selection. 
	# Bits FTH
	# Register FIFO_SRC_REG
	
	
	def setFIFO_SRC_REG(self, val):
		"""Set register FIFO_SRC_REG"""
		self.write(REG.FIFO_SRC_REG, val, 8)
	
	def getFIFO_SRC_REG(self):
		"""Get register FIFO_SRC_REG"""
		return self.read(REG.FIFO_SRC_REG, 8)
	
	# Bits WTM
	# WTM bit is set high when FIFO content exceeds watermark level 
	# Bits OVRN_FIFO
	# OVRN bit is set high when FIFO buffer is full; this means that the FIFO buffer contains 
	#           32 unread samples. At the following ODR a new sample set replaces the oldest FIFO value. 
	#           The OVRN bit is set to 0 when the first sample set has been read. 
	
	# Bits EMPTY
	# EMPTY flag is set high when all FIFO samples have been read and FIFO is empty 
	# Bits FSS
	# The FSS field always contains the current number of unread samples stored in 
	#           the FIFO buffer. When FIFO is enabled, this value increases at ODR frequency 
	#           until the buffer is full, whereas, it decreases every time one sample set is retrieved from FIFO. 
	
	# Register INT1_CFG
	# 8.21 
	#       Content of this register is loaded at boot. 
	#       Write operation at this address is possible only after system boot.
	#       Table 55: Interrupt mode:
	#         AOI    6D        Interrupt mode
	#         0       0        OR combination of interrupt events
	#         0       1        6-direction movement recognition
	#         1       0        AND combination of interrupt events
	#         1       1        6-direction position recognition
	#         Difference between AOI-6D = ‘01’ and AOI-6D = ‘11’.
	#         AOI-6D = ‘01’ is movement recognition. An interrupt is generated when the orientation moves from an 
	#         unknown zone to known zone. The interrupt signal remains for a duration ODR.
	#         AOI-6D = ‘11’ is direction recognition. An interrupt is generated when the orientation is inside a 
	#         known zone. The interrupt signal remains until the orientation is inside the zone. 
	#     
	
	
	def setINT1_CFG(self, val):
		"""Set register INT1_CFG"""
		self.write(REG.INT1_CFG, val, 8)
	
	def getINT1_CFG(self):
		"""Get register INT1_CFG"""
		return self.read(REG.INT1_CFG, 8)
	
	# Bits AOI
	# And/Or combination of Interrupt events. 
	#           Refer to Table 55: Interrupt mode 
	
	# Bits DIR_6D
	# 6 direction detection function enabled. 
	#           Refer to Table 55: Interrupt mode 
	
	# Bits ZHIE
	# Enable interrupt generation on Z high event or on Direction recognition. 
	# Bits ZLIE
	# Enable interrupt generation on Z low event or on Direction recognition. 
	# Bits YHIE
	# Enable interrupt generation on Y high event or on Direction recognition. 
	# Bits YLIE
	# Enable interrupt generation on Y low event or on Direction recognition. 
	# Bits XHIE
	# Enable interrupt generation on X high event or on Direction recognition. 
	# Bits XLIE
	# Enable interrupt generation on X low event or on Direction recognition. 
	# Register INT1_SRC
	# 8.22 
	#       Interrupt 1 source register. Read-only register.
	#       Reading at this address clears the INT1_SRC (31h) IA bit (and the interrupt signal on the INT 1 pin) 
	#       and allows the refresh of data in INT1_SRC (31h) if the latched option was chosen. 
	
	
	def setINT1_SRC(self, val):
		"""Set register INT1_SRC"""
		self.write(REG.INT1_SRC, val, 8)
	
	def getINT1_SRC(self):
		"""Get register INT1_SRC"""
		return self.read(REG.INT1_SRC, 8)
	
	# Bits unused_0
	# Bits IA
	# Interrupt active. 
	# Bits ZH
	# Z high. 
	# Bits ZL
	# Z low. 
	# Bits YH
	# Y high. 
	# Bits YL
	# Y low. 
	# Bits XH
	# X high. 
	# Bits XL
	# X low. 
	# Register INT1_THS
	# Interrupt 1 threshold. 
	
	def setINT1_THS(self, val):
		"""Set register INT1_THS"""
		self.write(REG.INT1_THS, val, 8)
	
	def getINT1_THS(self):
		"""Get register INT1_THS"""
		return self.read(REG.INT1_THS, 8)
	
	# Bits unused_0
	# Bits THS
	# 1 LSb = 16 mg @ FS = ±2 g
	#           1 LSb = 32 mg @ FS = ±4 g
	#           1 LSb = 62 mg @ FS = ±8 g
	#           1 LSb = 186 mg @ FS = ±16 g 
	
	# Register INT1_DURATION
	# 8.24 
	#       The D[6:0] bits set the minimum duration of the Interrupt 2 event to be recognized. Duration
	#       steps and maximum values depend on the ODR chosen.
	#       Duration time is measured in N/ODR, where N is the content of the duration register. 
	
	
	def setINT1_DURATION(self, val):
		"""Set register INT1_DURATION"""
		self.write(REG.INT1_DURATION, val, 8)
	
	def getINT1_DURATION(self):
		"""Get register INT1_DURATION"""
		return self.read(REG.INT1_DURATION, 8)
	
	# Bits unused_0
	# Bits D
	# Duration value. 
	#           1 LSb = 1/ODR 
	
	# Register INT2_CFG
	# 8.25 
	#       Content of this register is loaded at boot. 
	#       Write operation at this address is possible only after system boot.
	#       Table 64: Interrupt mode:
	#         AOI           6D        Interrupt mode
	#         0              0        OR combination of interrupt events
	#         0              1        6-direction movement recognition
	#         1              0        AND combination of interrupt events
	#         1              1        6-direction position recognition
	#         Difference between AOI-6D = ‘01’ and AOI-6D = ‘11’.
	#         AOI-6D = ‘01’ is movement recognition. An interrupt is generated when the orientation moves from an 
	#         unknown zone to known zone. The interrupt signal remains for a duration ODR.
	#         AOI-6D = ‘11’ is direction recognition. An interrupt is generated when the orientation is inside a 
	#         known zone. The interrupt signal remains until the orientation is inside the zone. 
	#     
	
	
	def setINT2_CFG(self, val):
		"""Set register INT2_CFG"""
		self.write(REG.INT2_CFG, val, 8)
	
	def getINT2_CFG(self):
		"""Get register INT2_CFG"""
		return self.read(REG.INT2_CFG, 8)
	
	# Bits AOI
	# And/Or combination of Interrupt events. 
	#           Refer to Table 64: Interrupt mode 
	
	# Bits DIR_6D
	# 6 direction detection function enabled. 
	#           Refer to Table 64: Interrupt mode 
	
	# Bits ZHIE
	# Enable interrupt generation on Z high event or on Direction recognition. 
	# Bits ZLIE
	# Enable interrupt generation on Z low event or on Direction recognition. 
	# Bits YHIE
	# Enable interrupt generation on Y high event or on Direction recognition. 
	# Bits YLIE
	# Enable interrupt generation on Y low event or on Direction recognition. 
	# Bits XHIE
	# Enable interrupt generation on X high event or on Direction recognition. 
	# Bits XLIE
	# Enable interrupt generation on X low event or on Direction recognition. 
	# Register INT2_SRC
	# 8.26 
	#       Interrupt 2 source register. Read-only register.
	#       Reading at this address clears the INT1_SRC (31h) IA bit (and the interrupt signal on the INT 1 pin) 
	#       and allows the refresh of data in INT1_SRC (31h) if the latched option was chosen. 
	
	
	def setINT2_SRC(self, val):
		"""Set register INT2_SRC"""
		self.write(REG.INT2_SRC, val, 8)
	
	def getINT2_SRC(self):
		"""Get register INT2_SRC"""
		return self.read(REG.INT2_SRC, 8)
	
	# Bits unused_0
	# Bits IA
	# Interrupt active. 
	# Bits ZH
	# Z high. 
	# Bits ZL
	# Z low. 
	# Bits YH
	# Y high. 
	# Bits YL
	# Y low. 
	# Bits XH
	# X high. 
	# Bits XL
	# X low. 
	# Register INT2_THS
	# 8.27
	#       Interrupt 2 threshold. 
	
	
	def setINT2_THS(self, val):
		"""Set register INT2_THS"""
		self.write(REG.INT2_THS, val, 8)
	
	def getINT2_THS(self):
		"""Get register INT2_THS"""
		return self.read(REG.INT2_THS, 8)
	
	# Bits unused_0
	# Bits THS
	# 1 LSb = 16 mg @ FS = ±2 g
	#           1 LSb = 32 mg @ FS = ±4 g
	#           1 LSb = 62 mg @ FS = ±8 g
	#           1 LSb = 186 mg @ FS = ±16 g 
	
	# Register INT2_DURATION
	# 8.28
	#       The D[6:0] bits set the minimum duration of the Interrupt 2 event to be recognized. Duration
	#       steps and maximum values depend on the ODR chosen.
	#       Duration time is measured in N/ODR, where N is the content of the duration register. 
	
	
	def setINT2_DURATION(self, val):
		"""Set register INT2_DURATION"""
		self.write(REG.INT2_DURATION, val, 8)
	
	def getINT2_DURATION(self):
		"""Get register INT2_DURATION"""
		return self.read(REG.INT2_DURATION, 8)
	
	# Bits unused_0
	# Bits D
	# Duration value. 
	#           1 LSb = 1/ODR 
	
	# Register CLICK_CFG
	# 8.29 
	
	def setCLICK_CFG(self, val):
		"""Set register CLICK_CFG"""
		self.write(REG.CLICK_CFG, val, 8)
	
	def getCLICK_CFG(self):
		"""Get register CLICK_CFG"""
		return self.read(REG.CLICK_CFG, 8)
	
	# Bits unused_0
	# Bits ZD
	# Enable interrupt double click on Z-axis. 
	# Bits ZS
	# Enable interrupt single click on Z-axis. 
	# Bits YD
	# Enable interrupt double click on Y-axis. 
	# Bits YS
	# Enable interrupt single click on Y-axis. 
	# Bits XD
	# Enable interrupt double click on X-axis. 
	# Bits XS
	# Enable interrupt single click on X-axis. 
	# Register CLICK_SRC
	# 8.30 
	
	def setCLICK_SRC(self, val):
		"""Set register CLICK_SRC"""
		self.write(REG.CLICK_SRC, val, 8)
	
	def getCLICK_SRC(self):
		"""Get register CLICK_SRC"""
		return self.read(REG.CLICK_SRC, 8)
	
	# Bits unused_0
	# Bits IA
	# Interrupt active. 
	# Bits DCLICK
	# Double-click enable. 
	# Bits SCLICK
	# Single-click enable. 
	# Bits Sign
	# Click sign. 
	# Bits Z
	# Z click detection. 
	# Bits Y
	# Y click detection. 
	# Bits X
	# X click detection. 
	# Register CLICK_THS
	# 8.31 
	
	def setCLICK_THS(self, val):
		"""Set register CLICK_THS"""
		self.write(REG.CLICK_THS, val, 8)
	
	def getCLICK_THS(self):
		"""Get register CLICK_THS"""
		return self.read(REG.CLICK_THS, 8)
	
	# Bits LIR_Click
	# If the LIR_Click bit is not set, the interrupt is kept high for the duration of the latency window. 
	#           If the LIR_Click bit is set, the interrupt is kept high until the CLICK_SRC (39h) register is read. 
	
	# Bits Ths
	# Click threshold. 
	# Register TIME_LIMIT
	# 8.32 
	
	def setTIME_LIMIT(self, val):
		"""Set register TIME_LIMIT"""
		self.write(REG.TIME_LIMIT, val, 8)
	
	def getTIME_LIMIT(self):
		"""Get register TIME_LIMIT"""
		return self.read(REG.TIME_LIMIT, 8)
	
	# Bits unused_0
	# Bits TLI
	# Click time limit. 
	# Register TIME_LATENCY
	# 8.33 
	#       Click time latency. 
	
	
	def setTIME_LATENCY(self, val):
		"""Set register TIME_LATENCY"""
		self.write(REG.TIME_LATENCY, val, 8)
	
	def getTIME_LATENCY(self):
		"""Get register TIME_LATENCY"""
		return self.read(REG.TIME_LATENCY, 8)
	
	# Bits TIME_LATENCY
	# Register TIME_WINDOW
	# 8.34
	#       Click time window 
	
	
	def setTIME_WINDOW(self, val):
		"""Set register TIME_WINDOW"""
		self.write(REG.TIME_WINDOW, val, 8)
	
	def getTIME_WINDOW(self):
		"""Get register TIME_WINDOW"""
		return self.read(REG.TIME_WINDOW, 8)
	
	# Bits TIME_WINDOW
	# Register ACT_THS
	# 8.35 
	
	def setACT_THS(self, val):
		"""Set register ACT_THS"""
		self.write(REG.ACT_THS, val, 8)
	
	def getACT_THS(self):
		"""Get register ACT_THS"""
		return self.read(REG.ACT_THS, 8)
	
	# Bits unused_0
	# Bits Acth
	# Sleep-to-wake, return-to-sleep activation threshold in low-power mode 
	#         1 LSb = 16 mg @ FS = ±2 g
	#         1 LSb = 32 mg @ FS = ±4 g
	#         1 LSb = 62 mg @ FS = ±8 g
	#         1 LSb = 186 mg @ FS = ±16 g 
	
