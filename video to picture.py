import cv2
import os

EXTRACT_FREQUENCY = 1


def extract(videopath, index=EXTRACT_FREQUENCY):
    dst_folder = videopath.split('.', 1)[0]
    import shutil
    try:
        shutil.rmtree(dst_folder)
    except OSError:
        pass

    os.mkdir(dst_folder)
    video = cv2.VideoCapture()
    if not video.open(videopath):
        print("can not open the video")
        exit(1)
    count = 1
    while True:
        _, frame = video.read()
        if frame is None:
            break
        if count % EXTRACT_FREQUENCY == 0:
            save_path = "{}/{:>d}.jpg".format(dst_folder, index)
            cv2.imwrite(save_path, frame)
            index += 1
        count += 1
    video.release()
    print("Totally save {:d} pics".format(index - 1))


if __name__ == '__main__':
    extract('top-down-test2.mp4')
