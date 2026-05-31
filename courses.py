# ===============================
# STREAM -> COURSE -> SPECIALIZATION
# ===============================

COURSES = {

    "Science": {

        "Engineering": [
            "Computer Science",
            "AI & ML",
            "Data Science",
            "Cyber Security",
            "Information Technology",
            "ECE",
            "EEE",
            "Mechanical",
            "Civil",
            "Biotechnology",
            "Chemical",
            "Robotics",
            "Mechatronics",
            "Aerospace",
            "Automobile",
            "Production Engineering",
            "Industrial Engineering",
            "Marine Engineering"
        ],

        "Medical": [
            "MBBS",
            "BDS",
            "BAMS",
            "BHMS",
            "BSc Nursing",
            "Pharm D",
            "B Pharmacy",
            "Physiotherapy",
            "Radiology",
            "Optometry",
            "Medical Laboratory Technology"
        ],

        "Science": [
            "Physics",
            "Chemistry",
            "Mathematics",
            "Statistics",
            "Computer Science",
            "Data Analytics",
            "Biotechnology",
            "Microbiology",
            "Botany",
            "Zoology",
            "Forensic Science",
            "Agriculture"
        ]
    },

    "Commerce": {

        "Commerce & Management": [
            "BCom",
            "Accounting",
            "Finance",
            "Taxation",
            "Banking",
            "Insurance",
            "BBA",
            "MBA",
            "CA",
            "CMA",
            "CS",
            "Economics",
            "Business Analytics",
            "Digital Marketing"
        ]
    },

    "Humanities": {

        "Arts & Education": [
            "BA English",
            "BA History",
            "BA Political Science",
            "BA Sociology",
            "BA Psychology",
            "Journalism",
            "Mass Communication",
            "Social Work",
            "BEd",
            "MEd",
            "Public Administration"
        ]
    },

    "Vocational": {

        "Professional Skills": [
            "Graphic Design",
            "UI/UX Design",
            "Animation",
            "Photography",
            "Video Editing",
            "Fashion Design",
            "Hotel Management",
            "Culinary Arts",
            "Travel & Tourism",
            "Event Management"
        ]
    }
}


# ===============================
# 📅 YEARS CONFIGURATION
# ===============================

YEARS = [
    "1st Year",
    "2nd Year",
    "3rd Year",
    "4th Year",
    "5th Year",
    "Internship Year"
]


# ===============================
# 🔧 HELPER FUNCTIONS (UPGRADE)
# ===============================

def get_streams():
    return list(COURSES.keys())


def get_courses(stream):
    return list(COURSES.get(stream, {}).keys())


def get_specializations(stream, course):
    return COURSES.get(stream, {}).get(course, [])


def is_valid_path(stream, course, specialization):
    return specialization in get_specializations(stream, course)