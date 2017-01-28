from conans import ConanFile, CMake, tools

class KalmanConan(ConanFile):
    name = "kalman"
    version = "1.0"

    def source(self):
       self.run("git clone https://github.com/mherb/kalman.git")

    def package(self):
        self.copy("*", dst="include", src="kalman/include")
        self.copy("*", dst="include", src="include")
