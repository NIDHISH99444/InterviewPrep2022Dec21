
from abc import  ABC,abstractmethod

class VideoExporter(ABC):
    @abstractmethod
    def prepareVideo(self):
        pass
    @abstractmethod
    def doExport(self):
        pass

class FastVideoExporter(VideoExporter):
    def prepareVideo(self):
        print("Fast video prepare")

    def doExport(self):
        print("Fast video export")


class SlowVideoExporter(VideoExporter):
    def prepareVideo(self):
        print("Slow video prepare")

    def doExport(self):
        print("Slow video export")

class AudioExporter(ABC):
    @abstractmethod
    def prepareAudio(self):
        pass
    @abstractmethod
    def doExport(self):
        pass

class FastAudioExporter(AudioExporter):
    def prepareAudio(self):
        print("Fast audio prepare")

    def doExport(self):
        print("Fast audio export")


class SlowAudioExporter(AudioExporter):
    def prepareAudio(self):
        print("Slow audio prepare")

    def doExport(self):
        print("Slow audio export")



class ExporterFactory :
    @abstractmethod
    def get_video_exporter(self) -> VideoExporter:
        pass

    def get_audio_exporter(self) -> AudioExporter:
        pass

class FastExporter(ExporterFactory):
    def get_video_exporter(self) -> VideoExporter:
        return FastVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return FastAudioExporter()


class SlowExporter(ExporterFactory):
    def get_video_exporter(self) -> VideoExporter:
        return SlowVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return SlowAudioExporter()


def readExporter():
    factory={
        "slow": SlowExporter(),
        "fast" : FastExporter()
    }
    while True:
        inputQuality=input("enter export quality")
        if inputQuality in factory:
            return factory[inputQuality]


def main() -> None:
    fac=readExporter()
    vid=fac.get_video_exporter()
    vid.prepareVideo()
    vid.doExport()

    aud = fac.get_audio_exporter()
    aud.prepareAudio()
    aud.doExport()


if __name__ == '__main__':
    main()

