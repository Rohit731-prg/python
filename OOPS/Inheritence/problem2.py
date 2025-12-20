class Device:
    def __init__(self, deviceName) -> None:
        self.deviceName = deviceName

    def powerOn(self):
        print(f"Device {self.deviceName} is power ON");

class Camera(Device):
    def __init__(self, deviceName) -> None:
        super().__init__(deviceName)
    
    def takePhoto(self):
        print("Taking a photo using the camera")

class Phone(Device):
    def __init__(self, deviceName) -> None:
        super().__init__(deviceName)

    def makeCall(self):
        print("Making a phone call.")

class SmartPhone(Camera, Phone):
    def __init__(self, name) -> None:
        Camera.__init__(self, name)
        Phone.__init__(self, name)

    def useSmartFeatures(self):
        print("Using smartphone features like internet and apps.")

class GamingSmartPhone(SmartPhone):
    def __init__(self, name) -> None:
        super().__init__(name)

    def playGame(self):
        print("Playing high-performance games on the gaming smartphone.")


gp = GamingSmartPhone("Realme Narzo 30")
gp.powerOn()
gp.takePhoto()
gp.makeCall()
gp.useSmartFeatures()
gp.playGame()