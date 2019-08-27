import smbus
import time
import numpy as np
import matplotlib.pyplot as plt
import obspy
from obspy import Stream, Trace

print ' '
print 'All Sensors DLVR sensor read-out'
print ' '
print 'Olivier den Ouden'
print 'Royal Netherlands Meteorological Institute'
print 'Aug. 2019'
print ' '

sensor = smbus.SMBus(1)
addr = 0x28

stats = {'network':'MB','station':'Al','npts':6000,'mseed':{'dataquality':'D'}}

i=0
pressure = np.zeros((6000))
while i<6000:
	if i==0:
		start = obspy.UTCDateTime()
		stats['starttime']=start
	data = [0,0,0,0]
	data = sensor.read_i2c_block_data(addr,0,4)
	databits = (data[0] & 0x3F)
	rawdata = (databits<<8) +z[1]
	rawpress = int(rawdata)
	pressure[i] = (((rawpress-8192.0)/16384.0)*497.68)
	print 'P:',pressure[i],'Pa'
	time.sleep(0.01)
	i = i+1
	if i ==5999:
		end = obspy.UTCDateTime()
		stats['endtime']=end
st = Stream([Trace(data=pressure[:],header=stats)])
st.write("test.mseed",format="MSEED")
plt.plot(pressure)
#plt.show()
