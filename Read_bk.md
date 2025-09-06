# 🚀 SpaceX Launch Tracker

A Python application that tracks and analyzes SpaceX launches using their public API.

## Features
- Fetch launch, rocket, and launchpad data from SpaceX API v4.
- Local caching to minimize API calls.
- Filter launches by:
  - Date range
  - Rocket
  - Launch success/failure
  - Launch site
- Generate statistics:
  - Success rates by rocket
  - Launch counts per site
  - Monthly launch frequency
- Unit tests included.

## Setup

### 1. Clone repository
```bash
git clone https://github.com/yourusername/spacex-launch-tracker.git
cd spacex-launch-tracker
