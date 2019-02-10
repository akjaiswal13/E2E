from parking import ParkingLot
import argparse, os


parking_action = {
    'create_parking_lot': ParkingLot.create_parking_lot,
    'park': ParkingLot.park,
    'status': ParkingLot.status,
    'leave': ParkingLot.leave,
    'registration_numbers_for_cars_with_colour': ParkingLot.registration_numbers_for_cars_with_colour,
    'slot_numbers_for_cars_with_colour': ParkingLot.slot_numbers_for_cars_with_colour,
    'slot_number_for_registration_number': ParkingLot.slot_number_for_registration_number,
    'exit': ParkingLot.exit
}


def main():
    cmd = ParkingLot.parking_menu().strip()
    action = cmd.split()

    if not action:
        os.system('clear')
        main()

    try:
        os.system('clear')
        action = action[0]
        result = parking_action.get(action, ParkingLot.input_error)(cmd)
        if result:
            print '-------------------------------------- Result -------------------------------------'
            print result
            print '-----------------------------------------------------------------------------------\n'

        if action != 'exit':
            main()

    except Exception as e:
        print str(e)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', default=None)
    args = parser.parse_args()
    file_name = args.file_name

    if file_name:
        try:
            with open(file_name) as file:
                for cmd in file.readlines():
                    action = cmd.split()
                    if action:
                        action = action[0]
                        result = parking_action.get(action, ParkingLot.input_error)(cmd)
                        print result

        except IOError as e:
            print "File not found"

        except Exception as e:
            print str(e)

    else:
        main()

