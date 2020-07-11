from django.http import HttpResponse
from django.shortcuts import render
import pyautogui
import os
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def remote(request):
    if request.method == "POST":
        command = request.POST['command']
        if command == "play-pause":
            pyautogui.typewrite('space')
            return HttpResponse("SPACE Typed...")
        elif command == "volume-up":
            pyautogui.typewrite("+")
            return HttpResponse("+ Typed...")
        elif command == "volume-down":
            pyautogui.typewrite("-")
            return HttpResponse("- Typed...")
        elif command == "arrow-up":
            pyautogui.hotkey("up")
            return HttpResponse("- Typed...")
        elif command == "open-terminal":
            os.system('qterminal &')
            return HttpResponse("RUNNING QTerminal...")
    return render(request, 'index.html')
