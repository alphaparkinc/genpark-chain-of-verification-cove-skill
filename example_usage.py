from client import ChainOfVerification

def main():
    print("=== Testing Chain-of-Verification (CoVe) ===")
    cove = ChainOfVerification()

    claims = ["The Eiffel Tower was built in Paris in 1889", "It was built by Leonardo da Vinci"]
    plan = cove.generate_verification_plan(claims)
    print("Generated Verification Questions:")
    for item in plan:
        print(" ", item["verification_question"])

    # Simulate independent fact-checking
    verifications = [
        {"claim": claims[0], "is_valid": True, "correction": None},
        {"claim": claims[1], "is_valid": False, "correction": "It was designed by Gustave Eiffel's company"}
    ]
    res = cove.execute_and_revise("baseline", verifications)
    print("Revised synthesis:", res["revised_draft"])
    print("Corrections applied:", res["corrections_made"])
    assert len(res["corrections_made"]) == 1
    assert "Gustave Eiffel" in res["revised_draft"]
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
