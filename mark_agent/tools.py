# Step1: Agent & Tool

# 🗓️ Pretend this is Mark's Calendar
FAKE_AVAILABILITY = {
    "2026-09-01": "Busy all day",
    "2026-09-02": "Available from 11:00 AM to 03:00 PM",
    "2026-09-03": "Available from 11:00 AM to 03:00 PM",
    "2026-09-04": "Busy all day",
    "2026-09-05": "Available all day",
    "2026-09-06": "Available from 12:00 PM to 04:00 PM",
    "2026-09-07": "Busy all day",
    "2026-09-08": "Available from 11:00 AM to 03:00 PM",
    "2026-09-09": "Available all day",
    "2026-09-10": "Busy all day",
    "2026-09-11": "Available from 11:00 AM to 03:00 PM",
    "2026-09-12": "Available from 12:00 PM to 04:00 PM",
    "2026-09-13": "Busy all day",
    "2026-09-14": "Available all day",
    "2026-09-15": "Available from 11:00 AM to 03:00 PM",
    "2026-09-16": "Busy all day",
    "2026-09-17": "Available from 12:00 PM to 04:00 PM",
    "2026-09-18": "Available all day",
    "2026-09-19": "Busy all day",
    "2026-09-20": "Available from 11:00 AM to 03:00 PM",
    "2026-09-21": "Available from 12:00 PM to 04:00 PM",
    "2026-09-22": "Busy all day",
    "2026-09-23": "Available all day",
    "2026-09-24": "Available from 11:00 AM to 03:00 PM",
    "2026-09-25": "Busy all day",
    "2026-09-26": "Available from 12:00 PM to 04:00 PM",
    "2026-09-27": "Available all day",
    "2026-09-28": "Busy all day",
    "2026-09-29": "Available from 11:00 AM to 03:00 PM",
    "2026-09-30": "Available from 12:00 PM to 04:00 PM",
}

def get_availability(date_str: str) -> dict[str, str]:
    """
    Simulates checking Mark's availability on a specific date.

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

from crewai.tools import BaseTool


class AvailabilityTool(BaseTool):
    name: str = "Calendar Availability Checker"
    description: str = "Checks Mark's availability for a given date."

    def _run(self, date: str) -> str:
        return get_availability(date)["message"]