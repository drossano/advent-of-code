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

def inc_or_dec_dampener(report):
  changes = np.diff(report)
  negs = 0
  pos = 0
  for i in range(len(changes)):
    if changes[i] > 0:
      pos += 1
    else:
      negs += 1
  if pos > negs:
      if changes[-1] < 0:
        del report[-1]
        return report
      else:
        for i in range(len(changes)):
          if changes[i] < 0:
              del report[i]
              return report
  else:
    if changes[-1] > 0:
      del report[-1]
      return report
    for i in range(len(changes)):
      if changes[i] > 0:
          del report[i]
          return report



def is_level_change_safe(report):
  changes = np.abs(np.diff(report))
  safe = all(change >= 1 for change in changes) and all(change <= 3 for change in changes)
  return safe

def change_dampener(report):
  changes = np.abs(np.diff(report))
  if changes[0] < 1 or changes [0]> 3:
    del report[0]
    return report
  elif changes[-1] < 1 or changes[-1] > 3:
    del report[-1]
    return report
  else:
    dupes = [k for k, v in Counter(report).items() if v >1]
    if len(dupes) > 1 or not dupes:
      return  False
    else:
      report.remove(dupes[0])
      return report

def main():
  safe_reports = 0
  safe_report_list = []
  reports = get_reports('example.txt')
  for report in reports:
    if inc_or_dec(report) == True:
      if is_level_change_safe(report) == True:
        safe_reports += 1
        safe_report_list.append(report)
      else:
        dampened_report = change_dampener(report)
        if dampened_report != False:
          if is_level_change_safe(dampened_report) == True:
            safe_reports +=1
            safe_report_list.append(report)
    else:
      dampened_report = inc_or_dec_dampener(report)
      if inc_or_dec(dampened_report) == True:
        if is_level_change_safe(dampened_report) == True:
          safe_reports += 1
          safe_report_list.append(report)

  print(safe_reports)
  print(safe_report_list)

main()

#part 2
# if inc or dec fails
# inc or dec passes
  # change fails
  # should only matter for matches?
  # just remove dupes???