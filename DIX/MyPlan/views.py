# -*- coding: utf-8 -*-
from django.shortcuts import render

from Meals.models import Meals
from include import mail

from .models import SinglePlan
from .models import Sprints


def index(request):

    return render(request, 'MyPlan/index.html')

def new_plan(request):
    return render(request, 'MyPlan/new_plan.html', {'meals': Meals.objects.all()})

def my_plans(request):
    return render(request, 'MyPlan/my_plans.html', {'my_plans': SinglePlan.objects.all()})

def start_sprint(request):
    components = {}

    for sprint in Sprints.objects.all():
        if sprint.sprint_status == 'Nowy':
            print('Nowy sprint : {}'.format(sprint.sprint_id))
            sprint.sprint_status = 'Rozpoczety'
            sprint.save()

        for sprint_param in sprint.sprint_parameters.all():
            for single in sprint_param.meals.all():
                for a in single.components.all():
                    if a.name not in components:
                        components[a.name] = a.waste
                    else:
                        components[a.name] = components[a.name] + a.waste

    mail.send_main(components)
    return render(request, 'MyPlan/start_sprint.html', {'components': components})