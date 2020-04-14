from covid import Covid

# covid = Covid()
# covid.get_data()
# active = covid.get_total_active_cases()
# print(active)

covid = Covid(source="worldometers")
active = covid.get_total_active_cases()
confirmed = covid.get_total_confirmed_cases()
recovered = covid.get_total_recovered()
deaths = covid.get_total_deaths()

print(deaths)