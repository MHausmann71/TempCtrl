# main script for the temperature controller
from Tools import fsm
from Tools.check_platform.check_platform import is_raspberry_pi
from dataclasses import dataclass

if not is_raspberry_pi():
    # on Windows or other platforms, use the periphery_sim module to simulate GPIO with RotarySwitchSim.txt config
    # set the environment variable PERIPHERY_SIM_CONFIG to the path of the simulation config file if not already set
    # import os
    # os.environ.setdefault("PERIPHERY_SIM_CONFIG", "E:/python_local/TempCtrl/sim_config/tempctrl.txt")
    # from PeripherySim.periphery_sim import GPIO
    from DisplayLibrary.tools.window_display_backend import WindowDisplayBackend
    print(f"WindowDisplayBackend module loaded.")
else:
    from periphery import GPIO


@dataclass(frozen=False)
class TempSense:
    # holds the temperature sensor configuration settings and state
    id: int | None = None  # oneWire device id
    name: str | None = None  # sensor name
    temperature: float | None = None  # current temperature reading
    error: str | None = None  # error message if any
    th_normal: float | None = None  # normal-mode temperature threshold
    th_reduced: float | None = None  # reduced-mode temperature threshold
    th_freeze: float | None = None  # freeze-mode temperature threshold
    thyst: float = 1.0  # hysteresis value for temperature control


if __name__ == '__main__':
    t = TempSense(id=1, name="Sensor1", temperature=25.0, th_normal=30.0, th_reduced=20.0, th_freeze=10.0)
    print(t)