'''
Generic function that takes in a member_insurance dict and applies some strategy function on each key/value pair
TODO: mypy typing will help
params:
    member_insurance: Dict[ApiName, Dict[InsuranceEnum, int]]
    strategy: Callable[Dict[str, int], int]
return type:
    Dict[ApiName, int]
'''
def coalesce(member_insurance, strategy):
    coalesced_result = {}
    for insurance_detail, responses in member_insurance.items():
        coalesced_result[insurance_detail] = strategy(responses)
    return coalesced_result
