# Step1: Agent & Tool

# 🗓️ Pretend this is Jeff's Calendar
FAKE_AVAILABILITY = {
    "2026-09-01": "Available from 10:00 AM to 12:00 PM",
    "2026-09-02": "Available from 3:00 PM to 5:00 PM",
    "2026-09-03": "Busy all afternoon (1:00 PM – 5:00 PM)",
    "2026-09-04": "Available all day",
    "2026-09-05": "Available from 11:00 AM to 1:00 PM",
    "2026-09-06": "Busy all day",
    "2026-09-07": "Available from 9:00 AM to 11:00 AM",
    "2026-09-08": "Available from 2:00 PM to 4:00 PM",
    "2026-09-09": "Available from 10:00 AM to 12:00 PM",
    "2026-09-10": "Busy all morning (9:00 AM – 12:00 PM)",
    "2026-09-11": "Available from 4:00 PM to 6:00 PM",
    "2026-09-12": "Available all day",
    "2026-09-13": "Busy all day",
    "2026-09-14": "Available from 10:00 AM to 12:00 PM",
    "2026-09-15": "Available from 3:00 PM to 5:00 PM",
    "2026-09-16": "Busy all afternoon (1:00 PM – 5:00 PM)",
    "2026-09-17": "Available from 11:00 AM to 1:00 PM",
    "2026-09-18": "Available all day",
    "2026-09-19": "Available from 2:00 PM to 4:00 PM",
    "2026-09-20": "Busy all day",
    "2026-09-21": "Available from 9:00 AM to 11:00 AM",
    "2026-09-22": "Available from 4:00 PM to 6:00 PM",
    "2026-09-23": "Busy all afternoon (1:00 PM – 5:00 PM)",
    "2026-09-24": "Available from 10:00 AM to 12:00 PM",
    "2026-09-25": "Available all day",
    "2026-09-26": "Available from 11:00 AM to 1:00 PM",
    "2026-09-27": "Busy all day",
    "2026-09-28": "Available from 3:00 PM to 5:00 PM",
    "2026-09-29": "Available from 10:00 AM to 12:00 PM",
    "2026-09-30": "Available from 4:00 PM to 6:00 PM",
}

def get_availability(date_str: str) -> dict[str, str]:
    """
    Simulates checking Jeff's availability on a specific date.

    Args:
        date_str (str): A date in 'YYYY-MM-DD' format.

    Returns:
        dict: A small JSON-like dictionary with availability info.
    """

    if not date_str:
        return {"status": "error", "message": "No date provided."}

    availability = FAKE_AVAILABILITY.get(date_str)

    if availability:
        return {
            "status": "completed",
            "message": f"On {date_str}, Jeff is {availability}.",
        }

    return {
        "status": "input_required",
        "message": f"He is not available on {date_str}. Please ask about another date.",
    }