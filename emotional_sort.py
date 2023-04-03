def sort_emotions(arr, order):
    emotion_value = {':D': 1, ':)': 2, ':|': 3, ':(': 4, 'T_T': 5}
    occ_emotions = []
    value_emotion = []

    for i in range(len(arr)):
        if arr[i] in emotion_value.keys():
            occ_emotions.append(arr[i])
            value_emotion.append(emotion_value[arr[i]])
    d = zip(occ_emotions, value_emotion)
    d = sorted(list(d), key = lambda x: x[1])

    result = []
    for x in d:
        result.append(x[0])
    
    return result if order else list(reversed(result))

print(sort_emotions([ ':D', 'T_T', ':D', ':(' ], True), [ ':D', ':D', ':(', 'T_T' ])
print(sort_emotions([ 'T_T', ':D', ':(', ':(' ], True), [ ':D', ':(', ':(', 'T_T' ])
print(sort_emotions([ ':)', 'T_T', ':)', ':D', ':D' ], True), [ ':D', ':D', ':)', ':)', 'T_T' ])
print(sort_emotions([ ':)', 'T_T', ':)', ':D', ':D' ], False), [ ':D', ':D', ':)', ':)', 'T_T' ])

