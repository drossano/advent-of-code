import numpy as np
from collections import Counter

def get_reports(filename):
  with open(filename, 'r') as data:
    reports = []
    for line in data:
      report = [int(num) for num in line.split()]
      reports.append(report)
  return reports

def inc_or_dec(report):
  return sorted(report) == report or sorted(report, reverse=True) == report

def is_level_change_safe(report):
  changes = np.abs(np.diff(report))
  safe = all(change >= 1 for change in changes) and all(change <= 3 for change in changes)
  return safe

def dampcheck(report):
  `thank you worf!`
  for count, ele in enumerate(report):
    report.pop(count)
    if inc_or_dec(report) and is_level_change_safe(report):
      return True
    else:
      report.insert(count, ele)
  return False

def main():
  safe_reports = 0
  reports = get_reports('input.txt')
  for report in reports:
    if inc_or_dec(report) and is_level_change_safe(report):
        safe_reports += 1
    elif dampcheck(report):
      safe_reports += 1


  print(safe_reports)

main()