from statistics import mean

# Weighted by api name
def coalesce_weighted_mean(api_responses):
    weights = {
        "api1": 0.5,
        "api2": 0.3,
        "api3": 0.2,
    }
    weighted_mean = 0
    for api, value in api_responses.items():
        weighted_mean += weights[api] * value
    return weighted_mean/len(api_responses)

# Ignoring a particular api response
def coalesce_mean_ignore_api1(api_responses):
    filtered = {k: v for k, v in api_responses.items() if k.find("api1") == -1}
    return mean(filtered.values())