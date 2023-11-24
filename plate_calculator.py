import logging as log


def Plate_Calculator(target_weight:int, plates:list, bar:int = 45) -> dict:

    if target_weight < bar:
        log.warning(f'Target weight ({target_weight}) is less than the bar ({bar})')
        raise ValueError(f'Target weight ({target_weight}) is less than the bar ({bar})')

    one_side_weight = (target_weight-bar)/2
    remaining_weight = one_side_weight*100
    log.debug(f'One side weight: {one_side_weight}')

    plate_assignments = {}

    for plate in plates:

        non_decimal_plate = plate*100

        log.debug(f'Plate: {non_decimal_plate}, remaining weight: {remaining_weight}')

        plate_count:int = remaining_weight//non_decimal_plate
        remainder:int = round(remaining_weight % non_decimal_plate,2)
        
        remaining_weight = remainder
        plate_assignments[plate] = int(plate_count*2)
        
        if remainder == 0:
            break
        
    plates_used = { plate_weight:count for plate_weight, count in plate_assignments.items() if count }
    total_weight = sum(k*v for k,v in plates_used.items())+bar

    return {'target_weight':target_weight,'bar_weight':bar, 'plates':plates_used,'total':total_weight,'remaining':target_weight-total_weight}


if __name__ == "__main__":
    log.basicConfig(format='%(levelname)s: %(asctime)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=log.DEBUG)

    # plates_lb:list = [45,35,25,15,10,5,2.5,1.25]
    plates_lb:list = [45,10,5]

    # print(calc_plates(target_weight=90, plates=plates_lb))
    # print(calc_plates(target_weight=135, plates=plates_lb))
    # print(calc_plates(target_weight=140, plates=plates_lb))
    # print(calc_plates(target_weight=180, plates=plates_lb))
    print(calc_plates(target_weight=185, plates=plates_lb))
    # print(calc_plates(target_weight=191, plates=plates_lb))
    # print(calc_plates(target_weight=195, plates=plates_lb))

    # try: 
    #     print(calc_plates(target_weight=35, plates=plates_lb))
    # except ValueError as e:
    #     print(e)