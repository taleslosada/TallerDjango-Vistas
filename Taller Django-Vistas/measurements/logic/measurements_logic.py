from ..models import Measurement
from variables.models import Variable

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(mea_pk):
    measurement = Measurement.objects.get(pk=mea_pk)
    return measurement

def update_measurement(mea_pk, new_mea):
    measurement = get_measurement(mea_pk)
    measurement.unit = new_mea["unit"]
    measurement.value = new_mea["value"]
    measurement.dateTime = new_mea["dateTime"]
    measurement.place = new_mea["place"]
    measurement.variable = Variable.objects.get(pk=new_mea["variable"]['pk'])
    measurement.save()
    return measurement

def create_measurement(mea):
    measurement = Measurement(
        unit=mea["unit"],
        value=mea["value"],
        place=mea["place"],
        variable= Variable.objects.get(pk=mea["variable"]["pk"]),
        dateTime=mea["dateTime"]
    )
    measurement.save()
    return measurement

def delete_measurement(mea_pk):
    measurements = get_measurement(mea_pk)
    measurements.delete()