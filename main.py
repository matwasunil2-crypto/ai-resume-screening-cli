from database import load_data, save_data
from ai_engine import calculate_score, classify
from auth import login, register

current_user = None


def safe_int_input(msg):
    try:
        return int(input(msg))
    except:
        print("❌ Invalid number!")
        return None


def add_resume():
    data = load_data()

    name = input("Candidate Name: ").strip()
    skills = input("Skills (comma): ").split(",")

    exp = safe_int_input("Experience (years): ")
    if exp is None:
        return

    data.append({
        "name": name,
        "skills": skills,
        "experience": exp
    })

    save_data(data)
    print("✅ Resume added!")


def view_resumes():
    data = load_data()

    if not data:
        print("⚠️ No resumes found")
        return

    for i, r in enumerate(data, 1):
        print(f"{i}. {r['name']} | {r['skills']} | Exp: {r['experience']}")


def edit_resume():
    data = load_data()
    view_resumes()

    idx = safe_int_input("Enter number to edit: ")
    if idx is None:
        return

    idx -= 1

    if 0 <= idx < len(data):
        data[idx]["name"] = input("New name: ")
        data[idx]["skills"] = input("New skills: ").split(",")
        exp = safe_int_input("New experience: ")
        if exp is None:
            return
        data[idx]["experience"] = exp

        save_data(data)
        print("✅ Updated!")
    else:
        print("❌ Invalid choice")


def delete_resume():
    data = load_data()
    view_resumes()

    idx = safe_int_input("Enter number to delete: ")
    if idx is None:
        return

    idx -= 1

    if 0 <= idx < len(data):
        data.pop(idx)
        save_data(data)
        print("🗑️ Deleted!")
    else:
        print("❌ Invalid choice")


def analyze():
    data = load_data()

    if not data:
        print("⚠️ No data to analyze")
        return

    job_skills = input("Job skills: ").split(",")

    results = []

    for r in data:
        score = calculate_score(r["skills"], job_skills, r["experience"])
        status = classify(score)

        results.append({
            "name": r["name"],
            "score": score,
            "status": status
        })

    results = sorted(results, key=lambda x: x["score"], reverse=True)

    print("\n🏆 Ranking:\n")
    for i, r in enumerate(results, 1):
        print(f"{i}. {r['name']} → {r['score']}% ({r['status']})")


def dashboard():
    global current_user

    while True:
        print(f"\n👤 Logged in as: {current_user}")
        print("""
1. Add Resume
2. View Resumes
3. Edit Resume
4. Delete Resume
5. Analyze & Rank
6. Logout
""")

        ch = input("Choice: ")

        if ch == "1":
            add_resume()
        elif ch == "2":
            view_resumes()
        elif ch == "3":
            edit_resume()
        elif ch == "4":
            delete_resume()
        elif ch == "5":
            analyze()
        elif ch == "6":
            print("👋 Logged out")
            break
        else:
            print("❌ Invalid choice")


def main():
    global current_user

    while True:
        print("""
===== AI Resume CLI =====
1. Login
2. Register
3. Exit
""")

        ch = input("Choice: ")

        if ch == "1":
            user = login()
            if user:
                current_user = user
                dashboard()
        elif ch == "2":
            register()
        elif ch == "3":
            print("Goodbye 👋")
            break
        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()