# ai personality matrix

รายละเอียด API สำหรับโมดูล ai personality matrix

## วิธีใช้งาน
# AI Personality Matrix

## Overview
The AI Personality Matrix module provides a framework for generating, managing, and evolving AI-driven personality profiles. It enables dynamic personality modeling for virtual agents, chatbots, and digital entities.

## Features
- Dynamic personality generation
- Profile evolution and adaptation
- Integration with other NaMo modules
- REST API for profile management

## API Endpoints
### Create Personality Profile
```bash
curl -X POST http://localhost:8000/api/profile -d '{"traits": ["empathy", "logic"]}'
```
### Get Personality Profile
```bash
curl http://localhost:8000/api/profile/{id}
```

## Folder Structure
```
ai-personality-matrix/
├── main.py
├── README.md
├── requirements.txt
└── docs/
    ├── USAGE.md
    ├── SECURITY.md
    └── flow.md
```

## Installation
```bash
pip install -r requirements.txt
```

## Configuration
Edit `config.yaml` to customize personality traits and API settings.

## License
MIT

## License
ดูรายละเอียดใน [LICENSE](LICENSE)
