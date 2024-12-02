# Find out how many reports are safe
  # 2 things must be true
    # numbers in list are either increasing or decreasing
    # Numbers incease at most by 3

def get_reports(filename):
  with open(filename, 'r') as data:
    reports = []
    for line in data:
      report = [int(num) for num in line.split()]
      reports.append(report)
  return reports

def main():
  safe_reports = 0

  reports = get_reports('example.txt')
  print(reports)

main()