#include <Wire.h>
#include "KX122.h"

KX122 KX122(KX122_DEVICE_ADDRESS_1F);
bool send_data = false;

void setup() {
  Serial.begin(115200);
  Wire.begin();
  if (KX122.init() != 0) {
    Serial.println("KX122 initialization failed");
  }
}

void loop() {
  if (Serial.available() > 0) {
    int command = Serial.read();
    if (command == '1') {
      send_data = true;
    } else if (command == '0') {
      send_data = false;
    }
  }

  if (send_data) {
    float acc[3];
    if (KX122.get_val(acc) == 0) {
      Serial.print(acc[0]);
      Serial.print(",");
      Serial.print(acc[1]);
      Serial.print(",");
      Serial.println(acc[2]);
    }
    delay(100);
  }
}
