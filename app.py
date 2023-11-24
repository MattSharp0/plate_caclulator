import logging
from fastapi import FastAPI, Query
from starlette import status
from typing import Annotated, Union

from fastapi.responses import RedirectResponse

from plate_calculator import Plate_Calculator

logging.basicConfig(format='%(levelname)s: %(asctime)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)
log = logging.getLogger(__name__)

app = FastAPI()
log.info('App intiated')

imperial:dict = {'bars':[45,35],'plates':[45,35,25,15,10,5,2.5,1.25]}
metric:dict = {'bars':[20,16],'plates':[20, 16, 11, 7, 5, 2, 1, .5]}

@app.get('/')
def root():
    return RedirectResponse(url='/docs', status_code=status.HTTP_302_FOUND)


@app.get('/plate_calculator')
def return_weight_options(system:Union[str, None]=None):

    match system:
        case 'imperial':
            return {'default imperial':imperial}
        case 'metric':
            return {'default metric': metric}
        case _:
            return {'default imperial':imperial, 'metric':metric}

@app.get('/plate_calculator/{target_weight}')
def calculate_plates(target_weight: int,
                    metric_or_imperial:Union[str, None] = None,
                    exclude_plates:Annotated[list[float],Query()] = [],
                    bar_weight:Union[int, None] = None):

    plates = []
    bar = 0
    log.debug(f'plates passed: {exclude_plates}')
    log.debug(f'API called - target_weight: {target_weight}, metric_or_imperial: {metric_or_imperial}, exclude_plates: {exclude_plates}, bar_weight: {bar_weight}')
    match metric_or_imperial:
        case 'imperial':
            plates = imperial['plates']
            bar:int = imperial['bars'][0]
        case 'metric':
            plates = metric['plates']
            bar = metric['bars'][0]
        case _:
            plates = imperial['plates']
            bar = imperial['bars'][0]

    if exclude_plates:
        log.debug(f'Excluding plate options: {exclude_plates}')
        plates = list(set(plates)-set(exclude_plates))
        plates.sort(reverse=True)

    log.debug(f'Plates used: {plates}')

    if bar_weight:
        log.debug(f'Using query bar weight: {bar_weight}')
        bar = bar_weight

    try: 
        plate_calculation = Plate_Calculator(target_weight,plates=plates, bar=bar)
    except ValueError as e:
        return {'error':f'Value Error: {e}'}
    return {'plate_calculation': plate_calculation, 'plate_options':plates,'bar_weight':bar}