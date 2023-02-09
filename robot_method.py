# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 21:12:47 2022

@author: stefa
"""
import os
from pyhamilton import (HamiltonInterface,  LayoutManager, 
 Plate96, Tip96, initialize, tip_pick_up, tip_eject, 
 aspirate, dispense,  oemerr, resource_list_with_prefix, normal_logging,
 hhs_create_star_device)

from pyhamilton import(hhs_begin_monitoring, hhs_create_star_device, hhs_create_usb_device,
            hhs_end_monitoring, hhs_get_firmware_version, hhs_get_serial_num, hhs_get_shaker_param,
            hhs_get_shaker_speed, hhs_get_temp_param, hhs_get_temp, hhs_get_temp_state, hhs_send_firmware_cmd,
            hhs_set_plate_lock, hhs_stop_all_shakers, hhs_set_shaker_param, 
            hhs_set_simulation, hhs_set_temp_param, hhs_set_usb_trace, hhs_start_all_shaker,
            hhs_start_all_shaker_timed, hhs_start_shaker, hhs_start_shaker_timed, hhs_start_temp_ctrl,
            hhs_stop_shaker, hhs_stop_temp_ctrl, hhs_terminate, hhs_wait_for_shaker, hhs_wait_for_temp_ctrl)



lmgr = LayoutManager('deck.lay')
plates = resource_list_with_prefix(lmgr, 'plate_', Plate96, 5)
tips = resource_list_with_prefix(lmgr, 'tips_', Tip96, 1)
liq_class = 'StandardVolumeFilter_Water_DispenseJet_Empty'

aspiration_poss = [(plates[0], x) for x in range(8)]
dispense_poss = [(plates[0], x) for x in range(8,16)]
vols_list = [100]*8


tips_poss = [(tips[0], x) for x in range(8)]


if __name__ == '__main__': 
    with HamiltonInterface(simulate=True) as ham_int:
        normal_logging(ham_int, os.getcwd())
        initialize(ham_int)
        
        device_num = hhs_create_star_device(ham_int, used_node=1)
        device_num2 = hhs_create_star_device(ham_int, used_node=2)

        device_num=1
        
        hhs_begin_monitoring(ham_int, device_num, 10, 5, 0)
        
        monitor_result = hhs_end_monitoring(ham_int, device_number=device_num)
        print("Monitor result: ", monitor_result)

        firmware_STAR = hhs_get_firmware_version(ham_int, device_number=device_num)
        print("Firmware Version: ", firmware_STAR)

        serial_STAR = hhs_get_serial_num(ham_int, device_number=device_num)
        print("Serial Num:", serial_STAR)

        shaker_param_STAR = hhs_get_shaker_param(ham_int, device_num)
        print("Shaker Parameters: ", shaker_param_STAR)

        shaker_speed_STAR = hhs_get_shaker_speed(ham_int, device_num)
        print("Shaker speed: ", shaker_speed_STAR)


        temp_param_STAR = hhs_get_temp_param(ham_int, device_num)
        print("Temp parameters: ", temp_param_STAR)

        temp_STAR = hhs_get_temp(ham_int, device_num)
        print("Temperature: ", temp_STAR)

        temp_state_STAR = hhs_get_temp_state(ham_int, device_num)
        print("Temperature state: ", temp_state_STAR)

        # hhs_send_firmware_cmd(ham_int, device_num, '', 'shakingSpeed')

        hhs_set_plate_lock(ham_int, device_num, 1)

        hhs_set_shaker_param(ham_int, device_num, 1, 8000)

        hhs_set_simulation(ham_int, 1)

        hhs_set_temp_param(ham_int, device_num, 10, 5, 5)

        hhs_set_usb_trace(ham_int, 1)

        # hhs_start_all_shaker(ham_int, 500)

        # hhs_start_all_shaker_timed(ham_int, 500, 5)

        hhs_start_shaker(ham_int, device_num, 500)

        hhs_start_shaker_timed(ham_int, device_num, 500, 5)

        hhs_start_temp_ctrl(ham_int, device_num, 50, 0)

        # hhs_stop_all_shakers(ham_int)

        hhs_stop_shaker(ham_int, device_num)

        hhs_stop_temp_ctrl(ham_int, device_num)

        # hhs_terminate(ham_int)

        hhs_wait_for_shaker(ham_int, device_num)

        hhs_wait_for_temp_ctrl(ham_int, device_num)

        hhs_terminate(ham_int)
