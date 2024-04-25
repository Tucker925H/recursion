#include <Wire.h>
#include "KX122.h"

KX122 KX122(KX122_DEVICE_ADDRESS_1F);

void setup() {
  Serial.begin(115200);
  while (!Serial);
  Wire.begin();

  if (KX122.init() != 0) {
    Serial.println("KX122 initialization failed");
    Serial.flush();
  }
}

void loop() {
  float acc[3];
  if (KX122.get_val(acc) == 0) {
    Serial.print(acc[0]);
    Serial.print(",");
    Serial.print(acc[1]);
    Serial.print(",");
    Serial.println(acc[2]);
  }
  delay(500);
}
