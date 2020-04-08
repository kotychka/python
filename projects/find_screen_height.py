def find_screen_height(width, ratio): 
    # your code here
    int_ratio = ratio.split(':')

    height = int(width / int(int_ratio[0]) * int(int_ratio[1]))
    # answer = str(width) + 'x' + str(height)
    answer = f'{width}x{height}'
    print(answer)

find_screen_height(1024, "4:3")