# Find out how many reports are safe
  # 2 things must be true
    # numbers in list are either increasing or decreasing
    # Numbers incease at most by 3


import numpy as np

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
  safe = any(changes) < 1 or any(changes > 3)
  return safe


def main():
  safe_reports = 0
  
  reports = get_reports('example.txt')
  for report in reports:
    if inc_or_dec(report) == True:
      if is_level_change_safe(report) == True:
        safe_reports += 1
  print(safe_reports)

main()