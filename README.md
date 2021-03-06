### Keyword Density

Calculates the keyword density of a text as described in 
[Wikipedia](https://en.wikipedia.org/wiki/Keyword_density).

#### Usage

```
from kwdensity.density_calculator import DensityCalculator
from kwdensity.tokenizer import Tokenizer
from kwdensity.filters import StopwordsFilter

calculator = DensityCalculator(Tokenizer(), StopwordsFilter('el'))
densities = calculator(u''' Πλάτων ήταν αρχαίος Έλληνας φιλόσοφος από την Αθήνα, ο πιο γνωστός μαθητής του Σωκράτη και δάσκαλος του Αριστοτέλη. Το έργο του με τη μορφή φιλοσοφικών διαλόγων έχει σωθεί ολόκληρο και άσκησε τεράστια επιρροή στην αρχαία ελληνική φιλοσοφία και γενικότερα στη δυτική φιλοσοφική παράδοση μέχρι τις ημέρες μας. 
Ο Πλάτων, μεταξύ άλλων, έγραψε την Απολογία του Σωκράτους, το Συμπόσιο όπου μιλά για την φύση του έρωτα, ενώ σε δύο μακρούς διαλόγους, την Πολιτεία και τους Νόμους, περιέγραψε την ιδανική πολιτεία.Τα έργα του Πλάτωνα είναι 36 και όλα, εκτός από την Απολογία, διαλογικά. Μεταξύ των άλλων υπήρξε και ο ιδρυτής της Ακαδημίας.''')

print densities
```



