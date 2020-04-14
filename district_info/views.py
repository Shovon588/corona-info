from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import DistrictInfo, CaseInfo, TotalInfo, DivisionInfo
import folium

# Create your views here.


def get_data(request):
    infos = TotalInfo.objects.all().order_by('date')

    date = []; case_info = []; death_info = []; recov_info = []
    cumcase = []; cumdeath = []; cumrecov = []
    lastc = 0; lastd = 0; lastr = 0
    for info in infos:
        date.append(info.date)
        case_info.append(info.new_case)
        death_info.append(info.new_death)
        recov_info.append(info.new_recovery)
        lastc += case_info[-1]
        lastd += death_info[-1]
        lastr += recov_info[-1]
        cumcase.append(lastc)
        cumdeath.append(lastd)
        cumrecov.append(lastr)

    data = {
        'date': date,
        'case_info': case_info,
        'death_info': death_info,
        'cum_case': cumcase,
        'cum_death': cumdeath,
        'cum_recov': cumrecov
    }

    return JsonResponse(data=data)


def index(request):
    infos = TotalInfo.objects.all().order_by('date')

    date = []
    case_info = []
    death_info = []
    recovery_info = []

    for info in infos:
        date.append(info.date)
        case_info.append(info.new_case)
        death_info.append(info.new_death)
        recovery_info.append(info.new_recovery)

    total_case = sum(case_info)
    total_death = sum(death_info)
    total_recovery = sum(recovery_info)

    new_case = case_info[-1]
    new_death = death_info[-1]
    new_recovery = recovery_info[-1]

    active_case = total_case-total_death-total_recovery

    context = {'new_case': new_case, 'new_death': new_death, 'new_recovery': new_recovery,
               'total_case': total_case, 'total_death': total_death,
               'total_recovery': total_recovery, 'active_case': active_case}

    return render(request, 'index.html', context=context)


def get_district_data(request):
    division = DivisionInfo.objects.all().order_by('-cases')
    div_name = []
    div_cases = []
    for div in division:
        div_name.append(div.name)
        div_cases.append(div.cases)

    dists = DistrictInfo.objects.all()
    dist_name = []
    dist_cases = []
    new_cases = []
    for dist in dists:
        cases = CaseInfo.objects.filter(name=dist).order_by('-date')

        if len(cases)==1:
            new_cases.append(cases[0].cases)
        else:
            new_cases.append(cases[0].cases-cases[1].cases)

        dist_name.append(dist.dist_name)
        dist_cases.append(cases[0].cases)

    data = {
        'div_name': div_name,
        'div_cases': div_cases,
        'dist_name': dist_name,
        'dist_cases': dist_cases,
        'new_cases': new_cases
    }
    print(data)

    return JsonResponse(data=data)


def district(request):
    dists = DistrictInfo.objects.all()
    dist_name = []
    dist_cases = []
    new_cases = []
    for dist in dists:
        cases = CaseInfo.objects.filter(name=dist).order_by('-date')

        if len(cases) == 1:
            new_cases.append(cases[0].cases)
        else:
            new_cases.append(cases[0].cases - cases[1].cases)

        dist_name.append(dist.dist_name)
        dist_cases.append(cases[0].cases)

    data = zip(dist_name, dist_cases, new_cases)

    return render(request, 'district.html', context={"data": data})


