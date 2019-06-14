# -------------------------------------------------------------------------------------------------------------------
# This class is used for data transmission over serial. It is instantiated with port name as a parameter (this one   |
# used for serial transmission). In main loop of this program this class receives prepared values of EB/N0 corresponding
# to each transponder and basing on these data prepares output string that needs to be send over serial.             |
# -------------------------------------------------------------------------------------------------------------------
import serial
import logging
# ---------------------------------------------------------------------------------------------------------------------
# Constructor receives parameters of serial transmission. In case of port unavailability (wrong port was chosen, or    |
# other software problems) it returns information that problem has occured and then transmission is not available.     |
# ---------------------------------------------------------------------------------------------------------------------

class SerialTransmission(object):
    def __init__(self, port):
        try:
            self.s = serial.Serial(port=port,
                                   baudrate=9600,
                                   parity=serial.PARITY_NONE,
                                   stopbits=serial.STOPBITS_ONE,
                                   bytesize=serial.EIGHTBITS,
                                   timeout=None)
        except serial.SerialException:
            logging.error("Couldn't open this port - it probably doesn't exist")

    def set_output_text(self, transponder_number, margin):
        try:
            if margin < 10.0:
                if margin % 1 == 0:
                    text = str.encode(']>{}/EBN0_0{}.0dB\r\n'.format(transponder_number, margin))
                else:
                    text = str.encode(']>{}/EBN0_0{}dB\r\n'.format(transponder_number, margin))
            else:
                if margin % 1 == 0:
                    text = str.encode(']>{}/EBN0_{}.0dB\r\n'.format(transponder_number, margin))
                else:
                    text = str.encode(']>{}/EBN0_{}dB\r\n'.format(transponder_number, margin))
            return text
        except TypeError:
            logging.error("No value to pass to output string")

    def send_data(self, number, value):
        margin = self.set_output_text(number, value)
        try:
            if margin is not None:
                self.s.write(margin)
            else:
                logging.error('There is no data to send over serial')
        except serial.SerialTimeoutException:
            logging.error("Sending over serial takes too long... closing port")
            self.s.close()

    def save_to_txt(self, file, text):
        with open(file, 'ab') as file:
            file.write(text)

    def clear_file_content(self, file):
        with open(file, 'w') as file:
            file.close()
