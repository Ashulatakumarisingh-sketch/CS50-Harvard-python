# AstroSpace Mobile App

#### Video Demonstration: https://youtu.be/5pdkVsekfIU

#### Project Overview
AstroSpace is an interactive mobile application prototype designed for astronomy enthusiasts. Built using Python and the modern Flet engine, the application features a responsive multi-card layout tailored for mobile displays. The project strictly follows a clean architecture by isolating all core networking tasks inside a dedicated logic module, allowing independent interface rendering and bulletproof execution in distributed host environments.

#### Implemented Features
- **Astronomy Picture of the Day:** Synchronizes with planetary datasets to surface trending cosmic highlights and featured structural names from deep space surveys.
- **Mars Curiosity Tracker:** Pings exploration logs to track the operations of active robotic surface equipment deployed inside Gale Crater.
- **ISS Live Telemetry Station:** Filters continuous orbital parameters, displaying accurate numerical telemetry records (Latitude and Longitude) of the International Space Station.

#### File Architecture
1. **`project.py` (Core Logic Framework):** Houses standalone, testable backend components that fetch data payloads, intercept timeout parameters, and clean raw data packets securely.
2. **`main.py` (UI Presentation Layer):** Governs the interface architecture using reactive Flet controls. It packs containers, layout alignments, and structural design configurations optimized for standard mobile dimensions.
3. **`test_project.py` (Validation Engine):** Implements rigorous automated unit testing through the `pytest` platform to assert datatypes and data structures returned by the core logic framework.

#### Installation and Running Guide
Before launching the application interface, provision your environment with the following command:
```bash
pip install flet requests pytest
```

To run the automated diagnostic unit test blocks:
```bash
pytest test_project.py
```

To initiate the live reactive mobile view simulation:
```bash
python main.py
```
