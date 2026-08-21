# Digitization-of-the-Mathematical-Pendulum

A digital mathematical pendulum laboratory instrument based on **Arduino
Uno, E18-D80NK proximity sensor, I2C LCD, buzzer, push button, and
Python GUI** for automatically measuring pendulum oscillation and
estimating gravitational acceleration.

------------------------------------------------------------------------

## List of Content

-   [Introduction](#Introduction)
-   [Literature](#Literature)
    -   [Simple Harmonic Motion](#Simple-Harmonic-Motion)
    -   [Mathematical Pendulum](#Mathematical-Pendulum)
    -   [E18-D80NK Proximity Sensor](#E18-D80NK-Proximity-Sensor)
    -   [Arduino UNO](#Arduino-UNO)
    -   [Arduino IDE](#Arduino-IDE)
    -   [Python](#Python)
    -   [I2C LCD](#I2C-LCD)
    -   [Push Button](#Push-Button)
    -   [Buzzer](#Buzzer)
-   [Design](#Design)
    -   [Hardware Design](#Hardware-Design)
    -   [Software Design](#Software-Design)
    -   [System Workflow](#System-Workflow)
-   [Programs](#Programs)
    -   [Arduino Program](#Arduino-Program)
    -   [Python GUI](#Python-GUI)
-   [Installation](#Installation)
-   [Result](#Result)
    -   [System Testing](#System-Testing)
    -   [25 cm Pendulum Test](#25-cm-Pendulum-Test)
    -   [30 cm Pendulum Test](#30-cm-Pendulum-Test)
-   [Project Structure](#Project-Structure)
-   [Reference](#Reference)
-   [Conclusion](#Conclusion)

------------------------------------------------------------------------

## Introduction

A mathematical pendulum is one of the fundamental experiments in physics
for studying **simple harmonic motion** and determining gravitational
acceleration from the oscillation period.

Conventional pendulum experiments commonly use a stopwatch to measure
oscillation time. This method depends on the observer's reaction time
and can introduce measurement errors.

In this project, a **digital mathematical pendulum laboratory
instrument** is developed using an **Arduino UNO and Python**. An
**E18-D80NK infrared proximity sensor** is used to automatically detect
the pendulum's oscillation. The Arduino processes the detected
oscillations and calculates the pendulum period and gravitational
acceleration.

An **I2C LCD** provides local feedback, while a **buzzer** provides
audible feedback during the measurement process. A **push button** is
also included as a physical control input.

A Python-based graphical user interface (GUI) is used to enter the
pendulum length and number of periods and to display the measurement
results.

The main goal of this project is to reduce manual measurement errors and
provide a more interactive laboratory instrument for learning **simple
harmonic motion and gravitational acceleration**.

------------------------------------------------------------------------

## Literature

### Simple Harmonic Motion

```{=html}
<p align="center">
```
`<img src="images/simple_harmonic_motion.png" width="500">`{=html}
```{=html}
</p>
```
Simple Harmonic Motion (SHM) is an oscillatory motion in which the
restoring force is proportional to the displacement from the equilibrium
position.

A mathematical pendulum can approximate SHM when the oscillation angle
is sufficiently small. The oscillation period depends primarily on the
length of the pendulum and the gravitational acceleration.

------------------------------------------------------------------------

### Mathematical Pendulum

```{=html}
<p align="center">
```
`<img src="images/mathematical_pendulum.png" width="500">`{=html}
```{=html}
</p>
```
A mathematical pendulum consists of a mass suspended from a string that
is assumed to have negligible mass and length compared with the size of
the pendulum bob.

The theoretical period is:

``` text
T = 2π√(L/g)
```

where `T` is the period, `L` is the pendulum length, and `g` is
gravitational acceleration.

Rearranging gives:

``` text
g = 4π²L / T²
```

The implemented Arduino program uses:

``` cpp
g = (39.43 * set_panjang / 100) / T2;
```

where `39.43` represents the implemented `4π²` factor and the pendulum
length is converted from centimeters to meters.

------------------------------------------------------------------------

### E18-D80NK Proximity Sensor

```{=html}
<p align="center">
```
`<img src="images/e18_d80nk.jpg" width="400">`{=html}
```{=html}
</p>
```
The **E18-D80NK** is an infrared optical proximity sensor used to detect
objects without physical contact. Its detection distance can be adjusted
within its operating range.

In this project, the sensor is positioned near the pendulum's
oscillation path. When the pendulum passes through the detection area,
the sensor produces a digital signal that is processed by the Arduino.

The sensor output becomes **LOW when an object is detected**, allowing
the Arduino to automatically count pendulum oscillations.

------------------------------------------------------------------------

### Arduino UNO

```{=html}
<p align="center">
```
`<img src="images/arduino_uno.png" width="400">`{=html}
```{=html}
</p>
```
Arduino UNO is the main microcontroller used in this project. It
receives the signal from the E18-D80NK sensor, counts oscillations,
measures elapsed time, calculates the pendulum period, and determines
gravitational acceleration.

Arduino also communicates with the Python GUI through serial
communication at **9600 baud** and controls the I2C LCD and buzzer.

------------------------------------------------------------------------

### Arduino IDE

```{=html}
<p align="center">
```
`<img src="images/arduino_ide.png" width="500">`{=html}
```{=html}
</p>
```
Arduino IDE is used to develop and upload the C/C++ program to Arduino
UNO.

The program handles sensor input, oscillation counting, time
measurement, period calculation, gravitational acceleration calculation,
LCD display, buzzer feedback, and serial communication.

------------------------------------------------------------------------

### Python

```{=html}
<p align="center">
```
`<img src="images/python.png" width="400">`{=html}
```{=html}
</p>
```
Python is used to create the graphical user interface and communicate
with Arduino. The program accepts pendulum length and number of periods,
sends the parameters to Arduino, receives the measurement result, and
displays the result in a table.

The GUI uses **Tkinter**, while serial communication uses **PySerial**.

------------------------------------------------------------------------

### I2C LCD

```{=html}
<p align="center">
```
`<img src="images/lcd_i2c.png" width="400">`{=html}
```{=html}
</p>
```
The I2C LCD provides local information from Arduino. The implemented
program uses an I2C LCD with address `0x27` and a 16 × 2 display.

The LCD displays states such as:

``` text
BANDUL
MATEMATIS
```

and:

``` text
Proses
Menghitung...
```

------------------------------------------------------------------------

### Push Button

```{=html}
<p align="center">
```
`<img src="images/push_button.png" width="300">`{=html}
```{=html}
</p>
```
The push button is used as a physical control element for the
experiment. The system also provides a **Mulai** button through the
Python GUI for starting a measurement.

------------------------------------------------------------------------

### Buzzer

```{=html}
<p align="center">
```
`<img src="images/buzzer.png" width="300">`{=html}
```{=html}
</p>
```
The buzzer provides audible feedback. In the Arduino program, it is
activated briefly when a pendulum event is detected and when the
measurement process is completed.

------------------------------------------------------------------------

## Design

The system consists of **hardware design** and **software design**. The
hardware detects the pendulum oscillation and performs the measurement,
while the software provides the user interface and data communication.

### Hardware Design

```{=html}
<p align="center">
```
`<img src="images/schematic.png" width="1000">`{=html}
```{=html}
</p>
```
The hardware consists of Arduino UNO, E18-D80NK proximity sensor, 16 × 2
I2C LCD, buzzer, push button, mathematical pendulum, pendulum stand,
PCB, jumper wires, and power supply.

The E18-D80NK sensor is positioned near the pendulum's oscillation path
so that each passage through the detection region can be recorded.

The electronic circuit is placed inside a protective case, while the
pendulum mechanism is mounted on a stand to maintain stable oscillation.

### Hardware Components

  Component                          Quantity    Function
  -------------------------------- ------------- ----------------------------------
  **Arduino UNO**                        1       Main microcontroller
  **E18-D80NK Proximity Sensor**         1       Detects pendulum oscillation
  **I2C LCD 16×2**                       1       Displays measurement information
  **Buzzer**                             1       Provides audible feedback
  **Push Button**                        1       Physical control input
  **Pendulum**                           1       Experimental object
  **Pendulum Stand**                     1       Supports the pendulum
  **PCB**                                1       Mounts the electronic circuit
  **Jumper Wires**                  As required  Electrical connections

### Software Design

The software consists of two main programs:

``` text
Arduino UNO
    │
    ├── E18-D80NK Sensor
    ├── I2C LCD
    └── Buzzer
          │
          │ Serial Communication
          ▼
      Python GUI
```

Arduino performs timing and oscillation measurement, while Python
provides the user interface and displays the results.

The serial communication uses:

``` text
Baud Rate = 9600
```

### System Workflow

``` text
Start
  │
  ▼
Enter Pendulum Length
and Number of Periods
  │
  ▼
Python Sends Parameters
to Arduino
  │
  ▼
Arduino Starts Measurement
  │
  ▼
E18-D80NK Detects Pendulum
Oscillation
  │
  ▼
Count Oscillations
  │
  ▼
Measure Elapsed Time
  │
  ▼
Calculate Period (T)
  │
  ▼
Calculate Gravitational
Acceleration (g)
  │
  ▼
Send Result to Python
  │
  ▼
Display Result in GUI
  │
  ▼
Measurement Complete
```

------------------------------------------------------------------------

## Programs

The programming system is divided into **Arduino firmware** and **Python
graphical user interface**.

### Arduino Program

The Arduino program initializes the LCD, serial communication, buzzer,
and sensor:

``` cpp
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

#define alarm 11
#define sensor 2
```

The sensor uses an interrupt-capable pin:

``` cpp
attachInterrupt(
    digitalPinToInterrupt(sensor),
    hitungAyunan,
    FALLING
);
```

When the sensor detects the pendulum:

``` cpp
void hitungAyunan() {
    if (digitalRead(sensor) == LOW) {
        nilai++;
        alarmSingkat();
    }
}
```

Two detected transitions are counted as one complete oscillation:

``` cpp
while (jumlah < set_priode) {
    if (nilai >= 2) {
        jumlah++;
        nilai = 0;
    }

    nilai_waktu++;
    delay(1);
}
```

The elapsed time is converted to seconds and the period is calculated:

``` cpp
nilai_waktu /= 1000;
T = nilai_waktu / set_priode;
T2 = T * T;
```

Gravitational acceleration is then calculated:

``` cpp
g = (39.43 * set_panjang / 100) / T2;
```

The result is sent to Python in the format:

``` text
L=<length>,T=<period>,g=<gravity>
```

### Python GUI

The Python interface uses Tkinter and PySerial:

``` python
arduino = serial.Serial('COM3', 9600)
arduino.flush()
```

The user enters pendulum length and number of periods. The parameters
are sent to Arduino using:

``` python
arduino.write(f"{panjang},{periode}\n".encode())
```

The result is received using:

``` python
hasil = arduino.readline().decode().strip()
```

The GUI separates the returned data into pendulum length, period, and
gravitational acceleration and displays them in a table.

The interface contains **Mulai**, **Reset**, and **Keluar** controls.

------------------------------------------------------------------------

## Installation

### Hardware Requirements

-   Arduino UNO
-   E18-D80NK proximity sensor
-   16 × 2 I2C LCD
-   Buzzer
-   Push button
-   Mathematical pendulum
-   Pendulum stand
-   PCB
-   Jumper wires
-   Computer/laptop

### Software Requirements

-   Arduino IDE
-   Python 3
-   Tkinter
-   PySerial

### Arduino Libraries

Install:

``` text
LiquidCrystal_I2C
```

The program also uses the built-in `Wire` library for I2C communication.

### Python Libraries

Install PySerial:

``` bash
pip install pyserial
```

Tkinter is normally included with standard Python installations. On
Linux, it may need to be installed through the operating system package
manager.

------------------------------------------------------------------------

## Running the Program

### 1. Upload the Arduino Program

Open the Arduino source code in Arduino IDE, select **Arduino UNO**,
select the correct serial port, and upload the program.

### 2. Connect the Hardware

Connect the E18-D80NK sensor, I2C LCD, buzzer, and push button to
Arduino UNO according to the project schematic. Position the proximity
sensor near the pendulum's oscillation path.

### 3. Run the Python GUI

Run:

``` bash
python3 bandul_gui.py
```

Make sure the serial port matches the Arduino port:

``` python
arduino = serial.Serial('COM3', 9600)
```

Change `COM3` if another port is assigned.

### 4. Start a Measurement

Enter the pendulum length and number of periods, then press **Mulai**.
Arduino detects the oscillations, calculates the period and
gravitational acceleration, and returns the result to the Python GUI.

------------------------------------------------------------------------

## Result

### System Testing

Testing evaluated the ability of the digital pendulum kit to measure
oscillation and estimate gravitational acceleration. The sensor, LCD,
and control buttons were checked before measurement, and the E18-D80NK
was positioned below the pendulum's oscillation path.

Two pendulum lengths were tested:

-   **25 cm**
-   **30 cm**

Each configuration was measured **10 times** with 10 periods per
measurement. The results were compared with the standard gravitational
acceleration of **9.81 m/s²**.

### 25 cm Pendulum Test

```{=html}
<p align="center">
```
`<img src="images/test_25cm.png" width="800">`{=html}
```{=html}
</p>
```
      Trial       Gravitational Acceleration (m/s²)
  ------------- -----------------------------------
        1                                      9.82
        2                                      9.30
        3                                      9.50
        4                                      9.61
        5                                      9.75
        6                                      9.48
        7                                      9.54
        8                                      9.31
        9                                      9.27
       10                                      9.24
   **Average**                            **9.482**

The average was **9.482 m/s²**. Relative to 9.81 m/s², the difference is
approximately **3.34%**.

The report discusses possible causes including small variations in
pendulum length or initial position, air resistance, and sensor
detection conditions.

### 30 cm Pendulum Test

```{=html}
<p align="center">
```
`<img src="images/test_30cm.png" width="800">`{=html}
```{=html}
</p>
```
      Trial       Gravitational Acceleration (m/s²)
  ------------- -----------------------------------
        1                                     10.06
        2                                      9.81
        3                                     10.11
        4                                      9.35
        5                                     10.07
        6                                      9.60
        7                                     10.03
        8                                      9.85
        9                                      9.72
       10                                      9.54
   **Average**                            **9.814**

The average was **9.814 m/s²**. Relative to 9.81 m/s², the difference is
approximately **0.04%**.

The 30 cm configuration therefore produced a result much closer to the
standard gravitational acceleration. The report attributes the
improvement to greater pendulum stability at the longer string length,
which helps the proximity sensor detect oscillations more consistently.

### Comparison of Results

  -----------------------------------------------------------------------
    Pendulum Length    Average g (m/s²)       Standard g          Approx.
                                                  (m/s²)       Difference
  -------------------- ---------------- ---------------- ----------------
       **25 cm**                  9.482             9.81            3.34%

       **30 cm**                  9.814             9.81            0.04%
  -----------------------------------------------------------------------

The results show that the **30 cm configuration provided better
agreement with the standard gravitational acceleration**.

### Python Interface

```{=html}
<p align="center">
```
`<img src="images/python_interface.png" width="700">`{=html}
```{=html}
</p>
```
The Python GUI provides fields for pendulum length and number of periods
and displays pendulum length, period, and gravitational acceleration. It
also includes **Mulai, Reset, and Keluar** controls.

------------------------------------------------------------------------

## Project Structure

``` text
Digitalisasi-Alat-Praktikum-Bandul-Matematis/
│
├── README.md
│
├── code/
│   ├── bandul_arduino.ino
│   └── bandul_gui.py
│
├── images/
│   ├── simple_harmonic_motion.png
│   ├── mathematical_pendulum.png
│   ├── e18_d80nk.jpg
│   ├── arduino_uno.png
│   ├── arduino_ide.png
│   ├── python.png
│   ├── lcd_i2c.png
│   ├── push_button.png
│   ├── buzzer.png
│   ├── schematic.png
│   ├── python_interface.png
│   ├── test_25cm.png
│   └── test_30cm.png
│
└── LICENSE
```

------------------------------------------------------------------------

## Reference

This README is based on the project report **Digitalisasi Alat Praktikum
Fisika Dasar Bandul Matematis**. The report documents the hardware
design, Arduino and Python implementation, testing procedure, and
measurement results.

------------------------------------------------------------------------

## Conclusion

This project demonstrates a **digital mathematical pendulum laboratory
instrument based on Arduino and Python**.

The E18-D80NK proximity sensor detects pendulum oscillations
automatically, while Arduino performs timing and gravitational
acceleration calculations. The I2C LCD and buzzer provide local
feedback, while the Python Tkinter interface provides an interactive
method for entering experimental parameters and viewing measurement
results.

The experimental results show that the system can estimate gravitational
acceleration with good agreement with the standard value. The **25 cm**
configuration produced an average of **9.482 m/s²**, while the **30 cm**
configuration produced an average of **9.814 m/s²**. The 30 cm
configuration showed the closest agreement with the standard value of
**9.81 m/s²**.

The project can be further developed by adding automatic pendulum-length
adjustment and improving the Python interface with more interactive data
visualization.
