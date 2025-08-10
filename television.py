class Television:
    """
    Class that defines variables within the limits of the programs possibilities.
    """
    MIN_VOLUME = 0
    MAX_CHANNEL = 3
    MIN_CHANNEL = 0
    MAX_VOLUME = 2

    def __init__(self) -> None:
        """
        Method that defines instance variables.
        stats(bool): Power of Tv (False = off)
        muted(bool): Status of Tv.
        volume(int): Volume level of Tv when on.
        channel(int): Channel Number of Tv when on.
        """
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL and Television.MAX_CHANNEL
        self.__status = False

    def power(self) -> None:
        """
        Method that checks power of TV.
        Returns:
            None
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        The method that toggles the mute function.
        Returns:
            None
        """
        if self.__status:
            self.__muted = not self.__muted



    def channel_up(self) -> None:
        """
        This is the method that increases channels
        Returns:
            None
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL


    def channel_down(self) -> None:
        """
        This is the method that decreases channels
        Returns:
            None
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        This is the method that turns volume up.
        Returns:
            None
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        This is the method that turns volume down.
        Returns:
            None
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        This is the method that prints out the data for the inputs on the televison
        Returns:
            Tv status.
        """


        return (f"Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME if self.__muted else self.__volume }")
