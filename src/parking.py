import argparse
import os


class ParkingLot(object):
    """
    ParkingLot is utility for maintaing parking
    System
    """
    parking_lot = {}

    def __init__(self):
        super(ParkingLot, self).__init__()
        self.total_parking_lot = n

    @staticmethod
    def parking_menu(*args, **kwargs):
        print "==================================================================================="
        print "Parking Lot: Enter your choice"
        print "==================================================================================="
        print "1. Create Parking Lot:", ParkingLot.create_parking_lot.__doc__
        print "2. Park:", ParkingLot.park.__doc__
        print "3. Leave:", ParkingLot.leave.__doc__
        print "4. Status:", ParkingLot.status.__doc__
        print "5. Registration Numbers For Cars With Colour:", ParkingLot.registration_numbers_for_cars_with_colour.__doc__
        print "6. Slot Numbers For Cars With Colour:", ParkingLot.slot_numbers_for_cars_with_colour.__doc__
        print "7. Slot Number For Registration Number:", ParkingLot.slot_number_for_registration_number.__doc__
        print "8. Exit:", ParkingLot.exit.__doc__
        print "==================================================================================="
        choice = raw_input("Enter Command$ ")

        return choice

    @classmethod
    def create_parking_lot(cls, cmd, *args, **kwargs):
        """
        Cmd Help: create_parking_lot <slots>
        """
        token = cmd.split()
        if len(token) == 2:
            n = int(token[1])
            for x in range(1, n + 1):
                cls.parking_lot.update({x: {}})

            return "Created a parking lot with {} slots".format(n)

        else:
            return "Invalid input"

    @classmethod
    def status(cls, cmd, *args, **kwargs):
        """
        Cmd Help: status
        """
        result = 'Slot No\tRegistration No\tColour\n'

        for key, val in cls.parking_lot.items():
            result += '{}\t{}\t{}\n'.format(key, val.get('reg_no', ''), val.get('color', ''))

        return result

    @classmethod
    def park(cls, cmd, *args, **kwargs):
        """
        Cmd Help: park <Reg_no> <color>
        """
        token = cmd.split()
        if len(token) == 3:
            for key, val in cls.parking_lot.items():
                if not val:
                    datalist = {}
                    datalist['reg_no'] = token[1]
                    datalist['color'] = token[2].upper()
                    cls.parking_lot.update({key: datalist})
                    return 'Allocated slot number: {}'.format(key)

            else:
                return "Sorry, parking lot is full"

        else:
            return "Invalid input"

    @classmethod
    def leave(cls, cmd, *args, **kwargs):
        """
        Cmd Help: leave <slot no>
        """
        token = cmd.split()
        if len(token) == 2:
            slot = int(token[1])
            if cls.parking_lot.has_key(slot):
                cls.parking_lot.get(slot).clear()
                return 'Slot number {} is free'.format(slot)

        else:
            return "Invalid input"

    @classmethod
    def registration_numbers_for_cars_with_colour(cls, cmd, *args, **kwargs):
        """
        Cmd Help: registration_numbers_for_cars_with_colour <color>
        """
        token = cmd.split()
        if len(token) == 2:
            color = token[1].upper()
            data = []
            for key, val in cls.parking_lot.items():
                if val.get('color') == color:
                    data.append(val.get('reg_no'))

            return ', '.join(data) if data else 'Not found'

        else:
            return "Invalid input"

    @classmethod
    def slot_numbers_for_cars_with_colour(cls, cmd, *args, **kwargs):
        """
        Cmd Help: slot_numbers_for_cars_with_colour <color>
        """
        token = cmd.split()
        if len(token) == 2:
            color = token[1].upper()
            data = []
            for key, val in cls.parking_lot.items():
                if val.get('color') == color:
                    data.append(key)

            return ', '.join(map(str, data)) if data else 'Not found'

        else:
            return "Invalid input"

    @classmethod
    def slot_number_for_registration_number(cls, cmd, *args, **kwargs):
        """
        Cmd Help: slot_number_for_registration_number <reg_no>
        """
        token = cmd.split()
        if len(token) == 2:
            reg_no = token[1].upper()
            data = []
            for key, val in cls.parking_lot.items():
                if val.get('reg_no') == reg_no:
                    data.append(key)

            return ', '.join(map(str, data)) if data else 'Not found'

        else:
            return "Invalid input"

    @classmethod
    def exit(cls, cmd, *args, **kwargs):
        """
        Cmd Help: exit
        """
        if cmd == 'exit':
            return

    @classmethod
    def input_error(cls, cmd, *args, **kwargs):
        return "No command found"


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

