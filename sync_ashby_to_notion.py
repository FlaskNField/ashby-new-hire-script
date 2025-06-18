import requests

# --- CONFIGURATION ---

# Ashby API
ASHBY_API_KEY = 'your_ashby_api_key'
ASHBY_API_URL = 'https://api.ashbyhq.com/v1/candidates'  # Adjust endpoint as needed

# Notion API
NOTION_TOKEN = 'your_notion_integration_token'
NOTION_DATABASE_ID = 'your_notion_database_id'
NOTION_API_URL = 'https://api.notion.com/v1/pages'
NOTION_VERSION = '2022-06-28'

# --- FETCH CANDIDATES WHO ACCEPTED OFFER FROM ASHBY ---

def get_accepted_candidates():
    headers = {
        'Authorization': f'Bearer {ASHBY_API_KEY}',
        'Content-Type': 'application/json'
    }
    # Adjust filter as needed for your Ashby API
    response = requests.get(ASHBY_API_URL, headers=headers)
    response.raise_for_status()
    candidates = response.json().get('candidates', [])
    # Filter for accepted offers (adjust field names as needed)
    accepted = [c for c in candidates if c.get('status') == 'Offer Accepted']
    return accepted

# --- ADD CANDIDATE TO NOTION ---

def add_candidate_to_notion(candidate):
    headers = {
        'Authorization': f'Bearer {NOTION_TOKEN}',
        'Notion-Version': NOTION_VERSION,
        'Content-Type': 'application/json'
    }
    data = {
        "parent": { "database_id": NOTION_DATABASE_ID },
        "properties": {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": candidate.get('name', 'Unknown')
                        }
                    }
                ]
            },
            "Email": {
                "email": candidate.get('email', '')
            },
            "Role": {
                "rich_text": [
                    {
                        "text": {
                            "content": candidate.get('role', '')
                        }
                    }
                ]
            },
            "Start Date": {
                "date": {
                    "start": candidate.get('start_date', '')
                }
            }
        }
    }
    response = requests.post(NOTION_API_URL, headers=headers, json=data)
    response.raise_for_status()
    return response.json()

# --- MAIN SCRIPT ---

if __name__ == "__main__":
    accepted_candidates = get_accepted_candidates()
    for candidate in accepted_candidates:
        result = add_candidate_to_notion(candidate)
        print(f"Added {candidate.get('name')} to Notion: {result.get('id')}")
