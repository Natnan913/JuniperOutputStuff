import serial
import time

intendedSerialPort= serial.Serial('COM3', 9600, timeout=1)
cliScreenLengthen = "set cli screen-length 0"
cliScreenRevert = "set cli screen-length 24"

def outputOfCommand(command):
    
    intendedSerialPort.write(command.encode() + b'\r\n') 
    time.sleep(2)
    output = intendedSerialPort.read(4096)   
    time.sleep(2)
    return output.decode(errors='ignore') # I'm not particularly worried about unicode errors - I've just asked decode() to not doing anything about them.
    

intendedSerialPort.write(cliScreenLengthen.encode() + b'\r\n')

###------------------These are the commands displaying all the output-----------------------------###

interfaceInfo = outputOfCommand("show interfaces terse")
print("Output of show interfaces terse:\n", interfaceInfo)
 
versionInfo = outputOfCommand('show version')
print("Output of show version:\n", versionInfo)

chassisEnvInfo = outputOfCommand('show chassis environment')
print("output of show chassis environment:\n", chassisEnvInfo)

chassisFirmwareInfo = outputOfCommand('show chassis firmware')
print("Output of show chassis firmware:\n", chassisFirmwareInfo)

chassisPicInfo = outputOfCommand('show chassis pic fpc-slot 0 pic-slot 0')
print("Output for pic info:\n", chassisPicInfo)

chassisPicInfoSlot1 = outputOfCommand('show chassis pic fpc-slot 0 pic-slot 1')
print("Output for pic info:\n", chassisPicInfoSlot1)

VirtualChassisInfo = outputOfCommand('show virtual-chassis status detail')
print("Output for virtual chassis stuff:\n", VirtualChassisInfo)

chassisHardwareInfo = outputOfCommand('show chassis hardware')
print("Output for chassis hardware:\n", chassisHardwareInfo)

###-------------------End of Output stuff----------------------------------###

intendedSerialPort.write(cliScreenRevert.encode() + b'\r\n') # I'm not really sure why, but I need to explicitly extend the max lines for the juniper CLI, unlike the Cisco script.


intendedSerialPort.close()



