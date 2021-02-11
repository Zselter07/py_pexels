from pexels import Pexels
from pexels.models.enums import Orientation, Size

pexels = Pexels()
video_ids = pexels.get_video_ids(
    'dogs',
    videos_orientation=Orientation.HORIZONTAL,  # Optional
    videos_size=Size.FOUR_K                     # Optional
)