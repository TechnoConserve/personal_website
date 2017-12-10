from django.shortcuts import render


def sensor(request):
    return render(request, "sensor/sensor-display.html", {
        'sensor': '99',
    })
