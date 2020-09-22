# 2018 KAKAO BLIND RECRUITMENT
# https://programmers.co.kr/learn/courses/30/lessons/17682
# 28min 4sec
def solution(dartResult):
    answer = 0

    # Store score in each shot.
    score = [0, 0, 0]
    score_idx = 0
    for i, data in enumerate(dartResult):
        if data == 'S':
            pass
        # double, ^2.
        elif data == 'D':
            score[score_idx] = pow(score[score_idx], 2)
        # triple, ^3.
        elif data == 'T':
            score[score_idx] = pow(score[score_idx], 3)
        # *2, previous score and currently score.
        elif data == '*':
            score[score_idx] *= 2
            if score_idx != 0:
                score[score_idx-1] *= 2
        # *-1, make current score minus.
        elif data == '#':
            score[score_idx] *= -1
        # score number.
        else:
            if i != 0:
                # score 10
                if data == '0' and dartResult[i-1] == '1':
                    score[score_idx] = 10
                    continue
                score_idx += 1
            score[score_idx] = int(data)
            
    answer = sum(score)

    return answer
if __name__ == "__main__":
    dartResult = "1D2S#10S"

    solution(dartResult)