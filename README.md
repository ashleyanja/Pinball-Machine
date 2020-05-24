# Pinball-Machine
With a team of four, designed and developed a Pinball Machine for a Digital Systems class. Our pinball machine was created using photocell sensors, a piezo buzzer, a Basys3 board (pushbuttons and seven segment display), as well as a multitude of wires. The base project for the Basys3 was provided by the professor, which only required modifications to one c file (which is included under the Basys 3 Code folder). The main objective of our project was to create an interactive object that showcased the ability of a simple logic function while creating an enjoyable experience for the user. There were many different segments used when building our contraption; we incorporated direct user input to trigger the sensors and run the machine, while the sensors and boards process the signals and direct the information to the website, keeping a real time score as the user interacts with the machine. When the user scores, (the ball rolls over one of the three point photocell sensors), the signal is sent to the Basys3 and from there through the raspberry pi to update the current score on the website. If the ball triggers the reset photocell, it resets the user’s current score to zero. The user’s previous score is saved and outputted back to the Basys3. At this point, the user can press the pushbutton on the Basys3 to display their previous score. 

Video Demo: https://youtu.be/Z0wf63qdtys 
