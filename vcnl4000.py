# Example sketch for talking to the VCNL4000 i2c proximity/light sensor
# Written by Adafruit! Public domain.
# To use: Connect VCC to 3.3-5V (5V is best if it is available), GND to
#         ground, SCL to i2c clock (on classic arduinos, Analog 5), SDA
#         to i2c data (on classic arduinos Analog 4). The 3.3v pin is
#         an ouptut if you need 3.3V
# This sensor is 5V compliant so you can use it with 3.3 or 5V micros

# You can pick one up at the Adafruit shop: www.adafruit.com/products/466

from Adafruit_I2C import Adafruit_I2C
import time

class VCNL4000():
  # the i2c address
  VCNL4000_ADDRESS = 0x13

  # commands and constants
  VCNL4000_COMMAND = 0x80
  VCNL4000_PRODUCTID = 0x81
  VCNL4000_IRLED = 0x83
  VCNL4000_AMBIENTPARAMETER = 0x84
  VCNL4000_AMBIENTDATA = 0x85
  VCNL4000_PROXIMITYDATA = 0x87
  VCNL4000_SIGNALFREQ = 0x89
  VCNL4000_PROXIMITYADJUST = 0x8A

  VCNL4000_3M125 = 0
  VCNL4000_1M5625 = 1
  VCNL4000_781K25 = 2
  VCNL4000_390K625 = 3

  VCNL4000_MEASUREAMBIENT = 0x10
  VCNL4000_MEASUREPROXIMITY = 0x08
  VCNL4000_AMBIENTREADY = 0x40
  VCNL4000_PROXIMITYREADY = 0x20

  def __init__(self, *args, **kwargs):
    i2c = Adafruit_I2C(0x77)
    rev = i2c.readU8(self.VCNL4000_PRODUCTID)
    if((rev & 0xF0) != 0x10):
      print 'Sensor not found wtf'

    i2c.write8(self.VCNL4000_IRLED, 10) # set to 10 * 10mA = 100mA
    current = i2c.readU8(self.VCNL4000_IRLED)
    print 'we think current is set to ', current
    sigFreq = i2c.read8(self.VCNL4000_SIGNALFREQ)
    print 'we think sigFreq is ',sigFreq
    i2c.write8(self.VCNL4000_PROXIMITYADJUST, 0x81)
    proxAdj = i2c.readU8(self.VCNL4000_PROXIMITYADJUST)
    print 'we think proximityAdjust is ',proxAdj

  def readProximity():
    i2c.write8(self.VCNL4000_COMMAND, self.VCNL4000_MEASUREPROXIMITY)
    while True:
      result = i2c.readU8(self.VCNL4000_COMMAND)
      if(result & self.VCNL4000_PROXIMITYREADY):
        return i2c.readU16(self.VCNL4000_PROXIMITYDATA)
      time.sleep(0.001)

  def readAmbient():
    i2c.write8(self.VCNL4000_COMMAND, self.VCNL4000_MEASUREPROXIMITY)
    while True:
      result = i2c.readU8(self.VCNL4000_COMMAND)
      if(result & self.VCNL4000_AMBIENTREADY):
        return i2c.readU16(self.VCNL4000_AMBIENTDATA)
      time.sleep(0.001)


  ########################################################################
# void setup() {
#   Serial.begin(9600);

#   Serial.println("self.VCNL");
#   Wire.begin();

#   uint8_t rev = read8(VCNL4000_PRODUCTID);
  
#   if ((rev & 0xF0) != 0x10) {
#     Serial.println("Sensor not found :(");
#     while (1);
#   }
    
  
#   write8(VCNL4000_IRLED, 20);        # set to 20 * 10mA = 200mA
#   Serial.print("IR LED current = ");
#   Serial.print(read8(VCNL4000_IRLED) * 10, DEC);
#   Serial.println(" mA");
  
#   #write8(VCNL4000_SIGNALFREQ, 3);
#   Serial.print("Proximity measurement frequency = ");
#   uint8_t freq = read8(VCNL4000_SIGNALFREQ);
#   if (freq == VCNL4000_3M125) Serial.println("3.125 MHz");
#   if (freq == VCNL4000_1M5625) Serial.println("1.5625 MHz");
#   if (freq == VCNL4000_781K25) Serial.println("781.25 KHz");
#   if (freq == VCNL4000_390K625) Serial.println("390.625 KHz");
  
#   write8(VCNL4000_PROXIMITYADJUST, 0x81);
#   Serial.print("Proximity adjustment register = ");
#   Serial.println(read8(VCNL4000_PROXIMITYADJUST), HEX);
  
#   # arrange for continuous conversion
#   #write8(VCNL4000_AMBIENTPARAMETER, 0x89);

# }

# uint16_t readProximity() {
#   write8(VCNL4000_COMMAND, VCNL4000_MEASUREPROXIMITY);
#   while (1) {
#     uint8_t result = read8(VCNL4000_COMMAND);
#     #Serial.print("Ready = 0x"); Serial.println(result, HEX);
#     if (result & VCNL4000_PROXIMITYREADY) {
#       return read16(VCNL4000_PROXIMITYDATA);
#     }
#     delay(1);
#   }
# }



# void loop() {

#   # read ambient light!
#   write8(VCNL4000_COMMAND, VCNL4000_MEASUREAMBIENT | VCNL4000_MEASUREPROXIMITY);
  
#   while (1) {
#     uint8_t result = read8(VCNL4000_COMMAND);
#     #Serial.print("Ready = 0x"); Serial.println(result, HEX);
#     if ((result & VCNL4000_AMBIENTREADY)&&(result & VCNL4000_PROXIMITYREADY)) {

#       Serial.print("Ambient = ");
#       Serial.print(read16(VCNL4000_AMBIENTDATA));
#       Serial.print("\t\tProximity = ");
#       Serial.println(read16(VCNL4000_PROXIMITYDATA));
#       break;
#     }
#     delay(10);
#   }
  
#    delay(100);
#  }

# # Read 1 byte from the VCNL4000 at 'address'
# uint8_t read8(uint8_t address)
# {
#   uint8_t data;

#   Wire.beginTransmission(VCNL4000_ADDRESS);
# #if ARDUINO >= 100
#   Wire.write(address);
# #else
#   Wire.send(address);
# #endif
#   Wire.endTransmission();

#   delayMicroseconds(170);  # delay required

#   Wire.requestFrom(VCNL4000_ADDRESS, 1);
#   while(!Wire.available());

# #if ARDUINO >= 100
#   return Wire.read();
# #else
#   return Wire.receive();
# #endif
# }


# # Read 2 byte from the VCNL4000 at 'address'
# uint16_t read16(uint8_t address)
# {
#   uint16_t data;

#   Wire.beginTransmission(VCNL4000_ADDRESS);
# #if ARDUINO >= 100
#   Wire.write(address);
# #else
#   Wire.send(address);
# #endif
#   Wire.endTransmission();

#   Wire.requestFrom(VCNL4000_ADDRESS, 2);
#   while(!Wire.available());
# #if ARDUINO >= 100
#   data = Wire.read();
#   data <<= 8;
#   while(!Wire.available());
#   data |= Wire.read();
# #else
#   data = Wire.receive();
#   data <<= 8;
#   while(!Wire.available());
#   data |= Wire.receive();
# #endif
  
#   return data;
# }

# # write 1 byte
# void write8(uint8_t address, uint8_t data)
# {
#   Wire.beginTransmission(VCNL4000_ADDRESS);
# #if ARDUINO >= 100
#   Wire.write(address);
#   Wire.write(data);  
# #else
#   Wire.send(address);
#   Wire.send(data);  
# #endif
#   Wire.endTransmission();
# }