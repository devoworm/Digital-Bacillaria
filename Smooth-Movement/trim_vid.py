from pathlib import Path
import moviepy.editor as mpy
from typing import List

# SOURCE_PATH = Path("data/Bacillaria paradoxa (DIC)-9-J1qszm3d0.mp4")
SOURCE_PATH = Path("data/Bacillaria paradoxa (DIC)-9-J1qszm3d0.mp4")
TARGET_PATH = Path("data/bacillaria_trimmed.mp4")

CUTS = [('00:00:05.00', '00:00:13.00')]


def main(
    source_path: Path,
    target_path: Path,
    cuts: List[str],
):
    video = mpy.VideoFileClip(str(source_path))

    clips = []
    for cut in cuts:
        clip = video.subclip(cut[0], cut[1])
        clips.append(clip)

    final_clip = mpy.concatenate_videoclips(clips)
    final_clip.write_videofile(str(target_path))

if __name__ == '__main__':
    main(SOURCE_PATH, TARGET_PATH, CUTS)