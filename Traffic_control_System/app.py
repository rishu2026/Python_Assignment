from Signals.city_signal import CitySignal
from Signals.highway_signal import HighwaySignal
from Controllers.controller import SignalController
from app_logger import logger

logger.info(f"Traffic Simulation Started...")


controller=SignalController()
no_vehicle=int(input("Enter number of vehicle"))

city_signal=CitySignal(no_vehicle)
highway_signal= HighwaySignal(no_vehicle)

controller.operate(city_signal)
controller.operate(highway_signal)
logger.info("Simulation completed")