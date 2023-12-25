# Calculate the weekly average activity for each email domain.
query_extract_weekly_activity = """
    SELECT
        user.email AS email_domain,
        WEEK(STR_TO_DATE(space_attendee.joinDate, '%m/%d/%Y %H:%i')) AS week_number,
        COUNT(space_attendee.spaceSessionId) AS weekly_activity
    FROM user
    JOIN space_attendee ON user.ID = space_attendee.userId
    GROUP BY email_domain, week_number;
"""

# Calculate the total activity for each email domain.
query_total_activity = """
    SELECT
        user.email AS email_domain,
        COUNT(spaceSessionId) AS total_activity
    FROM user
    JOIN space_attendee ON user.ID = space_attendee.userId
    GROUP BY email_domain;
"""

# Filter out invalid sessions that have less than 2 users and a duration of less than 5 minutes.
query_filtering_session = """
    SELECT *
    FROM space_session_info
    WHERE number_of_participants >= 2 AND duration >= 5;
"""