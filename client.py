class ChainOfVerification:
    """
    Chain-of-Verification (CoVe) (Dhuliawala et al.).
    Mitigates hallucination via 4 steps:
    1. Baseline response generation
    2. Fact-checking verification question generation
    3. Independent verification execution (unbiased)
    4. Calibrated final response synthesis
    """
    def generate_verification_plan(self, draft_claims):
        plan = []
        for claim in draft_claims:
            plan.append({
                "claim": claim,
                "verification_question": f"Is it verifiably true that '{claim}'?",
                "fact_check_source": "oracle_kb"
            })
        return plan

    def execute_and_revise(self, draft, verification_results):
        corrections = []
        revised_claims = []
        for v in verification_results:
            if not v["is_valid"]:
                corrections.append(f"Corrected: {v['claim']} -> {v['correction']}")
                revised_claims.append(v['correction'])
            else:
                revised_claims.append(v['claim'])
        return {
            "revised_draft": "; ".join(revised_claims),
            "corrections_made": corrections
        }
