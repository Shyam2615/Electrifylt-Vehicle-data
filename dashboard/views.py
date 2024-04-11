from django.shortcuts import render
from .models import *
from django.db.models import Q
from datetime import datetime
from django.db.models import Sum
from django.db.models.functions import Trunc

# Create your views here.


def home(request):
    queryset = VehicleData.objects.all()
    context = {"dataSet":queryset}
    
    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(
            Q(LicensePlate__icontains = search) |
            Q(Make__icontains = search) |
            Q(VIN__icontains = search) |
            Q(Model__icontains = search) |
            Q(Model__icontains = search) |
            Q(Type__icontains = search) |
            Q(date_str__icontains = search) |
            Q(MilesDriven__icontains = search)
        )
        context = {"dataSet":queryset}
    return render(request, "home.html", context)

def time_frame(request):
    if request.method == 'POST':
        from_date = request.POST.get('fromDate')
        to_date = request.POST.get('toDate')

        if from_date and to_date:
            from_date = datetime.strptime(from_date, '%Y-%m-%d')
            to_date = datetime.strptime(to_date, '%Y-%m-%d')

            data = VehicleData.objects.filter(date_str__range=(from_date, to_date))
        
        else:
            return render(request, 'time_frame.html', {'error':"Please select both From and To date"})

        if request.GET.get('search'):
            search = request.GET.get('search')
            data = data.filter(
                Q(LicensePlate__icontains = search) |
                Q(Make__icontains = search) |
                Q(VIN__icontains = search) |
                Q(Model__icontains = search) |
                Q(Model__icontains = search) |
                Q(Type__icontains = search) |
                Q(date_str__icontains = search) |
                Q(MilesDriven__icontains = search)
            )
            return render(request, 'time_frame.html', {'data': data})
        return render(request, 'time_frame.html', {'data': data})

    else:
        return render(request, 'time_frame.html')
    
def report_type(request):
    if request.method == 'POST':
        report_type = request.POST.get('reportType')
        from_date_str = request.POST.get('fromDate')
        to_date_str = request.POST.get('toDate')
        
        if from_date_str and to_date_str:
            from_date = datetime.strptime(from_date_str, '%Y-%m-%d')
            to_date = datetime.strptime(to_date_str, '%Y-%m-%d')
            
            if report_type == 'total_miles_driven':
                data = VehicleData.objects.filter(date_str__range=(from_date, to_date))
                
                total_miles_driven = sum([float(entry.MilesDriven) for entry in data])
                
                return render(request, 'report_type.html', {'Response': total_miles_driven})
            else:
                error_message = "Please select the nature of the data from the above dropdown"
                return render(request, 'report_type.html', {'Response': error_message})
        else:
            error_message = "Please provide both 'From' and 'To' dates."
            return render(request, 'report_type.html', {'Response': error_message})
    else:
        return render(request, 'report_type.html')
    
def frequency(request):
    if request.method == 'POST':
        report_type = request.POST.get('reportType')
        frequency = request.POST.get('frequency')
        from_date_str = request.POST.get('fromDate')
        to_date_str = request.POST.get('toDate')
        
        if from_date_str and to_date_str:
            from_date = datetime.strptime(from_date_str, '%Y-%m-%d')
            to_date = datetime.strptime(to_date_str, '%Y-%m-%d')
            
            if frequency == 'daily':
                data = VehicleData.objects.filter(date_str__range=(from_date, to_date))
                grouped_data = data.annotate(day=Trunc('date_str', 'day')).values('day').annotate(total_miles_driven=Sum('MilesDriven'))
            elif frequency == 'weekly':
                data = VehicleData.objects.filter(date_str__range=(from_date, to_date))
                grouped_data = data.annotate(week=Trunc('date_str', 'week')).values('week').annotate(total_miles_driven=Sum('MilesDriven'))
            elif frequency == 'monthly':
                data = VehicleData.objects.filter(date_str__range=(from_date, to_date))
                grouped_data = data.annotate(month=Trunc('date_str', 'month')).values('month').annotate(total_miles_driven=Sum('MilesDriven'))
            elif frequency == 'yearly':
                data = VehicleData.objects.filter(date_str__range=(from_date, to_date))
                grouped_data = data.annotate(year=Trunc('date_str', 'year')).values('year').annotate(total_miles_driven=Sum('MilesDriven'))
            else:
                error_message = "Invalid frequency selected."
                return render(request, 'frequency.html', {'error_message': error_message})
            
            return render(request, 'frequency.html', {'dataSet': grouped_data})
        else:
            error_message = "Please provide both 'From' and 'To' dates."
            return render(request, 'frequency.html', {'error_message': error_message})
    else:
        return render(request, 'frequency.html')