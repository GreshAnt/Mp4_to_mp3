from moviepy.editor import VideoFileClip
import os


def convert_mp4_to_mp3(input_path, output_path):
    video = VideoFileClip(input_path)
    audio = video.audio
    audio.write_audiofile(output_path)


def get_name(path):
    return os.path.splitext(os.path.basename(path))[0]


if __name__ == "__main__":
    while True:
        try:
            input_file = input('What is your input file path? Well, it must be a mp4 file, right? >')
            output_file = f'{get_name(input_file)}.mp3'
            convert_mp4_to_mp3(input_file, output_file)
            choice = input(f'Your file is ready! It\'s in {output_file} Wanna do it again? Y/N >').lower()
            if choice == 'y':
                print('It\'s a good choice. Let\'s do it again!')
                continue
            else:
                print('It\'s time to say goodbye!')
                break
        except Exception as e:
            choice = input(
                'There must be something wrong. Let\'s try again. Wait, do you want to exit? Y/N >').lower()
            if choice == 'y':
                print('Alright, exiting...')
                break
            else:
                print('Ok! Let\'s try again!')
                continue