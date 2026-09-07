from typing import Dict

# 🏸 Pretend this is Elon's Badminton Court Schedule
# "unknown" = available
# Anything else = booked/unavailable

COURT_SCHEDULE: Dict[str, Dict[str, str]] = {
    "2026-09-05": {
        "10:00": "unknown",
        "11:00": "unknown",
        "12:00": "unknown",
        "13:00": "unknown",
    },

    "2026-09-09": {
        "09:00": "unknown",
        "10:00": "unknown",
        "11:00": "unknown",
        "12:00": "unknown",
    },

    "2026-09-12": {
        "11:00": "unknown",
        "12:00": "unknown",
        "13:00": "unknown",
        "14:00": "unknown",
        "15:00": "unknown",
    },

    "2026-09-14": {
        "09:00": "unknown",
        "10:00": "unknown",
        "11:00": "unknown",
        "12:00": "unknown",
    },

    # ⭐ Best test date — Jeff + Mark + Court are all available
    "2026-09-18": {
        "09:00": "unknown",
        "10:00": "unknown",
        "11:00": "unknown",
        "12:00": "unknown",
        "13:00": "unknown",
        "14:00": "unknown",
        "15:00": "unknown",
        "16:00": "unknown",
    },

    "2026-09-20": {
        "10:00": "unknown",
        "11:00": "unknown",
        "12:00": "busy",
        "13:00": "unknown",
    },

    "2026-09-25": {
        "10:00": "unknown",
        "11:00": "unknown",
        "12:00": "unknown",
        "13:00": "unknown",
    },

    "2026-09-27": {
        "12:00": "unknown",
        "13:00": "unknown",
        "14:00": "unknown",
        "15:00": "unknown",
    },
}


def generate_court_schedule():
    """Dummy: Pretend to initialize the court schedule."""
    print("Dummy September 2026 court schedule initialized.")


# Initialize dummy schedule
generate_court_schedule()


def list_court_availabilities(date: str) -> dict:
    """
    List available and booked time slots for a given date.
    """

    if date not in COURT_SCHEDULE:
        return {
            "status": "error",
            "message": f"No schedule found for {date}. Try another one please.",
            "schedule": {},
        }

    daily_schedule = COURT_SCHEDULE[date]

    available_slots = [
        time for time, status in daily_schedule.items()
        if status == "unknown"
    ]

    booked_slots = {
        time: status
        for time, status in daily_schedule.items()
        if status != "unknown"
    }

    return {
        "status": "success",
        "message": f"Schedule for {date}.",
        "available_slots": available_slots,
        "booked_slots": booked_slots,
    }


def book_badminton_court(
    date: str,
    start_time: str,
    end_time: str,
    reservation_name: str
) -> dict:
    """
    Book a badminton court for the requested time slot.

    Only one-hour slots are supported.
    """

    if date not in COURT_SCHEDULE:
        return {
            "status": "error",
            "message": f"No schedule for {date}."
        }

    if start_time not in COURT_SCHEDULE[date]:
        return {
            "status": "error",
            "message": f"Invalid time for {date}."
        }

    if COURT_SCHEDULE[date][start_time] != "unknown":
        return {
            "status": "error",
            "message": (
                f"Slot {start_time} on {date} "
                f"already booked by {COURT_SCHEDULE[date][start_time]}."
            ),
        }

    # Book the slot
    COURT_SCHEDULE[date][start_time] = reservation_name

    return {
        "status": "success",
        "message": (
            f"Booked badminton court on {date} "
            f"from {start_time} to {end_time} "
            f"for {reservation_name}."
        ),
    }