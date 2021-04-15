from django.shortcuts import render
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "4f6a08d171msh03f25d12b0085bcp127056jsnf36b65e65737",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

def HomeView(request):
    number_of_results = int(response['results'])
    country = [response['response'][x]['country'] for x in range(0, number_of_results)]

    if request.method == "POST":
        selectedCountry = request.POST['Country']
        for counter in range(0, number_of_results):
            if selectedCountry == response['response'][counter]['country']:
                new = response['response'][counter]['cases']['new']
                active = response['response'][counter]['cases']['active']
                critical = response['response'][counter]['cases']['critical']
                recovered = response['response'][counter]['cases']['recovered']
                total = response['response'][counter]['cases']['total']
                deaths = int(total) - int(active) - int(recovered)
        context = {'countries':country,'selected_country': selectedCountry, 'new':new, 'active':active, 'critical': critical,
                   'recovered': recovered, 'deaths':deaths,'total':total}
        return render(request, 'home.html', context)

    context = {'countries': country}
    return render(request, 'home.html', context)
