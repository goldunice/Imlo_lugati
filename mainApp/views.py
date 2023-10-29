from django.shortcuts import render, redirect
from .models import *


def result(request):
    x = ''
    t = ''
    n = ''
    qidirish_sozi = request.GET.get("searched")
    if qidirish_sozi:
        togrisi = Togri.objects.filter(t_soz=qidirish_sozi)
        if togrisi:
            t = togrisi[0]
            n = Notogri.objects.filter(t_id=t)
        else:
            n = Notogri.objects.filter(n_soz=qidirish_sozi)
            if n:
                t = n[0].t_id
                n = Notogri.objects.filter(t_id=t)
            else:
                x = "So'z omborda yo'q!!!"

    else:
        x = ''
    content = {
        "togri": t,
        "notogrilar": n,
        "not_found": x
    }
    return render(request, 'result.html', content)
