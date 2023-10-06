import serial
import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Establish a serial connection with the Arduino
ser = serial.Serial('COMX', 9600)  # Replace 'COMX' with your Arduino's port

# Create or open a CSV file for data storage
csv_file = open('temperature_data.csv', 'a', newline='')
csv_writer = csv.writer(csv_file)

# Initialize Google Sheets API credentials
scope = ['https://www.googleapis.com/auth/spreadsheets']
creds = ServiceAccountCredentials.from_json_keyfile_name('your-credentials.json', scope)
client = gspread.authorize(creds)

# Open the Google Sheets document
sheet = client.open('Temperature Data').sheet1  # Replace with your Google Sheets document name

try:
    while True:
        # Read data from Arduino
        arduino_data = ser.readline().decode('utf-8').strip()
        if arduino_data:
            # Split data into timestamp and temperature
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            temperature = float(arduino_data)

            # Write data to CSV
            csv_writer.writerow([timestamp, temperature])
            csv_file.flush()

            # Write data to Google Sheets
            sheet.append_row([timestamp, temperature])

except KeyboardInterrupt:
    csv_file.close()
    ser.close()
