"""A video player class."""

from .video_library import VideoLibrary
import random
is_playing = False
old_video = None
video_playing = None
is_paused = False
tags = ""

class VideoPlayer:

    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()


    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        all_videos = self._video_library.get_all_videos()
        print("Here's a list of all available videos:")
        global tags
        temp = []
        for videos in all_videos:
            #Display tags in correct format
            tags = "["
            for tag in videos.tags:
                tags = tags + tag + " "
            tags = tags + "]"
            if tags != "[]":
                tags = tags[0:len(tags) -2] + "]"

            temp += [f"{videos.title} ({videos.video_id}) {tags}"]
        sortedl = sorted(temp)
        for i in sortedl:
            print(i)


    def play_video(self, video_id):
        global is_playing
        global old_video
        global video_playing
        video_playing = self._video_library.get_video(video_id)
        if not video_playing:
            print(f"Cannot play video: Video does not exist")
        else:
            if is_playing is True :
                print(f"Stoping video: {old_video}")
                print(f"Playing video: {video_playing.title}")
                old_video = video_playing.title
            else:
                print(f"Playing video: {video_playing.title}")
                is_playing = True
                old_video = video_playing.title

    def stop_video(self):
        """Stops the current video."""
        global is_playing
        if is_playing is True:
            print(f"Stoping video: {old_video}")
            is_playing = False

        else:
            print("Cannot stop video: No video is currently playing")



    def play_random_video(self):
        """Plays a random video from the video library."""

        global is_playing
        global old_video
        global video_playing
        video_playing = random.choice(self._video_library.get_all_videos())
        if is_playing is True :
            print(f"Stoping video: {old_video}")
            print(f"Playing video: {video_playing.title}")
            old_video = video_playing.title
        else:
            print(f"Playing video: {video_playing.title}")
            is_playing = True
            old_video = video_playing.title

    def pause_video(self):
        """Pauses the current video."""

        global is_playing
        global is_paused
        if is_playing is True:
            print(f"Pausing video: {old_video}")
            is_playing = False
            is_paused = True

        elif is_paused is True:
            print(f"Video already paused: {old_video}")

        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""

        if is_paused is True:
            print(f"Continuing video: {old_video}")
            is_paused = False
            is_playing = True

        elif is_playing is True:
            print("Cannot continue video: Video is not paused")

        else:
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""
        global video_playing

        if is_playing is True:
            print (f"Currently Playing: {video_playing.title} {video_playing.video_id} {tags}" )

        elif is_paused is True:
            print (f"Currently Playing: {video_playing.title} {video_playing.video_id} {tags}" )

        else:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
