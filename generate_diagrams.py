import base64
import json
import subprocess
import os

def download_mermaid(name, mermaid_code):
    # Mermaid.ink format: https://mermaid.ink/img/<base64>
    # Base64 encoding of the mermaid code
    
    # Create the state object expected by mermaid.ink (optional, but good for config)
    # Simple encoding of the string works for basic graphs
    
    # We need to use 'pako' compression for long URLs usually, but simple base64 works for short ones.
    # However, mermaid.ink supports standard base64 of the code directly.
    
    encoded_string = base64.urlsafe_b64encode(mermaid_code.encode('utf-8')).decode('utf-8')
    url = f"https://mermaid.ink/img/{encoded_string}"
    
    print(f"Downloading {name} from {url}...")
    try:
        subprocess.run(["curl", "-o", f"{name}.png", url], check=True)
        print(f"Saved {name}.png")
    except subprocess.CalledProcessError as e:
        print(f"Failed to download {name}: {e}")

diagrams = {
    "dfd_level_0": """graph LR
    S[Student] -- Login/Request --> T((TARMS System))
    F[Faculty] -- Approval/Status --> T
    A[Admin] -- Manage Users/Rooms --> T
    T -- Notifications --> S
    T -- Reports --> A""",

    "dfd_level_1": """graph TD
    S[Student] -->|Login| P1(Authentication)
    P1 -->|Valid| P2(Check Availability)
    P2 -->|Available| P3(Submit Request)
    P3 -->|Request| D1[(Booking DB)]
    F[Faculty] -->|Login| P1
    P1 -->|Valid| P4(Review Request)
    P4 -->|Approve/Reject| P5(Update Status)
    P5 --> D1
    P5 -->|Notify| S""",

    "class_diagram": """classDiagram
    class User {
        +String name
        +String email
        +String password
        +login()
        +logout()
    }
    class Student {
        +String rollNo
        +bookRoom()
        +viewStatus()
    }
    class Faculty {
        +String dept
        +approveRequest()
        +rejectRequest()
    }
    class Room {
        +String roomId
        +String capacity
        +checkAvailability()
    }
    class Booking {
        +Date date
        +String purpose
        +String status
    }
    User <|-- Student
    User <|-- Faculty
    Student "1" -- "*" Booking : makes
    Faculty "1" -- "*" Booking : approves
    Booking "*" -- "1" Room : for""",

    "sequence_login": """sequenceDiagram
    participant S as Student
    participant Sys as System
    participant DB as Database
    S->>Sys: Enter Credentials
    Sys->>DB: Validate User
    DB-->>Sys: User Found
    Sys-->>S: Login Success
    S->>Sys: Request Dashboard""",

    "sequence_booking": """sequenceDiagram
    participant S as Student
    participant Sys as System
    participant F as Faculty
    S->>Sys: Search Room
    Sys-->>S: List Available Rooms
    S->>Sys: Submit Booking Request
    Sys->>F: Notify New Request
    F->>Sys: Approve Request
    Sys-->>S: Notify Approval""",
    
    "activity_booking": """graph TD
    Start((Start)) --> Login[Login]
    Login --> Search[Search Room]
    Search --> Select[Select Room]
    Select --> Fill[Fill Booking Form]
    Fill --> Submit[Submit Request]
    Submit --> Review{Faculty Review}
    Review -- Approve --> Update[Update Status: Approved]
    Review -- Reject --> Reject[Update Status: Rejected]
    Update --> Notify[Notify Student]
    Reject --> Notify
    Notify --> End((End))""",
    
    "use_case_diagram": """graph TD
    S[Student] --> UC1(Login)
    S --> UC2(Book Room)
    S --> UC3(View Status)
    F[Faculty] --> UC1
    F --> UC4(Approve Request)
    F --> UC5(View Reports)
    A[Admin] --> UC6(Manage Users)
    A --> UC7(Manage Rooms)""",

    "swimlane_diagram": """graph TD
    subgraph Student
        St1[Login] --> St2[Search Room]
        St2 --> St3[Fill Form]
        St3 --> St4[Submit Request]
    end
    subgraph System
        St4 --> Sys1[Validate Data]
        Sys1 --> Sys2[Save Request]
        Sys2 --> Sys3[Notify Faculty]
        Sys4[Update Status] --> Sys5[Notify Student]
    end
    subgraph Faculty
        Sys3 --> Fac1[View Request]
        Fac1 --> Fac2{Approve?}
        Fac2 -- Yes --> Sys4
        Fac2 -- No --> Sys4
    end""",

    "collaboration_diagram": """graph LR
    S[Student] -- 1. Login --> Sys[System]
    S -- 2. Search --> Sys
    Sys -- 3. Check Availability --> DB[(Database)]
    DB -- 4. Return Status --> Sys
    Sys -- 5. Display Rooms --> S
    S -- 6. Book --> Sys
    Sys -- 7. Notify --> F[Faculty]
    F -- 8. Approve --> Sys
    Sys -- 9. Confirm --> S""",

    "state_chart_diagram": """stateDiagram-v2
    [*] --> Idle
    Idle --> Searching : Search Room
    Searching --> Selected : Select Room
    Selected --> Booking : Fill Form
    Booking --> Review : Submit
    Review --> Approved : Approve
    Review --> Rejected : Reject
    Approved --> [*]
    Rejected --> [*]""",

    "component_diagram": """graph TD
    subgraph Client
        Browser[Web Browser]
    end
    subgraph Server
        Auth[Auth Service]
        Booking[Booking Service]
        RoomMgr[Room Manager]
    end
    subgraph Data
        DB[(MongoDB)]
    end
    Browser --> Auth
    Browser --> Booking
    Browser --> RoomMgr
    Auth --> DB
    Booking --> DB
    RoomMgr --> DB""",

    "deployment_diagram": """graph TD
    node1(Student PC) -- HTTP --> node2(Web Server)
    node3(Faculty PC) -- HTTP --> node2
    node2 -- TCP/IP --> node4(Database Server)
    node2 -- SMTP --> node5(Email Server)""",

    "dfd_level_2": """graph TD
    S[Student] -->|1. Select Room| P1(Check Availability)
    P1 -->|2. Room Free| P2(Display Form)
    P1 -->|2. Room Busy| P3(Show Error)
    P2 -->|3. Fill Details| P4(Validate Input)
    P4 -->|4. Valid| P5(Create Booking Record)
    P5 -->|5. Store| DB[(Booking DB)]""",

    "sequence_add_booking": """sequenceDiagram
    participant S as Student
    participant Sys as System
    participant DB as Database
    S->>Sys: Click Book Room
    Sys-->>S: Show Booking Form
    S->>Sys: Submit Details
    Sys->>DB: Save Booking Request
    DB-->>Sys: Confirmation
    Sys-->>S: Show Success Message""",

    "sequence_view_room": """sequenceDiagram
    participant U as User
    participant Sys as System
    participant DB as Database
    U->>Sys: Select Room Category
    Sys->>DB: Fetch Rooms
    DB-->>Sys: Return Room List
    Sys-->>U: Display Rooms""",

    "collab_add_booking": """graph LR
    S[Student] -- 1. Request Booking --> Sys[System]
    Sys -- 2. Validate --> Sys
    Sys -- 3. Save --> DB[(Database)]
    DB -- 4. Confirm --> Sys
    Sys -- 5. Notify --> S""",

    "collab_view_room": """graph LR
    U[User] -- 1. View Rooms --> Sys[System]
    Sys -- 2. Query --> DB[(Database)]
    DB -- 3. Return Data --> Sys
    Sys -- 4. Show List --> U""",

    "state_unregistered": """stateDiagram-v2
    [*] --> Guest
    Guest --> Registering : Click Sign Up
    Registering --> Registered : Submit Valid Data
    Registering --> Guest : Cancel
    Registered --> [*]""",

    "state_booking": """stateDiagram-v2
    [*] --> Pending
    Pending --> Approved : Faculty Approve
    Pending --> Rejected : Faculty Reject
    Approved --> [*]
    Rejected --> [*]"""
}

if __name__ == "__main__":
    for name, code in diagrams.items():
        download_mermaid(name, code)
