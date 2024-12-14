# Communication System for Pilot and Air Traffic Controller (ATC)

This Python-based communication system simulates the interaction between a pilot and an Air Traffic Controller (ATC) during the approach phase of an airplane landing.

## Core Functionalities

1. **Voice Communication**: Simulates the transmission of voice messages between the pilot and ATC.
2. **Telemetry Data Transmission**: Transmits random telemetry data (altitude and speed) from the aircraft to ATC.
3. **Graphical Visualization**: Visualizes telemetry data over time using `matplotlib`.
4. **Feedback from ATC**: Displays ATC feedback on data transmission success or errors.

## Dependencies

Ensure you have the following Python libraries installed to run the project:

- `pyaudio`: For recording and simulating voice communication.
- `numpy`: For numerical calculations and random simulations.
- `scipy`: For signal processing (if required).
- `matplotlib`: For plotting telemetry data graphs.

Install the necessary libraries using:
```bash
pip install pyaudio numpy scipy matplotlib
