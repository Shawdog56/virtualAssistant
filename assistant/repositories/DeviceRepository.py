from assistant.models import EntDevice

class DeviceRepository:
    @staticmethod
    def get_by_id(device_id:int) -> EntDevice:
        return EntDevice.objects.filter(id=device_id).first()
    
    @staticmethod
    def list_all():
        return EntDevice.objects.all()