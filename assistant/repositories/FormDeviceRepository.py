from assistant.models import CatDeviceType, CatUbicationDeviceType

class FormDeviceRepository:
    @staticmethod
    def get_device_info():
        # .values() creates a list of dictionaries with field names as keys
        return {
            "types": list(CatDeviceType.objects.all().values('id', 'name')),
            "ubications": list(CatUbicationDeviceType.objects.all().values('id', 'name'))
        }