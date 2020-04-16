from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import DistrictInfo, CaseInfo, TotalInfo, DivisionInfo, WebHitCounter, DivisionName
import folium
import  numpy as np
import warnings

warnings.filterwarnings('ignore')

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

    webhit = WebHitCounter.objects.all().order_by('-counter')[0]
    count=webhit.counter+1
    new_count = WebHitCounter(counter=count)
    new_count.save()

    context = {'new_case': new_case, 'new_death': new_death, 'new_recovery': new_recovery,
               'total_case': total_case, 'total_death': total_death,
               'total_recovery': total_recovery, 'active_case': active_case}

    return render(request, 'index.html', context=context)


def get_division_data(request):
    division = DivisionName.objects.all()
    div_name = []
    div_total_cases = []
    div_all_names = []
    div_all_cases = [[] for i in range(len(division))]
    div_all_dates = [[] for i in range(len(division))]
    
    for i,div in enumerate(division):
        infos = DivisionInfo.objects.filter(name=div).order_by('-date')
        div_name.append(div.name)
        div_total_cases.append(infos[0].cases)

    for i,div in enumerate(division):
        infos = DivisionInfo.objects.filter(name=div).order_by('date')
        div_all_names.append(div.name)
        for info in infos:
            div_all_cases[i].append(info.cases)
            div_all_dates[i].append(info.date)

    data = {
        'div_name': div_name,
        'div_total_cases': div_total_cases,
        'div_all_names': div_all_names,
        'div_all_cases': div_all_cases,
        'div_all_dates': div_all_dates,
    }

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


def map_view(request):
    districts = DistrictInfo.objects.all()
    bd_lat = 23.6850
    bd_lon = 90.3563

    figure = folium.Figure()
    m = folium.Map(location=[bd_lat, bd_lon], zoom_start=8)
    m.add_to(figure)

    for dist in districts:
        info = CaseInfo.objects.filter(name=dist).order_by('-cases')
        folium.vector_layers.CircleMarker(
            location=[dist.lat, dist.lon],
            radius=np.log(info[0].cases * 300),  # define how big you want the circle markers to be
            color=None,
            fill=True,
            #popup=dist.dist_name + ": " + str(info[0].cases),
            tooltip=dist.dist_name + ": " + str(info[0].cases),
            fill_color='red',
            fill_opacity=0.7
        ).add_to(m)
    
    figure.render()
    
    return render(request, 'map.html', {'map': figure})


def web_hit(request):
    hit_counter = WebHitCounter.objects.all().order_by("-counter")[0]
    counter = hit_counter.counter

    return render(request, 'web_hit_counter.html', context={'counter': counter})
