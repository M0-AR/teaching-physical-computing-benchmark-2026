"""Ground-truth curriculum extracted + verified from edX + arm.com (Oct 2026).

Sources (live-verified 2026-10-03):
- edX professional certificate page: 4 courses, 42 weeks total, Intermediate, Self-paced
- Course 1: Intro to PBL, 10 wks, 1-2h/wk, 5977 learners enrolled (snapshot)
- Course 2: Practical application, 12 wks
- Course 3: Assessment of PBL, 10 wks
- Course 4: Soft skills/teamwork/wider curriculum, 10 wks
- arm.com/schools: 11+ micro:bit + Pico classroom projects, IPO worksheets, rubrics
- Price snapshot: $196 list, $176.40 with SUCCESS2026 (15% off, ends Oct 21 2026)
- Status: program currently unavailable for purchase; individual courses open (starts Oct 03, ends Jul 31 2027)
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Course:
    code: str
    title: str
    weeks: int
    hours_per_week: str
    modules: tuple

COURSES = (
    Course("C1", "Introduction to Project-Based Learning", 10, "1-2",
           ("Introduction", "Required hardware/software (micro:bit, Arduino, Raspberry Pi)",
            "Big picture of physical computing", "Orthodoxies",
            "Big picture of learning", "ASP approach",
            "Reflection on learning theories", "Reflection on teaching approaches",
            "Computational thinking", "Classroom investigation")),
    Course("C2", "Practical application and classroom strategies for PBL", 12, "1-2",
           ("Introduction", "Physical computing", "Project-based learning (PBL)",
            "Links to formal curriculum + formal assessments", "PBL toolkit",
            "PBL across ages", "Building resilience", "Group work in PBL",
            "Keep it super simple", "Practical considerations",
            "Classroom strategies", "Classroom investigation")),
    Course("C3", "Assessment of Project-Based Learning", 10, "1-2",
           ("Introduction", "Big picture of assessment", "Language of assessment",
            "Assessment of PBL", "Methods of assessment", "Question types",
            "Learning outcomes", "MCQs", "Open questioning + leading thinking",
            "Classroom investigation")),
    Course("C4", "Soft skills, teamwork and wider curriculum", 10, "1-2",
           ("Introduction", "Gracious professionalism", "Contexts are key",
            "Engaging parents + colleagues", "Keeping PBL extra-curricular",
            "Cross-curricular delivery", "Senior Leadership Team",
            "External partners", "Adapting/enhancing ASP PBL approach",
            "Classroom investigation")),
)

INSTRUCTORS = ("Robert Leeman (Arm)", "Dr John Woollard (Southampton)",
               "Gareth Edgell (Kingswood)", "Oli Howson (Open University)")

PROGRAM_TOTALS = {"courses": 4, "weeks": 42, "hours_per_week": "1-2",
                  "total_hours_low": 42, "total_hours_high": 84,
                  "level": "Intermediate", "pace": "Self-paced"}

def total_modules():
    return sum(len(c.modules) for c in COURSES)
