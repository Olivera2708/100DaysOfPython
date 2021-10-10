import requests

sheety_api = ""

class DataManager:
    def __init__(self):
         self.destination_data = {}

    def get_setination_data(self):
        response = requests.get(url=sheety_api)
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "prices": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{sheety_api}/{city['id']}", json=new_data)
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = ""
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
