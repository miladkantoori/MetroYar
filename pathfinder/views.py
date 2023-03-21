from django.shortcuts import render
from django.http import HttpResponse
from pathfinder.backend import *
from pathfinder.subway import *
from pathfinder.subway2 import *


def HomePageView(request):
    if request.method == 'POST':
        
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')
        #input validation
        stlist = []
        for obj in subway.stations:
            stlist.append(str(obj))
        ortest = origin in stlist
        destest = destination in stlist
        if origin == destination or destest == False or ortest == False:
            error = ''
            options = subway.stations

            context = {
                'error': error,
                'options': options
            }
            return render(request, 'home.html', context)
        else:
            # Find shortest path and its cost between stations
            stops, lines, cost = calculate(str(origin), str(destination))

            s1, l1 ,cost1 = calculate('تجریش', 'کهریزک')
            s1w, l1w, cost2 = calculate('شاهد', 'فرودگاه امام خمینی')
            s2, l2, cost3 = calculate('فرهنگسرا', 'تهران (صادقیه)')
            s3, l3, cost4 = calculate('قائم', 'آزادگان')
            s4, l4, cost5 = calculate('شهید کلاهدوز', 'ارم سبز')
            s4s, l4s, cost6 = calculate('بیمه', 'پایانه 4و6 فرودگاه مهرآباد')
            s5, l5, cost7 = calculate('تهران (صادقیه)', 'گلشهر')
            s5w, l5w, cost8 = calculate('گلشهر', 'شهید سپهبد سلیمانی')
            s6e, l6e, cost9 = calculate('دولت آباد', 'امام حسین')
            s6w, l6w, cost10 = calculate('دانشگاه تربیت مدرس', 'شهید ستاری')
            s7, l7, cost11 = calculate('بسیج', 'میدان صنعت')
            
            lines2 = []
            
            for line in lines:
                if line == 'l1':
                    i = stops.index(next(station for station in stops if station.line == 'l1'))
                    j = s1.index(next(station for station in s1 if station.name == stops[i].name))
                    if stops[i+1].name == s1[j+1].name:
                        lines2.append(Line('l1','خط 1 - به سمت کهریزک'))
                    else:
                        lines2.append(Line('l1','خط 1 - به سمت تجریش'))
                elif line == 'l1w':
                    i = stops.index(next(station for station in stops if station.line == 'l1w'))
                    j = s1w.index(next(station for station in s1w if station.name == stops[i].name))
                    if stops[i+1].name == s1w[j+1].name:
                        lines2.append(Line('l1w','خط 1 - به سمت فرودگاه امام خمینی'))
                    else:
                        lines2.append(Line('l1w','خط 1 - به سمت شاهد'))
                elif line == 'l2':
                    i = stops.index(next(station for station in stops if station.line == 'l2'))
                    j = s2.index(next(station for station in s2 if station.name == stops[i].name))
                    if stops[i+1].name == s2[j+1].name:
                        lines2.append(Line('l2','خط 2 - به سمت صادقیه'))
                    else:
                        lines2.append(Line('l2','خط 2 - به سمت فرهنگسرا'))
                elif line == 'l3':
                    i = stops.index(next(station for station in stops if station.line == 'l3'))
                    j = s3.index(next(station for station in s3 if station.name == stops[i].name))
                    if stops[i+1].name == s3[j+1].name:
                        lines2.append(Line('l3','خط 3 - به سمت آزادگان'))
                    else:
                        lines2.append(Line('l3','خط 3 - به سمت قائم'))
                elif line == 'l4':
                    i = stops.index(next(station for station in stops if station.line == 'l4'))
                    j = s4.index(next(station for station in s4 if station.name == stops[i].name))
                    if stops[i+1].name == s4[j+1].name:
                        lines2.append(Line('l4','خط 4 - به سمت ارم سبز'))
                    else:
                        lines2.append(Line('l4','خط 4 - به سمت شهید کلاهدوز'))
                elif line == 'l4s':
                    i = stops.index(next(station for station in stops if station.line == 'l4s'))
                    j = s4s.index(next(station for station in s4s if station.name == stops[i].name))
                    if stops[i+1].name == s4s[j+1].name:
                        lines2.append(Line('l4s','خط 4 - به سمت فرودگاه مهر آباد'))
                    else:
                        lines2.append(Line('l4s','خط 4 - به سمت بیمه'))
                elif line == 'l5':
                    i = stops.index(next(station for station in stops if station.line == 'l5'))
                    j = s5.index(next(station for station in s5 if station.name == stops[i].name))
                    if stops[i+1].name == s5[j+1].name:
                        lines2.append(Line('l5','خط 5 - به سمت گلشهر'))
                    else:
                        lines2.append(Line('l5','خط 5 - به سمت صادقیه'))
                elif line == 'l5w':
                    i = stops.index(next(station for station in stops if station.line == 'l5w'))
                    j = s5w.index(next(station for station in s5w if station.name == stops[i].name))
                    if stops[i+1].name == s5w[j+1].name:
                        lines2.append(Line('l5w','خط 5 - به سمت شهید سپهبد سلیمانی'))
                    else:
                        lines2.append(Line('l5w','خط 5 - به سمت گلشهر'))
                elif line == 'l6e':
                    i = stops.index(next(station for station in stops if station.line == 'l6e'))
                    j = s6e.index(next(station for station in s6e if station.name == stops[i].name))
                    if stops[i+1].name == s6e[j+1].name:
                        lines2.append(Line('l6e','خط 6 - به سمت امام حسین'))
                    else:
                        lines2.append(Line('l6e','خط 6 - به سمت دولت آباد'))
                elif line == 'l6w':
                    i = stops.index(next(station for station in stops if station.line == 'l6w'))
                    j = s6w.index(next(station for station in s6w if station.name == stops[i].name))
                    if stops[i+1].name == s6w[j+1].name:
                        lines2.append(Line('l6w','خط 6 - به سمت شهید ستاری'))
                    else:
                        lines2.append(Line('l6w','خط 6 - به سمت تربیت مدرس'))
                elif line == 'l7':
                    i = stops.index(next(station for station in stops if station.line == 'l7'))
                    j = s7.index(next(station for station in s7 if station.name == stops[i].name))
                    if stops[i+1].name == s7[j+1].name:
                        lines2.append(Line('l7','خط 7 - به سمت میدان صنعت'))
                    else:
                        lines2.append(Line('l7','خط 7 - به سمت بسیج'))
            error = 'hidden=True'

            if cost > 60:
                costdesc = str('{h} ساعت و {m} دقیقه'.format(h=int(cost/60), m=cost%60))
                cost = str('{h}:{m:02d}'.format(h=int(cost/60), m=cost%60))
            else:
                costdesc = str('{m} دقیقه'.format(m=int(cost)))
                cost = str('00:{m:02d}'.format(m=int(cost)))
            context = {
                'stops': stops,
                'cost': cost,
                'lines': lines2,
                'error': error,
                'costdesc': costdesc,
                
            }
            return render(request, 'result.html', context)

        # current_line = ''
        # linechange_penalty = 8
        # stops = []
        # lines = []

        # #checking line change method
        # def lineChange(a, b):
        #     a_set = set(a)
        #     b_set = set(b)
        #     if (a_set & b_set):
        #         return False
        #     else:
        #         return True

        # for index, station in enumerate(fpath):
        #     #checking if we are entering a station
        #     if index == 0:
        #         current_line = list(set(fpath[index].lines).intersection(fpath[index+1].lines))[0]
        #         stops.append(Stop(station.name, current_line))
        #         lines.append(current_line)
        #     #checking if we are changing lines
        #     elif index != len(fpath)-1 and lineChange(fpath[index-1].lines, fpath[index+1].lines):
        #         cost += linechange_penalty
        #         stops.append(Stop(station.name, current_line))
        #         current_line = list(set(fpath[index].lines).intersection(fpath[index+1].lines))[0]
        #         lines.append(current_line)
        #         stops.append(Stop(station.name, current_line))
        #     #then we are just on our way
        #     else:
        #         stops.append(Stop(station.name, current_line))
        
        

    options = subway.stations

    error = 'hidden=True'

    context = {
        'options': options,
        'error': error,

    }
    return render(request, 'home.html', context)




