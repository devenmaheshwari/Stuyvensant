#pragma config(Sensor, dgtl1,  farin,          sensorSONAR_cm)
#pragma config(Sensor, dgtl3,  closein,        sensorSONAR_cm)
#pragma config(Motor,  port1,           conveyer,      tmotorVex393_HBridge, openLoop, reversed)
#pragma config(Motor,  port10,          drop,          tmotorVex393_HBridge, openLoop)
//*!!Code automatically generated by 'ROBOTC' configuration wizard               !!*//

task main()
{
	if (SensorValue(farin) < 10) {
		startMotor(conveyer, -20); //check motor direction for conveyer
	}

	bool go = true;

	// Main Loop
  while (true) {
  	if (SensorValue(farin) < 10 & go) {
			startMotor(conveyer, -20); //check motor direction for conveyer
		}

	  if (SensorValue(closein) < 5 & go) {
	  	stopMotor(conveyer);
	  	wait(2);
	  	startMotor(drop, 64);
	  	wait(1);
	  	startMotor(drop, -20);
	  	wait(0.5);
	  	stopMotor(drop);
	  	wait(2);
	  	go = false;
	}
		if (!go){
			startMotor(conveyer, 20);
			wait(3.5);
			stopMotor(conveyer);
			wait(10);
			go = true;
		}


}






}
