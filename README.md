# Overview

I created this project with a boilerplate hoping it would save me some time but there is a bunch of Python specific things I'm not familiar with so it ended up taking a bit more time than I expected.

## Backend infra
Before starting on the code I spun up a lightweight DynamoDB database fronted by API Gateway following this guide: https://aws.amazon.com/blogs/compute/using-amazon-api-gateway-as-a-proxy-for-dynamodb/

You can view the output yourself by going to the endpoints yourself:
* https://2zkyzix7jl.execute-api.us-west-2.amazonaws.com/test/api1/1
* https://2zkyzix7jl.execute-api.us-west-2.amazonaws.com/test/api2/1
* https://2zkyzix7jl.execute-api.us-west-2.amazonaws.com/test/api3/1

I added the ability to add rows to the table by making a post request to the endpoint https://2zkyzix7jl.execute-api.us-west-2.amazonaws.com/test/api3/

If you run on a UNIX system, you can use `curl`. Something like
```
curl -X POST "https://2zkyzix7jl.execute-api.us-west-2.amazonaws.com/test/api3"
   -H "Content-Type: application/json"
   -d '{"member_id": 2, "stop_loss": 20000, "deductible": 1500, "oop_max": 8000}'
```

Get the result by making a GET request
```
curl -X GET "https://2zkyzix7jl.execute-api.us-west-2.amazonaws.com/test/api3/2"
   -H "Content-Type: application/json"
```

Or you can just view the output by loading the above URL in the browser directly.

## Code
As for the actual code, there are a few main bits.
* Data fetching
* Response data modeling
* Coalescing strategy
* Unit tests

For the coalescing strategy as well as for the response data model conversion, I decided to go with a functional approach which allows developers to specify functions themselves depending on the output and the strategy. This is useful for containerizing concrete logic onto potentially different output for APIs.

Workflow
* Fetched data from all 3 APIs
* Response is transformed into a sensible data structure
* The resulting output for each API is then aggregated again into a dictionary that can then be used for a coalescing strategy. 
* Run different coalescing strategies on the aggregate results

## Run the main function
Hopefully the following commands will work for you.

After cloning or downloading the repo, create a Python virtual environment with:
```
python -m venv .virtualenv
source .virtualenv/bin/activate
pip install -e .
python src/nirvana/main.py
```

## Run tests
I didn't get a chance to write tests for everything. Hope that's okay!

```
pip install -e .[dev]
python -m pytest
```
