from fetch.fetch import fetch

'''
Implementation of insurance data fetching along with a response to data model function.
This converter can have distinct implementations for different APIs to have a consistent data model output.
'''
def fetch_insurance_data(endpoint):
    # Defining an in-line function likes this makes it clear that this function is only meant to be used in this scope
    def response_to_data_model(response):
        items = response.json().get("Items")[0]
        # Accessing first index is okay because we are guaranteed to get at most one item back (hashkey based query)
        stop_loss = items.get("stop_loss").get("N")
        deductible = items.get("deductible").get("N")
        oop_max = items.get("oop_max").get("N")
        data_model = {
            "stop_loss": int(stop_loss),
            "deductible": int(deductible),
            "oop_max": int(oop_max),
        }
        print(f"Got data result: {data_model}")
        return data_model
    return fetch(endpoint, response_to_data_model)

'''
Aggregator of all API outputs into a single results dictionary keyed by api_name.
This is a convenient data structure for the coalescing strategy.
'''
api_names = ["api1", "api2", "api3"]
endpoint_prefix = "https://2zkyzix7jl.execute-api.us-west-2.amazonaws.com/test"
def fetch_all_insurance_data(member_id):
    api_endpoints = [f"{endpoint_prefix}/{api}/{member_id}" for api in api_names]
    results = {"stop_loss": {}, "deductible": {}, "oop_max": {}}
    for api_name, endpoint in zip(api_names, api_endpoints):
        # TODO: Parallelize this for performance boost
        insurance_data = fetch_insurance_data(endpoint)
        results["stop_loss"][api_name] = insurance_data.get("stop_loss")
        results["deductible"][api_name] = insurance_data.get("deductible")
        results["oop_max"][api_name] = insurance_data.get("oop_max")
    return results
