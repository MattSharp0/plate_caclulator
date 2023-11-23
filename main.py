
plates_lb:list = [45,35,25,15,10,5,2.5,1.25]

def calc_plates(target_weight:int, bar:int = 45, plates:list = plates_lb) -> dict:

    if target_weight < bar:
        raise ValueError(f'Target weight ({target_weight}) is less than the bar ({bar})')

    one_side_weight = (target_weight-bar)/2
    
    plate_assignments = {'target_weight':target_weight,'bar_weight':bar}
    remaning = one_side_weight

    for plate in plates:
        plate_count:int = remaning//plate
        remainder:int = remaning % plate
        
        remaning = remainder
        plate_assignments[plate] = plate_count*2
        
        if remainder == 0:
            break

    return { k:v for k, v in plate_assignments.items() if v }


if __name__ == "__main__":
    print(calc_plates(target_weight=90))
    print(calc_plates(target_weight=135))
    print(calc_plates(target_weight=140))
    print(calc_plates(target_weight=180))
    print(calc_plates(target_weight=191))
    print(calc_plates(target_weight=195))
    print(calc_plates(target_weight=35))