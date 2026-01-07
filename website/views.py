from django.shortcuts import render


def homw(request):
	return render(request, 'home.html', {})