import json
from datetime import datetime
import pytz
from typing import Dict, List

def get_current_time_in_countries(countries: List[Dict]) -> Dict[str, Dict[str, str]]:
    """
    Get the current time in each country, grouped by continent.
    
    Args:
        countries (List[Dict]): List of country dictionaries containing timezone and continent info
        
    Returns:
        Dict[str, Dict[str, str]]: Dictionary with continent as key and nested dictionary of 
        country names and their current times as values
        
    Example:
        {
            'Europe': {
                'United Kingdom': '14:30:45',
                'France': '15:30:45'
            },
            'Asia': {
                'Japan': '22:30:45'
            }
        }
    """
    pass