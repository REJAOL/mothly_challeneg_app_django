from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

from django.urls import reverse

# Create your views here.



monthly_challenges= {
    'january': 'No meat in january',
    'february': 'walk 20 minutes everyday in february',
    'march': 'learn django daily 20 minutes',
    'april': 'learn django daily 20 minutes',
    'may': 'learn django daily 20 minutes',
    'june': 'learn django daily 20 minutes',
    'july': 'learn django daily 20 minutes',
    'august': 'learn django daily 20 minutes',
    'september': 'learn django daily 20 minutes',
    'october': 'learn django daily 20 minutes',
    'november': 'learn django daily 20 minutes',
    'december': 'learn django daily 20 minutes',
}

def index(request):
    list_items=""
    
    months =  list(monthly_challenges.keys())
    
    for month in months:
        capitalize_month = month.capitalize()
        month_path = reverse('month-challenge', args=[month])
        list_items += f"<li> <a href= \"{month_path}\"> {capitalize_month} </a> </li>"
        
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data);

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if(month > len(months)):
        return HttpResponseNotFound('<h1>Invalid month</h1>')
        
    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            'text': challenge_text,
            'month_name':month
        }  )
    except:
        return HttpResponseNotFound('<h1>this is not supported</h1>')
    