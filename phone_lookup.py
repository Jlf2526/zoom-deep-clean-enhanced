#!/usr/bin/env python3
"""
Phone Number Information Lookup Tool

This script uses the NumVerify API to look up publicly available information
about phone numbers. Note that this only works for valid phone numbers and
provides only publicly available information.

IMPORTANT: This tool is for legitimate purposes only.
Misuse of this tool may violate privacy laws and terms of service.
"""

import requests
import json
import argparse
import sys
import os
from typing import Dict, Any, Optional

# Free API key from NumVerify (limited to 250 requests/month)
# For production use, you should get your own API key
DEFAULT_API_KEY = "YOUR_API_KEY_HERE"

def lookup_phone_number(phone_number: str, api_key: str) -> Optional[Dict[str, Any]]:
    """
    Look up information about a phone number using NumVerify API
    
    Args:
        phone_number (str): The phone number to look up
        api_key (str): NumVerify API key
        
    Returns:
        dict: Information about the phone number or None if error
    """
    url = f"http://apilayer.net/api/validate"
    
    params = {
        'access_key': api_key,
        'number': phone_number,
        'country_code': '',  # Auto-detect
        'format': 1  # JSON format
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        if not data.get('valid'):
            print(f"❌ Invalid phone number: {phone_number}")
            return None
            
        return data
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ JSON parsing error: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def format_phone_info(data: Dict[str, Any]) -> str:
    """
    Format phone number information for display
    
    Args:
        data (dict): Raw data from NumVerify API
        
    Returns:
        str: Formatted information string
    """
    lines = []
    lines.append("=" * 50)
    lines.append("📱 PHONE NUMBER INFORMATION")
    lines.append("=" * 50)
    
    lines.append(f"📱 Number: {data.get('number', 'N/A')}")
    lines.append(f"✅ Valid: {'Yes' if data.get('valid') else 'No'}")
    lines.append(f"📍 Country: {data.get('country_name', 'N/A')} ({data.get('country_code', 'N/A')})")
    lines.append(f"☎️  Carrier: {data.get('carrier', 'N/A')}")
    lines.append(f"📱 Line Type: {data.get('line_type', 'N/A')}")
    
    if data.get('location'):
        lines.append(f"🌍 Location: {data.get('location', 'N/A')}")
    
    lines.append("")
    lines.append("⚠️  DISCLAIMER:")
    lines.append("This information is publicly available data only.")
    lines.append("Accuracy depends on the data provider and may not be current.")
    lines.append("This tool is for legitimate purposes only.")
    
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(
        description="Look up publicly available information about phone numbers",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
EXAMPLES:
  # Look up a phone number
  python3 phone_lookup.py +14155550123
  
  # Look up a phone number with your own API key
  python3 phone_lookup.py +14155550123 --api-key YOUR_KEY
  
NOTE:
  - Phone numbers should include country code (e.g., +1 for US)
  - This tool only provides publicly available information
  - For privacy and legal reasons, detailed personal information is not accessible
        """
    )
    
    parser.add_argument(
        "phone_number",
        help="Phone number to look up (include country code, e.g., +14155550123)"
    )
    
    parser.add_argument(
        "--api-key",
        help="NumVerify API key (get one at https://numverify.com/)",
        default=DEFAULT_API_KEY
    )
    
    args = parser.parse_args()
    
    # Check if API key is set
    if args.api_key == DEFAULT_API_KEY:
        print("⚠️  WARNING: Using default API key")
        print("   For regular use, please get your own free API key at https://numverify.com/")
        print("   The default key is limited and may not work.")
        print()
    
    print(f"🔍 Looking up information for: {args.phone_number}")
    print()
    
    # Perform lookup
    result = lookup_phone_number(args.phone_number, args.api_key)
    
    if result:
        print(format_phone_info(result))
        return 0
    else:
        print("❌ Failed to retrieve information")
        return 1

if __name__ == "__main__":
    sys.exit(main())