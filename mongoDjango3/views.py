from django.shortcuts import render, redirect

from admin_page import models

def test_view(request):
    if request.method == 'POST':
        water = models.Water.objects.create(weight='125')
        water.save()
        beer = models.Beer.objects.create(name='bud', value=water)
        beer.save()
        return redirect('test_view')
    return render(request, 'test_view.html', {'test_view': 'test'})
