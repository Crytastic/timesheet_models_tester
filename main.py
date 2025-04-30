from timesheet_test import transcribe_audio, transform_to_timesheet, evaluate


def main():
    audio_path = "assets/test.wav"
    expected_output = [
        "AGORA plus a.s.",
        "Development",
        "Alpha",
        "04:00",
        "správa serverů"
    ]

    print("Transcribing audio...")
    transcribed_text = transcribe_audio(audio_path)
    print("Transcription:", transcribed_text)

    print("Generating timesheet format...")
    predicted = transform_to_timesheet(transcribed_text)
    print("Predicted:", predicted)
    print("Expected:", expected_output)

    print("Evaluating...")
    result = evaluate(predicted, expected_output)
    for field, score in result["field_scores"].items():
        print(f"{field}: {score * 100:.2f}%")
    print(f"Overall Accuracy: {result['overall_score'] * 100:.2f}%")


if __name__ == "__main__":
    main()
