// include the library code:
#include <LiquidCrystal.h>

const int sensorPower = 7;
const int sensorPin = A0;
int moisture = 0;

// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);

  pinMode(A0, OUTPUT);
  pinMode(A1, INPUT);
}

void loop() {
  lcd.clear();
  // Apply power to the soil moisture sensor
  digitalWrite(A0, HIGH);
  delay(10); // Wait for 10 millisecond(s)
  moisture = analogRead(A1);
  // Turn off the sensor to reduce metal corrosion
  // over time
  digitalWrite(A0, LOW);
  if (moisture < 200) {
    lcd.write("Ho tanta sete");
    delay(2000);
  } else {
    if (moisture < 400) {
    	lcd.write("Ho sete");
      	delay(2000);
    } else {
      if (moisture < 600) {
    	lcd.write("Ho un po di sete");
        delay(2000);
      } else {
        if (moisture < 800) {
    		lcd.write("Sto bene!");
          	delay(2000);
        } else {
    		lcd.write("TROPPA ACQUA!");
          	delay(2000);
        }
      }
    }
  }
}
 