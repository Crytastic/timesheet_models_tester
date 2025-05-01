TEST_CASES = [
    {
        "audio_path": "assets/agora_server.wav",
        "expected": [
            "AGORA plus a.s.",
            "Infrastructure, Maintenance",
            "Infrastructure + Maintenance",
            "04:00",
            "správa serverů"
        ]
    },
    {
        "audio_path": "assets/agora_database.webm",
        "expected": [
            "AGORA plus a.s.",
            "Infrastructure, Maintenance",
            "Storage",
            "00:30",
            "správa databází a nesrovnalostí"
        ]
    },
    {
        "audio_path": "assets/bdo.webm",
        "expected": [
            "BDO Valuation s.r.o.",
            "Infrastructure, Maintenance",
            "Storage",
            "00:00",
            "maintenance firewallu"
        ]
    },
    {
        "audio_path": "assets/devbalance.webm",
        "expected": [
            "DevBalance",
            "Development",
            "ML/AI app dev",
            "05:20",
            "vývoj aplikace umělé inteligence"
        ]
    },
    {
        "audio_path": "assets/emko.webm",
        "expected": [
            "Emko",
            "Infrastructure Networks",
            "Generic",
            "01:00",
            "příprava konfigurace, migrace firewallu"
        ]
    },
    {
        "audio_path": "assets/fastercz.webm",
        "expected": [
            "FasterCZ",
            "Development",
            "Generic",
            "03:00",
            "příprava znaleckého posudku"
        ]
    }
]
