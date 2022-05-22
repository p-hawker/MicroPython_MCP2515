
from machine import SPI

spi = SPI(0, baudrate=1000000,
             polarity=0,
             phase=0,
             bits=8,
             firstbit=SPI.MSB,
             sck=pin(18),
             mosi=pin(19),
             miso=pin(16))


def readCanRegister(Address, spiInterface):
    #Reads specified data from the address inputed
    txData = bytearray[3]
    txData[0] = 0b00000011 #Read command
    txData[1] = Address #Address to read from

    rxData = bytearray[len(txData)] #Recived data on last index

    spiInterface.write_readinto(txData, rxData) #Communicate data on spi

    return(rxData[2]) #Returns single byte from the address inputed

def resetCanControler(spiInterface):
    #Send command to reset can controller
    txData = bytearray[1]
    txData[0] = 0b11000000 #Reset command

    spiInterface.write(txData) #send command and return

def readCanReciveReg(AddressSelect: int, spiInterface):
    #Reads recive buffers from can controller
    Command
    if AddressSelect == 0:
       Command = 0b10010000 #command read from RXB0SIDH
    elif AddressSelect == 1:
        Command = 0b10010010 #command read from RXB0D0
    elif AddressSelect == 2:
        Command = 0b10010100 #commanf read from RXB1SIDH
    elif AddressSelect == 3:
        Command = 0b10010110  #command read from RXB1D0
    else:
        Command = 0b10010000 #Standard command is to read RXB0SIDH

    txData = bytearray[2] 
    txData[0] = Command #Load command

    rxData = bytearray[len(txData)] #load recive message

    spiInterface.write_readinto(txData,rxData) #Communicate on SPI

    return(rxData[1]) #Return the last byte recived

def writeCanRegister(Address, Data, spiInterface):
    #writes a byte to a registers address

    txData = bytearray[3]
    txData[0] = 0b00000010 #Write command
    txData[1] = Address #Addres to write to
    txData[2] = Data #Data writen

    spiInterface.write(txData) #Communicate on SPI

def  writeCanTXRegister(AddressSelect:int, Data, spiInterface):
    #Writes to one of the transmit registers

    Command
    if AddressSelect == 0:
        Command = 0b01000000 #TX Buffer 0, Start at TXB0SIDH
    elif AddressSelect == 1:
        Command = 0b01000001 #TX Buffer 0, Start at TXB0D0
    elif AddressSelect == 2:
        Command = 0b01000010 #TX Buffer 1, Start at TXB1SIDH
    elif AddressSelect == 3:
        Command = 0b01000011 #TX Buffer 1, Start at TXB1D0
    elif AddressSelect == 4:
        Command = 0b01000100 #TX Buffer 2, Start at TXB2SIDH
    elif AddressSelect == 5:
        Command = 0b01000101 #TX Buffer 2, Start at TXB2D0
    else:
        Command = 0b01000000

    txData = bytearray[2]
    txData[0] = Command #set command
    txData[1] = Data #set the data to be sent

    spiInterface.write(txData) #send data and return

def WriteCanReqToSend(RegisterNumber: int, spiInterface):
    #Writes command to send the data on the can bus

    Command
    if RegisterNumber == 0: #Request to send buffer 0
        Command = 0b10000001
    elif RegisterNumber == 1: #Request to send buffer 1
        Command = 0b10000010
    elif RegisterNumber == 2: #Request to send buffer 2
        Command = 0b10000100
    else:
        Command = 0b10000001 #Default buffer 1

    txData = bytearray[1] 
    txData[0] = Command #Set command

    spiInterface.write(txData) #Write to the SPI

def ReadCanStatus(spiInterface):

    txData = bytearray[2]
    txData[0] = 0b10100000 #Read status command

    rxData = bytearray[len(txData)] #set input buffer

    spiInterface.write_readinto(txData, rxData) #Communicate data on spi

    return(rxData[1]) #Return last bit of recived data

def ReadCanReciveStatus(spiInterface):

    txData = bytearray[2]
    txData[0] = 0b10110000 #Read recive status

    rxData = bytearray[len(txData)] #set recive buffer

    spiInterface.write_readinto(txData,rxData) #Communicate data on spi 

    return(rxData[1])  #Return last bit of recived data

def CheckCanMsgSent(StatusByte, Register: int):
    #Checks if the registers number can msg successfull bit is set
    #Bits in status Byte:
    #0:RX0IF #1:RX1IF #2:TXREQ #3:TX0IF
    #4:TXREQ #5:TX1IF #6:TXREQ #7:TX2IF
    if (Register > 2 or Register < 0):
        return 0
    Test
    if (Register == 0):
        Test = 0b00001000
    elif (Register == 1):
        Test = 0b00100000
    elif (Register == 2):
        Test = 0b10000000
    
    return(StatusByte & Test)

def CheckIfMsgRecived(StatusByte):
    #Checks if either recive buffer bits are set
    return(StatusByte & 0b00000001 or StatusByte & 0b00000010)






