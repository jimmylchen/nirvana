import requests
from statistics import mean


def main():
    member_insurance = fetch_insurance_data(1)
    print(member_insurance)
    
    # Using mean
    coalesce_mean = lambda items: mean(items.values())
    coalesced_member_insurance = coalesce(member_insurance, coalesce_mean)
    print(coalesced_member_insurance)

    # Weighted by api name
    weights = {
        "api1": 0.5,
        "api2": 0.3,
        "api3": 0.2,
    }
    def coalesce_weighted_mean(api_responses):
        weighted_mean = 0
        for api, value in api_responses.items():
            weighted_mean += weights[api] * value
        return weighted_mean/len(api_responses)
    print(coalesce(member_insurance, coalesce_weighted_mean))

    # Ignoring a particular api response
    def coalesce_mean_ignore_api1(api_responses):
        filtered = {k: v for k, v in api_responses.items() if k.find("api1") == -1}
        return mean(filtered.values())
    print(coalesce(member_insurance, coalesce_mean_ignore_api1))


def coalesce(member_insurance, strategy):
    coalesced_result = {}
    for insurance_detail, responses in member_insurance.items():
        coalesced_result[insurance_detail] = strategy(responses)
    return coalesced_result


api_names = ["api1", "api2", "api3"]
def fetch_insurance_data(member_id):
    endpoint_prefix = "https://2zkyzix7jl.execute-api.us-west-2.amazonaws.com/test"
    api_endpoints = [f"{endpoint_prefix}/{api}/{member_id}" for api in api_names]
    results = {"stop_loss": {}, "deductible": {}, "oop_max": {}}
    # TODO: Parallelize this
    for api_name, endpoint in zip(api_names, api_endpoints):
        # TODO: Abstract this into a generic fetcher
        response = response_to_data_model(requests.get(endpoint))        
        results["stop_loss"][api_name] = response.get("stop_loss")
        results["deductible"][api_name] = response.get("deductible")
        results["oop_max"][api_name] = response.get("oop_max")

    return results

def response_to_data_model(response):
    items = response.json().get("Items")[0]
    # Accessing first index is okay because we are guaranteed to get at most one item back
    stop_loss = items.get("stop_loss").get("N")
    deductible = items.get("deductible").get("N")
    oop_max = items.get("oop_max").get("N")
    return {
        "stop_loss": int(stop_loss),
        "deductible": int(deductible),
        "oop_max": int(oop_max),
    }

if __name__ == "__main__":
    main()