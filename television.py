class Television:
    '''
    class that defines variables within the limits of programs possibilites

    '''
    MIN_VOLUME = 0
    MAX_CHANNEL = 3
    MIN_CHANNEL = 0
    MAX_VOLUME = 2

    def __init__(self) -> None:
        '''
        method that defines instance variables
        '''
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL and Television.MAX_CHANNEL
        self.__status = False

    def power(self) -> None:
        '''
        Method that checks power of TV 
        '''
        self.__status = not self.__status

    def mute(self) -> None:
        '''
        the method that toggles the mute function
        '''
        if self.__status:
            self.__muted = not self.__muted



    def channel_up(self) -> None:
        '''
        This is the method that increases channels
        '''
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL


    def channel_down(self) -> None:
        '''
        This is the method that decreases channels
        '''
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        '''
        This is the method that turns volume up
        '''
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        '''
        This is the method that turns volume down
        '''
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        '''
        This is the method that prints out the data for the inputs on the televison
        :return: tv status
        '''


        return (f"Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME if self.__muted else self.__volume }")
