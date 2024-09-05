import requests
import json


def main():
    url = "https://kiilikool.edupage.org/timetable/server/regulartt.js?__func=regularttGetData"

    payload = {
        "__args": [
            None,
            "47"
        ],
        "__gsh": "00000000"
    }
    response = requests.post(url, json=payload).json()

    tables = response["r"]["dbiAccessorRes"]["tables"]

    periods = tables[1]["data_rows"]
    periods_data = {}
    for period in periods:
        periods_data[period["id"]] = {
            "name": period["name"],
            "period": period["period"],
            "starttime": period["starttime"],
            "endtime": period["endtime"],
            "short": period["short"],
        }

    teachers = tables[14]["data_rows"]
    teacher_data = {}
    for teacher in teachers:
        teacher_data[teacher["id"]] = teacher["short"]

    classes = tables[12]["data_rows"]
    classes_data = {}
    for c in classes:
        classes_data[c["id"]] = {
            "name": c["name"],
            "teacher": teacher_data[c["teacherid"]]
        }

    subjects = tables[13]["data_rows"]
    subjects_data = {}
    for subject in subjects:
        subjects_data[subject["id"]] = {
            "name": subject["name"],
            "short": subject["short"]
        }

    weeksdefs = tables[5]["data_rows"]
    weeksdefs_data = {}
    for week in weeksdefs:
        weeksdefs_data[week["id"]] = {
            "name": week["name"],
            "short": week["short"]
        }

    weeks = tables[8]["data_rows"]
    weeks_data = {}
    for week in weeks:
        weeks_data[week["id"]] = {
            "name": week["name"],
            "short": week["short"]
        }

    daysdefs = tables[4]["data_rows"]
    daysdefs_data = {}
    for day in daysdefs:
        daysdefs_data[day["id"]] = {
            "name": day["name"],
            "short": day["short"]
        }

    days = tables[7]["data_rows"]
    days_data = {}
    for day in days:
        days_data[day["id"]] = {
            "name": day["name"],
            "short": day["short"]
        }

    termsdefs = tables[6]["data_rows"]
    termsdefs_data = {}
    for term in termsdefs:
        termsdefs_data[term["id"]] = {
            "name": term["name"],
            "short": term["short"]
        }

    terms = tables[9]["data_rows"]
    terms_data = {}
    for term in terms:
        terms_data[term["id"]] = {
            "name": term["name"],
            "short": term["short"]
        }

    groups = tables[15]["data_rows"]
    groups_data = {}
    for group in groups:
        groups_data[group["id"]] = {
            "name": group["name"],
            "class": classes_data[group["classid"]]["name"]
        }

    lessons = tables[18]["data_rows"]
    lessons_data = {}
    for lesson in lessons:
        lessons_data[lesson["id"]] = {
            "subject": subjects_data[lesson["subjectid"]]["name"],
            "teachers": lesson["teacherids"],
            "groups": lesson["groupids"],
            "termdef": termsdefs_data[lesson["termsdefid"]]["name"],
            "weekdef": weeksdefs_data[lesson["weeksdefid"]]["name"],
            "daydef": daysdefs_data[lesson["daysdefid"]]["name"],
        }

    lessons = tables[18]["data_rows"]
    lessons_data = {}
    for lesson in lessons:
        lessons_data[lesson["id"]] = {
            "subject": subjects_data[lesson["subjectid"]]["name"],
            "teachers": lesson["teacherids"],
            "groups": lesson["groupids"],
            "termdef": termsdefs_data[lesson["termsdefid"]]["name"],
            "weekdef": weeksdefs_data[lesson["weeksdefid"]]["name"],
            "daydef": daysdefs_data[lesson["daysdefid"]]["name"],
        }

    for t in classes_data:
        print(t)


if __name__ == "__main__":
    main()