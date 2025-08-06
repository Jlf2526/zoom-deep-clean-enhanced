# Phone Number Lookup Tool

This tool uses the NumVerify API to look up publicly available information about phone numbers.

## ⚠️ Important Legal Notice

This tool is for legitimate purposes only. It only provides information that is publicly available through official channels. Misuse of this tool may violate privacy laws and terms of service.

## Features

- Validates phone numbers
- Provides country information
- Shows carrier information when available
- Indicates line type (mobile, landline, etc.)

## Installation

1. Install the required dependencies:
   ```bash
   pip install -r requirements_phone_lookup.txt
   ```

2. Get a free API key from [NumVerify](https://numverify.com/) (optional but recommended for regular use)

## Usage

```bash
# Look up a phone number (using default API key)
python3 phone_lookup.py +14155550123

# Look up a phone number with your own API key
python3 phone_lookup.py +14155550123 --api-key YOUR_KEY
```

## Limitations

1. Only provides publicly available information
2. Accuracy depends on data provider
3. Not all information is available for all numbers
4. Some numbers may be unlisted or private

## Legal and Ethical Usage

This tool should only be used for legitimate purposes such as:
- Validating contact information you have permission to check
- Identifying unknown callers for personal safety
- Business contact verification

Do NOT use this tool for:
- Harassment or stalking
- Unsolicited marketing
- Any illegal activities
- Violating anyone's privacy