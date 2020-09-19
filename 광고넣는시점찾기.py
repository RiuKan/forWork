from itertools import repeat
import operator

def solution(play_time, adv_time, logs):
    answer = ''
    play_time = play_time.split(":")
    all_play_time = int(play_time[0])*60*60 + int(play_time[1])*60 + int(play_time[2])


    adv_time = adv_time.split(":")
    all_adv_time = int(adv_time[0]) * 60 * 60 + int(adv_time[1]) * 60 + int(adv_time[2])


    allplaytime_list = list(repeat(0,int(all_play_time)+1))
    print(allplaytime_list)
    for i in range(len(logs)):
        logList = logs[i].split("-")

        first_play_time = logList[0].split(":")
        all_first_play_time = int(first_play_time[0]) * 60 * 60 + int(first_play_time[1]) * 60 + int(first_play_time[2])
        second_play_time = logList[1].split(":")
        all_second_play_time = int(second_play_time[0]) * 60 * 60 + int(second_play_time[1]) * 60 + int(second_play_time[2])

        for i in range(all_first_play_time,all_second_play_time+1):
            allplaytime_list[i] = allplaytime_list[i]+1



    sumList = []
    for i in range(len(allplaytime_list)-all_adv_time):
        sumList.append(sum(allplaytime_list[i:i+all_adv_time]))

    print(sumList)
    if (sumList.index(max(sumList))-1)//(60*60)<9:
        answer = "0" + str((sumList.index(max(sumList)) - 1) // (60 * 60)) + ":" + str(
            ((sumList.index(max(sumList)) - 1) % (60 * 60)) // 60) + ":" + str(
            ((sumList.index(max(sumList)) - 1) % (60 * 60)) % 60)
    else:
        answer = str((sumList.index(max(sumList)) - 1) // (60 * 60)) + ":" + str(
            ((sumList.index(max(sumList)) - 1) % (60 * 60)) // 60) + ":" + str(
            ((sumList.index(max(sumList)) - 1) % (60 * 60)) % 60)

    print(answer)



    return answer
# "01:30:59" ==
solution("3:00:00","00:14:15",["01:11:15-01:45:14", "00:20:31-01:30:00", "00:25:50-01:59:29", "01:10:59-02:53:29", "01:37:44-02:02:30"])