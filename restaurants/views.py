from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {

    }
    return render(request, 'detail.html', context)
