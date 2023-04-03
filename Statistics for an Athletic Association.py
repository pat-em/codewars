import statistics
import math


def change_to_hms(time_in_sec):
    hours = math.floor(time_in_sec // 3600)
    minutes = math.floor((time_in_sec - (hours * 3600)) //60)
    seconds = math.floor(time_in_sec - (minutes * 60) - (hours * 3600))

    return f"{str(hours).zfill(2)}|{str(minutes).zfill(2)}|{str(seconds).zfill(2)}"

def stat(strg):

    if strg == "":
        return ""

    time_inSec_list = []

    list_of_strg = strg.split(",")
    for i in range(len(list_of_strg)):
        teamTime = list_of_strg[i].split("|")

#change to seconds
        teamTime_inSec = int(teamTime[0])*3600 + int(teamTime[1])*60 + int(teamTime[2])
        time_inSec_list.append(teamTime_inSec)

    return f'Range: {change_to_hms(max(time_inSec_list)- min(time_inSec_list))} Average: {change_to_hms(statistics.mean(time_inSec_list))} Median: {change_to_hms(statistics.median(time_inSec_list) )}'

strg_ = "01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17"
print(stat(strg_))