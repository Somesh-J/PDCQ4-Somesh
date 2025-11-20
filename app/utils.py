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
    formatted_time = current_time.strftime('%d-%m-%Y %H:%M:%S %Z')
    
    return formatted_time

def generate_pattern(n: int) -> str:
        text = "FORMULAQSOLUTIONS"
        L = len(text)

        def seq(start, length):
            return "".join(text[(start+i) % L] for i in range(length))

        half = n // 2
        lines = []

        for i in range(n):
            idx = i if i <= half else n - i - 1
            space = " " * abs(half - idx)
            size = 2 * idx + 1
            start = i  # always continue forward sequence
            inside = size - 2

            if size == 1:
                lines.append(space + text[start % L])
                continue

            if i <= half:
                if idx % 2 == 0:  # even => letter line
                    lines.append(space + seq(idx, size))
                else:             # odd => dashed line
                    left = text[idx % L]
                    right = text[(idx + size - 1) % L]
                    lines.append(space + left + "-" * inside + right)
            else:
                if idx % 2 == 0:  # even => letter line
                    lines.append(space + seq(start, size))
                else:             # odd => dashed line
                    left = text[start % L]
                    right = text[(start + size - 1) % L]
                    lines.append(space + left + "-" * inside + right)

        return "\n".join(lines)

