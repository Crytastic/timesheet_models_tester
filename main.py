from config import TEMPERATURE_VALUES
from timesheet_test import transcribe_audio, transform_to_timesheet, evaluate
from annotations import TEST_CASES


def run_test_case(index: int, case: dict, temperature: float, output_file) -> float:
    print(f"\n--- Running Test Case #{index + 1} ---", file=output_file)
    print("Transcribing audio...", file=output_file)
    transcribed_text = transcribe_audio(case["audio_path"])
    print("Transcription:", transcribed_text, file=output_file)

    print("Generating timesheet format...", file=output_file)
    predicted = transform_to_timesheet(transcribed_text, temperature=temperature)
    print("Predicted:", predicted, file=output_file)
    print("Expected:", case["expected"], file=output_file)

    print("Evaluating...", file=output_file)
    result = evaluate(predicted, case["expected"])
    for field, score in result["field_scores"].items():
        print(f"{field}: {score * 100:.2f}%", file=output_file)
    print(f"Overall Accuracy: {result['overall_score'] * 100:.2f}%", file=output_file)

    return result['overall_score']


def main():
    for temp in TEMPERATURE_VALUES:
        filename = f"results/results_temp_{temp:.2f}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            print(f"Running tests at temperature {temp:.2f}...\n", file=f)

            total_score = 0
            num_cases = len(TEST_CASES)

            for i, case in enumerate(TEST_CASES):
                score = run_test_case(i, case, temp, output_file=f)
                total_score += score

            average_score = total_score / num_cases
            print(f"\n=== Summary for Temperature {temp:.2f} ===", file=f)
            print(f"Tested {num_cases} cases", file=f)
            print(f"Average Overall Accuracy: {average_score * 100:.2f}%", file=f)

        print(f"Finished temperature {temp:.2f}, results saved to {filename}")


if __name__ == "__main__":
    main()
