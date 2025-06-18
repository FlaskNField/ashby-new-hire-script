# Ashby to Notion New Hire Sync

This script automates the process of adding candidates who have accepted a job offer in Ashby to a Notion database for new hires.

## Overview

When a candidate’s status in Ashby is marked as “Offer Accepted,” this script retrieves their information and creates a new entry in your Notion “New Hires” database. This helps HR and onboarding teams keep Notion up-to-date automatically.

## Features

- Fetches candidates with “Offer Accepted” status from Ashby via API
- Adds each new hire to a specified Notion database
- Syncs key candidate details (name, email, role, start date)

## Requirements

- Python 3.7+
- [Ashby API access](https://developers.ashbyhq.com/)
- [Notion integration token and database](https://developers.notion.com/)
- `requests` Python package

## Setup

1. **Clone this repository**
2. **Install dependencies:**
   ```bash
   pip install requests
   ```
3. **Configure your credentials:**
   - Set your Ashby API key, Notion integration token, and Notion database ID in the script.
4. **Adjust field names** in the script to match your Ashby and Notion schemas if needed.

## Usage

Run the script:
```bash
python sync_ashby_to_notion.py
```

Each candidate with an “Offer Accepted” status in Ashby will be added to your Notion database as a new page.

## Customization

- Update the candidate filtering logic to match your workflow.
- Map additional fields as needed by editing the Notion properties in the script.

## References

- [Ashby API Documentation](https://developers.ashbyhq.com/)
- [Notion API Documentation](https://developers.notion.com/)

## License

MIT

---

**Author:** David Larsen
**Contact:** dc2larsen@gmail.com
