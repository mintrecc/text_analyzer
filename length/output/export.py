import json


def export_report_json(report):
    with open('reportJS.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=4)



