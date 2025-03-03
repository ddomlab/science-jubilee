from science_jubilee.tools import Spectrometer

# Create a spectrometer object
sp = Spectrometer.SpectroscopyTool(0, 'uv-vis')
spec = sp.dark_spectrum(15,15)
print(spec)