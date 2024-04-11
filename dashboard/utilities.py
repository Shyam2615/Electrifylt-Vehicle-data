import csv
from datetime import datetime
from .models import VehicleData


def import_data_from_csv(file_path):
    
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            license_plate, make, vin, model, type_, date_str,miles_driven   = row
            
            # Convert the date string to a Python datetime object
            date = datetime.strptime(date_str, '%d-%m-%Y').date()
            
            data_object = VehicleData.objects.create(
                LicensePlate=license_plate,
                Make=make,
                VIN=vin,
                Model=model,
                Type=type_,
                date_str=date,
                MilesDriven=miles_driven
            )
            data_object.save()


import_data_from_csv('C:\\Users\\syb26\\Desktop\\ElectrifyIt\\Vehicle_data\\core\\data.csv')
print("Done")
