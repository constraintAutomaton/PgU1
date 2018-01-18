
int laserPin ;
char userInput;


void setup() {
  Serial.begin(9600);
  laserPin = 7;
  pinMode(laserPin, OUTPUT);
  
  
}

void loop() {
   
  if(Serial.available()>0){
    
    userInput = Serial.read();
    
   switch(userInput){
     case 'l':
       laserOn();
       break;
     case 'g':
       laserOff();
       break;
       
    
   
    }
  }
}

void laserOn(){
  digitalWrite(laserPin, HIGH);
      
}

void laserOff(){
  digitalWrite(laserPin, LOW);
}
