"""Run personality eval cases against a trained model.

Each case specifies a prompt and expected keywords. A case passes if AT LEAST
ONE expected keyword appears in the response. This is loose on purpose —
we want to verify personality consistency, not exact string matching.
"""

from .cases import get_eval_cases


def run_eval(engine):
    """Run all eval cases and print a pass/fail report.

    Args:
        engine: a FrogInference instance (or anything with a .chat() method)

    Returns:
        True if all cases passed, False otherwise.
    """
    test_cases = get_eval_cases()
    num_passed, num_failed = 0, 0

    for case in test_cases:
        response = engine.chat([{"role": "user", "content": case["prompt"]}])
        response_lower = response.lower()

        # A case passes if any expected keyword appears in the response
        matched_keywords = [kw for kw in case["expect_keywords"] if kw in response_lower]
        passed = len(matched_keywords) > 0

        status = "PASS" if passed else "FAIL"
        if passed:
            num_passed += 1
        else:
            num_failed += 1

        print(f"  [{status}] {case['id']}")
        print(f"    Prompt:   {case['prompt']}")
        print(f"    Response: {response}")
        print(f"    Keywords: {matched_keywords} / {case['expect_keywords']}")
        print()

    total = num_passed + num_failed
    print(f"Results: {num_passed}/{total} passed, {num_failed}/{total} failed")
    return num_failed == 0
