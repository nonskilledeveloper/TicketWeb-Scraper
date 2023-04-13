# Here we have a code that filters the information using XPATH
def get_data(html_response, events_results, locations_results, dates_results):
    for n in range(20):
        events = html_response.xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div["+str(n+2)+"]/div[1]/div[1]/div/a/text()")
        events_results[n] = events[0]

        locations = html_response.xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div["+str(n+2)+"]/div[1]/div[2]/a[2]/text()")
        locations[0] = locations[0].lstrip().rstrip()

        addresses = html_response.xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div["+str(n+2)+"]/div[1]/div[2]/small/text()")
        addresses[0] = addresses[0].lstrip().rstrip()

        locations_results[n] = locations[0]+", "+addresses[0]

        dates = html_response.xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div["+str(n+2)+"]/div[1]/div[3]/span/text()")
        dates[0] = dates[0].lstrip().rstrip()

        hours = html_response.xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div["+str(n+2)+"]/div[1]/div[3]/small/text()")
        hours[0] = hours[0].lstrip().rstrip()
        hours[0] = hours[0].replace("                        ", "")

        dates_results[n] = dates[0]+" "+hours[0]

    return events_results, locations_results, dates_results