import re
def solution(files):
    answer = []
    files_list = []
    for i in range(len(files)):
        HEAD = ""
        NUMBER = ""
        check_num = False
        for j in range(len(files[i])):
            if files[i][j].isdigit():
                NUMBER += files[i][j]
                check_num = True
            elif not files[i][j].isdigit() and check_num == False:
                HEAD += files[i][j]
            elif not files[i][j].isdigit() and check_num == True:
                break

        files_list.append([files[i], HEAD, NUMBER])
    files_list.sort(key=lambda x: (x[1].lower(), int(x[2])))

    for i in range(len(files_list)):
        answer.append(files_list[i][0])

    return answer

solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "foo010bar020.zip"])