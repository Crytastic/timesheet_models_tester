from timesheet_test import transcribe_audio, transform_to_timesheet, evaluate
from annotations import TEST_CASES


def run_test_case(index: int, case: dict):
    print(f"\n--- Running Test Case #{index + 1} ---")
    print("Transcribing audio...")
    transcribed_text = transcribe_audio(case["audio_path"])
    print("Transcription:", transcribed_text)

    print("Generating timesheet format...")
    predicted = transform_to_timesheet(transcribed_text)
    print("Predicted:", predicted)
    print("Expected:", case["expected"])

    print("Evaluating...")
    result = evaluate(predicted, case["expected"])
    for field, score in result["field_scores"].items():
        print(f"{field}: {score * 100:.2f}%")
    print(f"Overall Accuracy: {result['overall_score'] * 100:.2f}%")


def main():
    total_score = 0
    num_cases = len(TEST_CASES)

    for i, case in enumerate(TEST_CASES):
        run_test_case(i, case)
        transcribed_text = transcribe_audio(case["audio_path"])
        predicted = transform_to_timesheet(transcribed_text)
        result = evaluate(predicted, case["expected"])
        total_score += result['overall_score']

    average_score = total_score / num_cases
    print(f"\n=== Summary ===")
    print(f"Tested {num_cases} cases")
    print(f"Average Overall Accuracy: {average_score * 100:.2f}%")


if __name__ == "__main__":
    main()
