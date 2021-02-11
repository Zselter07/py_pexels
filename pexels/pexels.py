# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
from typing import Optional, List, Dict, Callable, Union
import time, os

# Pip
from selenium_firefox import Firefox
from randomua import RandomUA

# Local
from .models.enums.orientation import Orientation
from .models.enums.size import Size

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------------- class: Pexels ------------------------------------------------------------ #

class Pexels():

    # -------------------------------------------------------- Public methods -------------------------------------------------------- #
    def __init__(
        self,
        user_agent: Optional[RandomUA] = None,
        proxy: Optional[str] = None
    ):
        self.browser = Firefox(
            user_agent=user_agent,
            proxy=proxy
        )

    def get_video_ids(
        self,
        search_term: str,
        videos_orientation: Orientation = Orientation.HORIZONTAL,
        videos_size: Size = Size.FULL_HD,
        max_videos: int = 35,
        ignored_ids: List[str] = [],
    ) -> List[str]:
        video_ids = []
        videos_orientation = videos_orientation.value
        videos_size = videos_size.value
        page_number = 1

        while len(video_ids) <= max_videos:
            url = self.__create_search_url(search_term, videos_orientation, videos_size, page_number)
            self.browser.get(url)
            time.sleep(1.5)
            video_elements = self.browser.find_all_by(type_='article', class_='js-photo-item--video photo-item photo-item--overlay photo-item--video js-photo-modal-navigator-watching')

            if not video_elements:
                print('No videos found')

                break

            for video_element in video_elements:
                video_id = self.browser.get_attribute(video_element, 'data-photo-modal-medium-id')

                if video_id not in ignored_ids:
                    video_ids.append(video_id)

            page_number += 1

        return video_ids

    # ------------------------------------------------------- Private methods -------------------------------------------------------- #
    @staticmethod
    def __create_search_url(
        search_term: str,
        videos_orientation: Orientation,
        videos_size: Size,
        page_number: int
    ) -> str:
        return "https://www.pexels.com/search/videos/{}/?orientation={}&size={}&page={}".format(
            search_term,
            videos_orientation,
            videos_size,
            page_number
        )


# ---------------------------------------------------------------------------------------------------------------------------------------- #