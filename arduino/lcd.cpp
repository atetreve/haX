
// include the library code:
#include <LiquidCrystal.h>
int analogPin = A0;
int buttonPin = 7;
int Vin = 5;
float comp;
float rl = 0.23 - 0.05;
float ru = 0.23 + 0.05;

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

float measure(int analogPin) {
  int raw = 0;
  int Vout = 0;
  float b = 0;
  raw = analogRead(analogPin);
  if(raw) {
    b= raw * Vin;
    Vout= (b)/1024.0;
    return Vout;
  }
}


int ButtonIsPressed(int buttonPin){
  pinMode(buttonPin, INPUT);
  int buttonState = digitalRead(buttonPin);
  if (buttonState == LOW) {
    return true; 
  } else {
      return false;
  }
}


void setup() {
  // set up the LCD's number of columns and rows:
  Serial.begin(9600);
  Serial.println("Starting.");
  Serial.println(rl);
  Serial.println(ru);
  //lcd.begin(16, 2);
}
void test(){
  comp = measure(analogPin);
  Serial.println(comp);

}
void loop() {
  Serial.println("loop");
  test();
}

 
