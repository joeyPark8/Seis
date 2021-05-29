students = []

m2 = '''1. 학번으로 찾기
2. 이름으로 찾기

-> '''

def load():
    file = open('data.txt', 'r', encoding='utf-8')
    info = file.read()
    info = info.rstrip('\n')

    sStudents = info.split('\n')

    for s in sStudents:
        sInfo = s.split(',')
        student = {}
        student['이름'] = sInfo[0]
        student['학번'] = int(sInfo[1])
        student['성별'] = sInfo[2]
        student['성적'] = list(map(int, sInfo[3:]))
        students.append(student)
        
    file.close()

def save():
    pass

def seeAll():
    print('이름           학번           성별     성적')
    for s in students:
        print('{}       {}      {}      {}'.format(s['이름'], s['학번'], s['성별'], s['성적']))

def seePersonal():
    choice = input(m2)
    if choice == '1':
          num = int(input('학번: '))
          for s in students:
              if s['학번'] == num:
                  print('이름           학번           성별     성적')
                  print('{}       {}      {}      {}'.format(s['이름'], s['학번'], s['성별'], s['성적']))

def personalAverage():
    choice = input(m2)
    if choice == '1':
        num = int(input('학번: '))
        for s in students:
            if s['학번'] == num:
                sSum = sum(s['성적'])
                average = sSum / len(s['성적'])
    return average

def appendStudent():
    stdInfo = {}
    stdInfo['이름'] = input('이름: ') + ','
    stdInfo += input('학번: ') + ','
    stdInfo += input('성별: ') + ','
    stdInfo += input('성적: ')

    file = open('data.txt', 'a', encoding='utf-8')
    file.write(stdInfo)
    
    file.close()
    

menu = '''
1. 전체 학생 정보
2. 학생 개인 정보
3. 학생 개인 평균
4. 전체 학생 평균
5. 석차
6. 과목별 평균
7. 학생 추가
0. 종료

-> '''

if __name__ == '__main__':
    while True:
        load()
        print()

        choice = input(menu)
        if choice == '1':
            seeAll()
        elif choice == '2':
            seePersonal()
        elif choice == '3':
            print(personalAverage())
        elif choice == '4':
            pass
        elif choice == '5':
            pass
        elif choice == '6':
            pass
        elif choice == '7':
            appendStudent()
        elif choice == '0':
            break
