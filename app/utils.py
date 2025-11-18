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
    
    Pattern logic:
    - Transform string: "SOLUTIONSFORMULAQ" (swap at index 8)
    - Double it for circular reading: "SOLUTIONSFORMULAQSOLUTIONSFORMULAQ"
    - Start from F (index 9) and expand symmetrically
    - Odd layers (1, 3, 5...) replace middle with dashes
    - Mirror pattern after center
    
    Args:
        num_lines (int): Number of lines for the pattern (max 100)
    
    Returns:
        str: Generated pattern as string
    """
    if num_lines < 1:
        return ""
    original = "FORMULAQSOLUTIONS"
    n = len(original)
    lines = []
    mid = num_lines // 2
    # Top half (including center for odd n)
    for i in range(mid + 1):
        if i == 0:
            seg = original[0]
        else:
            left = i
            right = n - i
            if left < right:
                seg = original[left:right]
            else:
                seg = ""
            if i % 2 == 1 and len(seg) > 2:
                seg = seg[0] + "-" * (len(seg) - 2) + seg[-1]
        line = seg.center(n)
        lines.append(line)
    # Center line for even num_lines
    if num_lines % 2 == 0:
        # For even, center is between two chars, so use the full string
        lines.append(original)
    # Bottom half (mirror)
    for i in range(mid, 0, -1):
        if i == 0:
            seg = original[0]
        else:
            left = i
            right = n - i
            if left < right:
                seg = original[left:right]
            else:
                seg = ""
            if i % 2 == 1 and len(seg) > 2:
                seg = seg[0] + "-" * (len(seg) - 2) + seg[-1]
        line = seg.center(n)
        lines.append(line)
    return '\n'.join(lines)

