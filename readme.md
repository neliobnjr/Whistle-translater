# Whistle Translater

This project is a fun experiment that translates a whistle sound from a laptop's microphone into a tone that can be played on an Arduino buzzer. It uses Python to listen to the microphone, extract the whistle's frequency using Fast Fourier Transform (FFT), and send the frequency information to the Arduino over a serial connection. The Arduino then generates the corresponding tone on the buzzer.

## Requirements

- Python 3.7 or higher
- PyAudio
- NumPy
- Matplotlib
- pyserial
- Arduino IDE
- Arduino board and buzzer

## Installation

1. Clone this repository: `git clone https://github.com/neliobnjr/whistle-translater.git`
2. Change into the project directory: `cd whistle-translater`
3. Install the required Python packages: `pip install -r requirements.txt`
4. Open `whistle_translater.ino` in the Arduino IDE and upload it to your Arduino board.
5. Connect the buzzer to the Arduino board as described in the `whistle_translater.ino` file.
6. Run `python app.py` to start the Python script.

## Usage

1. Launch the Python script by running `python app.py`.
2. Whistle into the microphone, making sure the sound is clear and strong.
3. The script will output the detected frequency of the whistle in Hz and play the corresponding tone on the buzzer.

## Credits

This project was created by neliobnjr as a fun experiment with Python and Arduino. The code is based on examples from the PyAudio and pyserial libraries.

## License

This project is licensed under the [MIT License](LICENSE).
