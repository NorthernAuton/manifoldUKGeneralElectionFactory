import requests
import datetime

# API endpoint for creating a market
api_url = "https://manifold.markets/api/v0/market"

# Your API key
api_key = "REPLACEME"  # Replace with your actual API key

# List of constituencies to create
constituencies = [
    ""
]  # Replace with actual constituency names
constituencies.sort()
# List of parties to add as answers
answers = ["Conservative", "Labour"] # Do not add "Other", this is created automatically by the question type. Recommend minimal answers to reduce Mana cost, further answers can be added later.
# Group IDs
group_ids = [
    "MR6TpXWpELsvTK0BY29F", # UK Politics
    "aavkiDd6uZggfL3geuV2", # United Kingdom
    "f763184a-51f4-4de2-a9df-d290134e6298" # UK 2024 General Election Constituency Winning Party
]

for constituency_name in constituencies:
    # Market data
    market_data = {
        "outcomeType": "MULTIPLE_CHOICE",
        "question": f"UK General Election: Which party will win {constituency_name}?",
        "descriptionHtml": "This refers to the next general election to take place electing representatives to the UK parliament following December 2019.<br><br>Market resolves 100% to the party with the winning candidate.<br><br>Please submit answers in the form of a political party, not an individual. If you wish to submit an individual who will run as an independent, please submit your answer in the form: 'Independent: [person's name]'. If anybody submits 'Independent' as an answer, it will not resolve YES, even if an independent wins.<br><br>'Labour' and 'Labour and Co-operative' will be treated interchangeably.<br><br>I may bet in this market.",
        "closeTime": int(datetime.datetime(2024, 12, 31).timestamp() * 1000),  # UNIX timestamp in milliseconds
        "answers": answers,
        "addAnswersMode": "ANYONE",
        "shouldAnswerSumToOne": True,
        "groupIds": group_ids  # Adding the group IDs
    }

    # Sending the POST request to create the market
    response = requests.post(api_url, json=market_data, headers={"Authorization": f"Key {api_key}"})

    # Check if the request was successful
    if response.status_code == 200:
        print(f"Market created successfully for {constituency_name}")
    else:
        print(f"Failed to create market for {constituency_name}: {response.text}")