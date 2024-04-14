import re
from datetime import datetime


def current_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def transform_values(dict):
    new_dict = {}
    new_dict['output_volt'] = float(dict['output_volt'].split(' ')[0])
    new_dict['output_frequency_hz'] = float(dict['output_frequency'].split(' ')[0])
    new_dict['output_load_percent'] = float(dict['output_load_(%)'].split(' ')[0])
    new_dict['output_load_amp'] = float(dict['output_load_(a)'].split(' ')[0])
    new_dict['output_load_watt'] = float(dict['output_load_(w)'].split(' ')[0])
    new_dict['output_load_va'] = float(dict['output_load_(va)'].split(' ')[0])
    
    new_dict['pv_volt'] = float(dict['pv_volt'].split(' ')[0])
    new_dict['pv_watt'] = float(dict['pv_watt'].split(' ')[0])
    new_dict['pv_amp'] = float(dict['pv_amp'].split(' ')[0])
    new_dict['pv_efficiency'] = float(dict['pv_efficiency'].split(' ')[0])

    new_dict['battery_volt'] = float(dict['battery_volt'].split(' ')[0])
    new_dict['battery_status_percent'] = float(dict['battery_status'].split(' ')[0])
    new_dict['battery_charging_amp'] = float(dict['battery_charging'].split(' ')[0])
    new_dict['battery_discharging_amp'] = float(dict['battery_discharging'].split(' ')[0])

    new_dict['inverter_mode'] = dict['inverter_mode']
    new_dict['inverter_temperature'] = float(dict['inverter_temperature'].split(' ')[0])
    
    return new_dict

