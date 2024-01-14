# Fridge Controller

This project contains code for controlling the temperature inside a refrigerator. The main goal is to maintain the temperature inside the refrigerator at a programmed level, regardless of the outside temperature. The innovation is the use of outside temperature for energy savings. We are just waiting for the invention of a technical solution that controls access to cold air from outside the building ;).

## Code Structure

The code consists of three main classes:

1. `Observer`: This is the base class for observers. Observers are notified of changes in the refrigerator's temperature and can react to them.

2. `FridgeTemperatureObserver`: This is a specific observer class that monitors the temperature inside the refrigerator. If the temperature inside the refrigerator differs from the programmed temperature, the observer calls the `adjust_temp()` method of the refrigerator to adjust the temperature.

3. `Fridge`: This is a class representing the refrigerator. It contains information about the current temperature inside the refrigerator, the outside temperature, and the programmed temperature. This class also manages a list of observers and informs them about temperature changes.

## Assumptions

1. The temperature inside the refrigerator is initially set to a certain value and can be changed by the influence of the outside temperature.

2. We can program the expected temperature inside the refrigerator. If the actual temperature inside the refrigerator differs from the programmed temperature, the system will try to adjust the temperature inside the refrigerator.

3. The system controls the temperature inside the refrigerator by turning the fan on and off and opening and closing the ventilation hole.

## How to Run

To run this code, you need to have Python 3 installed. Then you can run the `fridge controller 2.py` script using the `python fridge controller 2.py` command in the terminal.

## License

This project is available under the MIT license.
