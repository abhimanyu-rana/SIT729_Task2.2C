#include <OneWire.h>
#include <DallasTemperature.h>

// Data wire is plugged into pin 2 on the Arduino
#define ONE_WIRE_BUS 2

// Setup a oneWire instance to communicate with any OneWire devices
OneWire oneWire(ONE_WIRE_BUS);

// Pass our oneWire reference to Dallas Temperature
DallasTemperature sensors(&oneWire);

void setup() {
  Serial.begin(9600);
  sensors.begin();
}

void loop() {
  sensors.requestTemperatures();  // Request temperature data
  
  // Read temperature in Celsius
  float temperatureC = sensors.getTempCByIndex(0);
  
  // Print temperature to Serial Monitor
  Serial.print("Temperature (Celsius): ");
  Serial.println(temperatureC);
  
  // Delay for a while before taking another reading (adjust as needed)
  delay(5000);  // 5-second interval between readings
}
