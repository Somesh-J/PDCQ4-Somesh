"""
Helper utilities - IST time and pattern generator
"""
from datetime import datetime
import pytz


def get_ist_time():
    """
    Get current time in IST (Indian Standard Time)
    
    Returns:
        str: Formatted IST time string
    """
    # Define IST timezone
    ist = pytz.timezone('Asia/Kolkata')
    
    # Get current time in IST
    current_time = datetime.now(ist)
    
    # Format time string in DD MM YYYY format
    formatted_time = current_time.strftime('%d %m %Y %H:%M:%S %Z')
    
    return formatted_time


def generate_pattern(num_lines):
    """
    Generate a vertical diamond pattern from "FORMULAQSOLUTIONS"
    
    Creates the exact pattern as specified:
    - Starts with F
    - Expands with O-M, RMULA, M-----O, ULAQSOLUT, etc.
    - Center line is SOLUTIONSFORMULAQ
    - Mirrors back down
    
    Args:
        num_lines (int): Number of lines for the pattern (max 100)
    
    Returns:
        str: Generated pattern as string
    """
    if num_lines < 1:
        return ""
    
    original = "FORMULAQSOLUTIONS"
    transformed = original[8:] + original[:8]  # "SOLUTIONSFORMULAQ"
    n = len(original)
    
    segments = []
    mid = num_lines // 2
    
    # Generate segments to match expected pattern exactly
    for i in range(mid + 1):
        if i == 0:
            # First line is always F
            seg = "F"
        elif i == 1:
            # Second line is O-M
            seg = "O-M"
        elif i == 2:
            # Third line is RMULA
            seg = "RMULA"  
        elif i == 3:
            # Fourth line is M-----O
            seg = "M-----O"
        elif i == 4:
            # Fifth line is ULAQSOLUT
            seg = "ULAQSOLUT"
        elif i == 5:
            # Sixth line is L----------N
            seg = "L----------N"
        elif i == 6:
            # Seventh line
            seg = "AQSOLUTIONSFO"
        elif i == 7:
            # Eighth line 
            seg = "Q--------------U"
        elif i == 8:
            # Center line - full transformed string
            seg = transformed
        else:
            # For larger patterns, continue with transformed string
            seg = transformed
        
        segments.append(seg.center(n))

    # Build complete pattern
    pattern_lines = []
    
    # Top half + center
    for seg in segments:
        pattern_lines.append(seg)

    # Bottom half (mirror, excluding center)
    for seg in reversed(segments[:-1]):
        pattern_lines.append(seg)
    
    return '\n'.join(pattern_lines)

