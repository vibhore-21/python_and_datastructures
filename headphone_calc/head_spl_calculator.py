__author__ = 'Vibhore'
"""
This program gives the sound pressure level of your head phones at a given volume setting of your device.
Disclaimer: This is not a accurate way of measuring and will only give you a ballpark estimate at your
actual listening levels.
The best way to get the actual number would to get a dummy head and an SPL meter (kind of expensive).
No commercial purpose, just for python lovers.

The formula is based on the
Reference http://www.head-fi.org/t/586490/approximating-headphone-volume-output-db
"""

from math import log

def calculate_spl(Sensitivity, Impedance, MaxOutputVoltage, VolumeLevelFraction):
    # voltage provided by the device at the given volume setting
    Voltage = MaxOutputVoltage * (VolumeLevelFraction ** 2)
    Current = (Voltage * 2)/Impedance
    Power = Current * Voltage
    # SPL in Pa
    SPL_PA = Sensitivity * Power
    # SPL in db
    SPL_DB0 = 20 * log(SPL_PA / (2*10**-5), 10)

    # OR
    # SPL_dB = 20 * log(Sensitivity * Power / (2 * 10 ** -5))
    # SPL_dB = 20 * log(Sensitivity * (Voltage * 2 / Impedance) * Voltage / (2 * 10 ** -5))
    # SPL_DB = 20 * log((Sensitivity * (MaxOutputVoltage * VolumeLevelFraction ** 2) ** 2) / (Impedance * 10**-5), 10)
    print "Pressure level will be : ", SPL_DB0
    # if SPL_DB0 != SPL_DB0:
    #     print SPL_DB

    return SPL_DB0

if __name__ == '__main__':

    Sensitivity = float(raw_input("Sensitivity rating of headphones in db (spl): "))
    Impedance = float(raw_input("Impedance rating of headphones in ohms: "))
    MaxOutputVoltage = float(raw_input("Max output voltage of your device(ipod/notebook) in volts: "))
    VolumeLevelFraction = float(raw_input("fraction of volume setting, u are using on your device (<=1) ,"
                                          "\n 1 means full volume , 0.5 is half, so on : "))

    calculate_spl(Sensitivity, Impedance, MaxOutputVoltage, VolumeLevelFraction)
