
import random

quiz = random.randint(100, 999)


def is_same(target, number):
    if target == number:
        result = 'Win'
    elif target > number:
        result = 'Low'
    else:
        result = 'High'
    return result


print('100에서 999중 숫자 하나를 골랐어요')
guess = int(input('예상되는 숫자를 입력후 엔터 키를 누르세요. \n>'))

higher_or_lower = is_same(quiz, guess)
cnt = 1

while higher_or_lower != 'Win':
    if higher_or_lower == 'Low':
        guess = int(input('Up! 다시 생각해보세요. %s\n>' % quiz))
    else:
        guess = int(input('Down! 다시 생각해보세요. \n>'))

    higher_or_lower = is_same(quiz, guess)

    cnt += 1


if cnt <= 3:
    print('정답! 당신은', cnt, '번 만에 맞췄어요. 대단해요!')
elif cnt == 1:
    print('정답! 당신은', cnt, '번 만에 맞췄어요. 로또를 사러 갑시다!')
elif cnt > 10:
    print('바봉, 당신이', cnt, '번 만에 맞췄니다.')

else:
    print( cnt,  '번 만에 정답!')

