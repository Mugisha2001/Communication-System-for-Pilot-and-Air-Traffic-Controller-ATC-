import pyaudio
import numpy as np
import scipy.signal
import matplotlib.pyplot as plt
import time

# Constants for the communication system
SAMPLE_RATE = 44100  # Audio sample rate (for voice communication)
CHANNELS = 1  # Mono audio
FORMAT = pyaudio.paInt16  # Audio format
CHUNK_SIZE = 1024  # Number of frames per buffer
ERROR_THRESHOLD = 0.1  # Threshold for error detection (basic checksum comparison)

# Function to record pilot's voice (simulated communication)
def record_pilot_voice(duration=5):
    p = pyaudio.PyAudio()
    print("Recording pilot's voice...")
    stream = p.open(format=FORMAT, channels=CHANNELS,
                    rate=SAMPLE_RATE, input=True,
                    frames_per_buffer=CHUNK_SIZE)
    
    frames = []
    for _ in range(0, int(SAMPLE_RATE / CHUNK_SIZE * duration)):
        data = stream.read(CHUNK_SIZE)
        frames.append(data)

    print("Recording completed.")
    stream.stop_stream()
    stream.close()
    p.terminate()

    audio_data = b''.join(frames)
    return audio_data

# Function to simulate transmission of voice (send and receive)
def transmit_voice(audio_data):
    print("Simulating voice transmission...")
    # Simulate some error in transmission (for demonstration)
    error_simulation = np.random.random()
    if error_simulation > ERROR_THRESHOLD:
        print("Transmission successful.")
        return audio_data  # Data received correctly
    else:
        print("Error in transmission. Data corrupted.")
        return None  # Simulating corrupted data

# Function to simulate telemetry data (altitude, speed, etc.)
def generate_telemetry_data():
    altitude = np.random.uniform(3000, 10000)  # Altitude in feet
    speed = np.random.uniform(200, 600)  # Speed in knots
    telemetry_data = {
        'altitude': altitude,
        'speed': speed
    }
    return telemetry_data

# Function to simulate the transmission of telemetry data
def transmit_telemetry(telemetry_data):
    print("Simulating telemetry transmission...")
    error_simulation = np.random.random()
    if error_simulation > ERROR_THRESHOLD:
        print("Telemetry data transmitted successfully.")
        return telemetry_data  # Data received correctly
    else:
        print("Error in telemetry transmission. Data corrupted.")
        return None  # Simulating corrupted data

# Function to display received data at ATC (for both voice and telemetry)
def display_atc_data(received_voice, received_telemetry):
    print("\nATC Display:")
    if received_voice is not None:
        print("Received voice message from pilot: Transmission successful.")
    else:
        print("Error in receiving voice message.")

    if received_telemetry is not None:
        print(f"Received telemetry data - Altitude: {received_telemetry['altitude']} feet, Speed: {received_telemetry['speed']} knots.")
    else:
        print("Error in receiving telemetry data.")

# Function to plot the telemetry data (altitude and speed over time)
def plot_telemetry_data(altitudes, speeds, time_intervals):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    # Plotting altitude
    ax1.plot(time_intervals, altitudes, label='Altitude (feet)', color='blue')
    ax1.set_xlabel('Time (seconds)')
    ax1.set_ylabel('Altitude (feet)')
    ax1.set_title('Altitude Over Time')
    ax1.grid(True)

    # Plotting speed
    ax2.plot(time_intervals, speeds, label='Speed (knots)', color='red')
    ax2.set_xlabel('Time (seconds)')
    ax2.set_ylabel('Speed (knots)')
    ax2.set_title('Speed Over Time')
    ax2.grid(True)

    plt.tight_layout()
    plt.show()

# Main communication system simulation
def communication_system():
    # Record and transmit pilot's voice
    pilot_voice_data = record_pilot_voice(duration=3)  # Record 3 seconds of voice
    transmitted_voice = transmit_voice(pilot_voice_data)
    
    # Simulate telemetry data generation and transmission
    telemetry_data = generate_telemetry_data()
    transmitted_telemetry = transmit_telemetry(telemetry_data)

    # ATC receives and displays data
    display_atc_data(transmitted_voice, transmitted_telemetry)

    # If telemetry data is transmitted successfully, plot the data
    if transmitted_telemetry:
        altitudes = [transmitted_telemetry['altitude'] for _ in range(10)]  # Simulate constant altitude over time
        speeds = [transmitted_telemetry['speed'] for _ in range(10)]  # Simulate constant speed over time
        time_intervals = np.arange(10)  # Simulate 10 seconds intervals
        
        plot_telemetry_data(altitudes, speeds, time_intervals)

# Running the communication system
if __name__ == "__main__":
    communication_system()
