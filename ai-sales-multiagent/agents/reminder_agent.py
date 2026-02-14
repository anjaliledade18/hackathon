def create_reminder(qualification):

    if "Hot" in qualification:
        return "Reminder: Follow up in 1 day"
    elif "Warm" in qualification:
        return "Reminder: Follow up in 3 days"
    else:
        return "Reminder: Follow up in 7 days"
