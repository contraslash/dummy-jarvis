# dummy-jarvis

Código fuente para el [siguiente post](http://blog.contraslash.com/un-jarvis-simple-en-python/)

Se requiere de [espeak](http://espeak.sourceforge.net/download.html)

> Para mac, la mejor manera de tener espeak funcionando es usando [este repositorio](https://github.com/pettarin/espeakosx)

```
pip install -r requirements.txt
git clone https://github.com/relsi/python-espeak
cd python-espeak
make install

cd ..
mkdir pyespeak
cp python-espeak/espeak/* pyespeak
python jarvis.py
```
