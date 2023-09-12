from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Fathi Qushoyyi Ahimsa',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
