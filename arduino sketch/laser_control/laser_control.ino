
int laserPin ;
char userInput;
boolean switchLaser;

void setup() {
  Serial.begin(9600);
  switchLaser = false;
  laserPin = 6;
  pinMode(laserPin, OUTPUT);
  
  
}

void loop() {
   
  if(Serial.available()>0){
    
    userInput = Serial.read();
    
    if(userInput == 'l'){
      
      if(switchLaser == false){
        
        switchLaser = true;
      }
      
      else{
        switchLaser = false;
      laserCommand();
      }
      
    }
    
   
  }
}

void laserCommand(){
  
    if(switchLaser==true){
      digitalWrite(laserPin, HIGH);
      
       }
    else{
      digitalWrite(laserPin, LOW);
    }  
}
