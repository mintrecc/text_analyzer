import json
import csv


def export_report_json(report):
    with open('reportJS.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=4)

def export_report_csv(report):
    if isinstance(report, dict):
        report = [report]

    columns = list(report[0].keys())
    
    with open('reportCSV', 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=columns, delimiter=';')
        writer.writeheader()
        writer.writerows(report)

