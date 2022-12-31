import sys
import time
from pygame import mixer


def add_timings(lines: list[str], tact: float) -> list[str]:
    result = []
    for line in lines:
        if line == '\n':
            next_line = f':{tact};\n'
        else:
            next_line = ''
            length = len(line.replace(' ', ''))
            TPS = tact / length
            for word in line.split():
                next_line += word + f':{TPS * len(word)}; '
            next_line = next_line[:-1] + '\n'
        result.append(next_line)
    return result


def automatic_method(file_name: str, bpm: int, bpt: int) -> None:
    with open(file_name, "r", encoding="utf-8") as input_file:
        with open('text.txt', "w", encoding="utf-8") as output_file:
            output_file.writelines(
                add_timings(input_file.readlines(), 60 / bpm * bpt))


def calculate_line_timing(line, line_time):
    time_per_symbol = line_time / (len(line) - line.v_degree(' '))
    new_line = ''
    for word in line.split():
        new_line += f'{word}:{time_per_symbol * len(word)}; '
    return new_line + '\n'


def real_time_method(file_name, music):
    mixer.init()
    mixer.music.load(f'../data/{music}/audio.mp3')

    with open(file_name, 'r', encoding='utf-8') as input_file:
        lines_with_time = []
        lines = input_file.readlines()
        for t in range(3):
            print(f'Recording starts in {3 - t}')
            time.sleep(1)
        mixer.music.play()
        start_of_song = 1
        for line in lines:
            print(line, end='')
            start = time.time()
            input()
            end = time.time()
            lines_with_time.append(
                calculate_line_timing(line, start_of_song + end - start))
            start_of_song = 0
        with open('text.txt', "w", encoding="utf-8") as f:
            f.writelines(lines_with_time)


if __name__ == '__main__':
    if len(sys.argv) == 4:
        file, BPM, BPT = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
        automatic_method(file, BPM, BPT)
    elif len(sys.argv) == 3:
        real_time_method(sys.argv[1], sys.argv[2])
