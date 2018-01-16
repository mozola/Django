# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.conf import settings
from .models import Meals


def index(request):
    return render(request, 'Meals/index.html', {'all_meals': Meals.objects.all() , 'meala': settings.BASE_DIR})


def details(request, meal_id):
    return render(request, 'Meals/details.html', {'meals_id': Meals.objects.get(pk = meal_id)})