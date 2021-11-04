import requests
from statistics import mean
from fetch.fetch_insurance_data import fetch_all_insurance_data
from coalesce.coalesce import coalesce
from coalesce.coalesce_strategies import coalesce_weighted_mean, coalesce_mean_ignore_api1

def main():
    member_insurance = fetch_all_insurance_data(1)
    print(f"Aggregated data from all APIs: {member_insurance}")
    
    # Using mean
    print("")
    print("Coalescing with average mean")
    mean_coalesced_member_insurance = coalesce(member_insurance, lambda items: mean(items.values()))
    print(mean_coalesced_member_insurance)

    print("")
    print("Coalescing with weighted mean")
    weighted_mean_coalesced_member_insurance = coalesce(member_insurance, coalesce_weighted_mean)
    print(weighted_mean_coalesced_member_insurance)

    print("")
    print("Coalescing with average mean after discard api1 data")
    ignore_api1_coalesced_member_insurance = coalesce(member_insurance, coalesce_mean_ignore_api1)
    print(ignore_api1_coalesced_member_insurance)

if __name__ == "__main__":
    main()
