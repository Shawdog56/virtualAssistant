from django.shortcuts import render
from django.http import JsonResponse
from assistant.repositories.UserRepository import UserRepository
from assistant.repositories.DeviceRepository import DeviceRepository
from assistant.repositories.FormDeviceRepository import FormDeviceRepository

# Create your views here.
def user_details(request, id):
    try:
        user = UserRepository.get_by_id(id)
        data = {
            "success": True,
            "id": user.id,
            "username": user.username
        }
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({
            "success": False,
            "message": "User not found"
        })
    

def device_all(request):
    try:
        all_devices = DeviceRepository.list_all()
        data = {
            "success": True,
            "devices": all_devices
        }
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({
            "success": False,
            "message": "Not Devices Found"
        })
    

def form_info(request):
    try:
        return JsonResponse(FormDeviceRepository.get_device_info())
    except Exception as e:
        return JsonResponse({
            "success": False,
            "message": "Error while fetching information"
        })
