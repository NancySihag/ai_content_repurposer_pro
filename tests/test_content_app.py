from content_app import build_prompts


def test_build_prompts_returns_five_prompts():
    prompts = build_prompts(
        "Python is useful for automation.",
        "LinkedIn",
        "Professional",
        200
    )

    assert len(prompts) == 5


def test_build_prompts_uses_selected_options():
    prompts = build_prompts(
        "Python is useful for automation.",
        "LinkedIn",
        "Professional",
        200
    )

    assert all("LinkedIn" in prompt for prompt in prompts)
    assert all("Professional" in prompt for prompt in prompts)
