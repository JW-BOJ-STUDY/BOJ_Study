import sys

testCase = int(sys.stdin.readline().strip())

output = []

for i in range(testCase):
    applicant = [list(map(int,sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline().strip()))]
    sApplicant = sorted(applicant)
    hired = []
    hired.append(sApplicant[0][1])
    for appli in sApplicant:
        if(hired[-1] > appli[1]):
            hired.append(appli[1])
    output.append(len(hired))
    
for i in output:
    sys.stdout.write(str(i)+ "\n")
    
    