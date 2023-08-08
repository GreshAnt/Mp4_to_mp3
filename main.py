from moviepy.editor import VideoFileClip
from pydub import AudioSegment
import os


def get_base_name(path):
    return os.path.splitext(os.path.basename(path))[0]


def convert_video_to_audio(input_path, output_path, output_format):
    video = VideoFileClip(input_path)
    audio = video.audio
    audio.write_audiofile(output_path, codec=output_format)


def convert_audio_format(input_path, output_path, input_format, output_format):
    audio = AudioSegment.from_file(input_path, format=input_format)
    audio.export(output_path, format=output_format)


def main():
    print("Welcome to the Media Converter!")

    while True:
        try:
            choice = input("Select the conversion type:\n"
                           "A. mp4 to MP3\n"
                           "B. m4a to MP3\n"
                           "Q. Quit\n"
                           "> ").lower()

            if choice == 'q':
                print("Goodbye!")
                break

            if choice == 'a':
                input_file = input("Enter the input video file path: ")
                output_file = f"{get_base_name(input_file)}.mp3"
                convert_video_to_audio(input_file, output_file, 'mp3')

            elif choice == 'b':
                input_file = input("Enter the input audio file path: ")
                output_file = f"{get_base_name(input_file)}.mp3"
                convert_audio_format(input_file, output_file, 'm4a', 'mp3')

            else:
                print("Invalid choice. Please choose a valid option.")
                continue

            choice = input(f"File converted successfully! Output file: {output_file} Wanna do it again? Y/N >").lower()

            if choice == 'y':
                print('It\'s a good choice. Let\'s do it again!')
                continue
            else:
                print('It\'s time to say goodbye!')
                break

        except Exception as e:
            print(f"An error occurred: {e}")
            continue


if __name__ == "__main__":
    main()
