#Toll fine calculation script
#Author: Luke O'Keeffe

FINE_DAY = 3.15 #Fine for violations 7AM-7PM
FINE_OFFPEAK = 1.65 #Fine for 4:30-7AM and 7PM-midnight
FINE_CUTOFF = 60 #Cut-off for fines to display


def list_toll_dodgers(tfile):
    """
      Reads a file of vehicle data and prints vehicles with fines over the cutoff.
      Applies fine rules according to time of day and date.
      No fines are applied for entries on the first of the month or between midnight and 4:30AM.

      :paramater tfile: Path to the vehicle data file
      :return: None
      :print: Vehicles with fine over the cutoff
      """
    with open(tfile, "r") as file:
        car_data = file.readlines()

    car_data = [item.strip() for item in car_data]

    split_data = []
    for item in car_data:
     split_data.append(item.split())

    fines_dictionary = {}

    # Iterates through separated items and breaks them down to their individual components
    for item in split_data:
        fine = 0 #Default case is no fine
        hour = int(item[2][0:2])
        minute = int(item[2][3:5])
        day = item[1][1:4]
        plate = item[0]
        if day != "/1/":
            if hour >= 7 and hour < 19:
                fine += FINE_DAY
            else:
                if hour == 4 and minute <= 30:
                    pass
                elif hour < 4:
                    pass
                else:
                    fine += FINE_OFFPEAK
        if plate not in fines_dictionary:
            fines_dictionary[plate] = fine
        else:
            # Increases fine amount on plate listed before
            fines_dictionary[plate] += fine

    # Sorts dictionary entries by fines in descending order, lists those greater than cut-off
    for plate, fine in sorted(fines_dictionary.items(), key = lambda x: x[1], reverse = True):
        if fine >= FINE_CUTOFF:
            print(f'Car with the license plate: {plate}, was found to have accrued fines totalling {fine:.2f}')
