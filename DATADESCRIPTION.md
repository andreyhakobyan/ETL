`space_attendee` Table: [space_attendee.csv](./data/space_attendee.csv)  
This table appears to represent information about attendees in various space sessions.  
Columns:

* ID: A unique identifier for each record in this table.
* spaceSessionId: A reference to the space session associated with this attendee.
* userId: A reference to the user who is attending the space session.
* createdAt: A timestamp indicating when the attendee record was created.
* updatedAt: A timestamp indicating when the attendee record was last updated.
* joinDate: A text field that likely stores the date when the attendee joined the session.
* leftDate: A text field that likely stores the date when the attendee left the session.
* parentSpaceSessionId: A reference to another space session (possibly a parent session).
* openSpaceUser: A reference to a user related to the open space.
Relationships:

`spaceSessionId` and `userId` likely serve as foreign keys linking this table to the `space_session_info` and `user` tables, respectively.

`space_session_info` Table: [space_session_info.csv](./data/space_session_info.csv)  
This table seems to store information about different space sessions.  
Columns:

* ID: A unique identifier for each record in this table.
* spaceId: A reference to the space associated with this session.
* duration: The duration of the session in some numeric format (e.g., seconds or minutes).
* number_of_participants: The count of participants in the session.
* start_date: A text field storing the start date and time of the session.
* end_date: A text field storing the end date and time of the session.
* createdAt: A timestamp indicating when the session record was created.
* updatedAt: A timestamp indicating when the session record was last updated.
* roomSid: A text field, possibly related to session details.  

Relationships:  
`spaceId` likely serves as a foreign key linking this table to the space table (not provided).

`user` Table:  [user.csv](./data/user.csv)  
This table appears to store user-related information.  
Columns:

* ID: A unique identifier for each user.
* firstName: The user's first name.
* lastName: The user's last name.
* name: The user's full name.
* email: The user's email address.
Various other fields storing user-related data like timestamps, pictures, status, and more.  

Relationships:  
There are several fields that could potentially serve as foreign keys or references to other tables in database, but their specific relationships would depend on data model and application logic.