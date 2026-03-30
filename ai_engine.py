def calculate_score(skills, job_skills, exp):
    skills = [s.strip().lower() for s in skills if s.strip()]
    job_skills = [j.strip().lower() for j in job_skills if j.strip()]

    matched = len(set(skills).intersection(set(job_skills)))

    skill_score = (matched / len(job_skills)) * 100 if job_skills else 0

    # Experience scoring
    if exp >= 5:
        exp_score = 100
    elif exp >= 2:
        exp_score = 70
    else:
        exp_score = 40

    final_score = (0.7 * skill_score) + (0.3 * exp_score)
    return round(final_score, 2)


def classify(score):
    if score >= 75:
        return "Selected"
    elif score >= 50:
        return "Consider"
    else:
        return "Rejected"