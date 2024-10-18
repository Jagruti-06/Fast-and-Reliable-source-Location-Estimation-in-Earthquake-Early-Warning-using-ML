**MACHINE LEARNING FOR FAST AND RELIABLE SOURCE-LOCATION ESTIMATION IN EARTHQUAKE EARLY WARNING**

**ABSTRACT** :

We develop a random forest (RF) model for rapid earthquake location with an aim to assist earthquake early
warning (EEW) systems in fast decision making. This system exploits P-wave arrival times at the first five
stations recording an earthquake and computes their respective arrival time differences relative to a reference
station (i.e., the first recording station). These differential P-wave arrival times and station locations are
classified in the RF model to estimate the epicentral location. We train and test the proposed algorithm with an
earthquake catalog from Japan. The RF model predicts the earthquake locations with a high accuracy,
achieving a Mean Absolute Error (MAE) of 2.88 km. As importantly, the proposed RF model can learn from a
limited amount of data (i.e., 10% of the dataset) and much fewer (i.e., three) recording stations and still
achieve satisfactory results (MAE<5 km). The algorithm is accurate, generalizable, and rapidly responding,
thereby offering a powerful new tool for fast and reliable source-location prediction in EEW.

**EXISTING SYSTEM :**

Earthquake early warning (EEW) systems are required to report earthquake locations and magnitudes as
quickly as possible before the damaging S wave arrival to mitigate seismic hazards. Deep learning techniques
provide potential for extracting earthquake source information from full seismic waveforms instead of seismic
phase picks.
We developed a novel deep learning EEW system that utilizes fully convolutional networks to simultaneously
detect earthquakes and estimate their source parameters from continuous seismic waveform streams. The
system determines earthquake location and magnitude as soon as very few stations receive earthquake signals
and evolutionarily improves the solutions by receiving continuous data. We apply the system to the 2016 M
6.0 Central Apennines, Italy Earthquake and its first-week aftershocks. Earthquake locations and magnitudes
can be reliably determined as early as 4 s after the earliest P phase, with mean error ranges of 8.5–4.7 km and
0.33–0.27, respectively.

**Disadvantages of existing system :**

● An existing system method is not investigated to improve the performance of real-time earthquake
detection and classification of source characteristics.
● Convolution neural networks-based clustering methods have not been used to regionalize earthquake
epicenters or predict their precise hypocenter locations.

**PROPOSED SYSTEM :**

The system proposes a RF-based method to locate earthquakes using the differential P-wave arrival times and
station locations (Figure 1). The proposed algorithm only relies on Pwave arrival times detected at the first
few stations. Its prompt response to earthquake first arrivals is critical for rapidly disseminating EEW alerts.
Our strategy implicitly considers the influence of the velocity structures by incorporating the source-station
locations into the RF model.
The proposed system evaluates the proposed algorithm using an extensive seismic catalog from Japan. Our
test results show that the RF model is capable of determining the locations of earthquakes accurately with
minimal information, which sheds new light on developing efficient machine learning.

**Advantages of proposed system :**

● The number of stations is a critical factor that determines the data availability and prediction accuracy.
The proposed RF model takes the arrival times of P waves recorded at multiple stations as the input,
hence a more stringent requirement of simultaneous recording at an increased number of stations
lowers the availability of qualified events.
● The localization problem can be resolved using a sequence of detected waves (arrival times) and
locations of seismograph stations that are triggered by ground shaking. Among various network
architectures, the recurrent neural network (RNN) is capable of precisely extracting information from a
sequence of input data, which is ideal for handling a group of seismic stations that are triggered
sequentially following the propagation paths of seismic waves.

**SYSTEM REQUIREMENTS :**

**Hardware System Configuration:-**

● Processor - Pentium –IV

● RAM - 4 GB (min)

● Hard Disk - 20 GB

● Key Board - Standard Windows Keyboard

● Mouse - Two or Three Button Mouse

● Monitor - SVGA

**SOFTWARE REQUIREMENTS :**

● Operating system : Windows 7 Ultimate.

● Coding Language : Python.

● Front-End : Python.

● Back-End : Django-ORM

● Designing : Html, css, javascript.

● Data Base : MySQL (WAMP Server).
