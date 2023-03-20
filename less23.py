def test_input_text(expected_result, actual_result):
    assert (expected_result == actual_result),f"expected {expected_result}, got {actual_result}"

def test_substring(full_string, substring):
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"