from plpred.processing import generate_aa_compostion_df
from plpred.models import PlpredNN
from plpred.models import PlpredRF
from plpred.models import PlpredSVM
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import tempfile
import os 

citoplasm_df = pd.read_csv( '/home/jan/plpred/data/raw/cytoplasm.fasta', membrane_label=0)
membrane_df  = pd.read_csv('/home/jan/plpred/data/raw/membrane.fasta', membrane_label=1)
df_concat    = pd.concat([citoplasm_df, membrane_df])



X = df_concat.drop( ['membrane'], axis=1 )
y = df_concat['membrane']

X_train, X_test, y_train, y_test = train_test_split(X, y)


#plpredGB

def test_plprednn_fit():
    model = PlpredNN()
    model.fit(X_train, y_train)

def test_plprednn_predict():
    model = PlpredNN()
    model.fit(X_train, y_train)
    model.predict(X_test)

def test_plprednn_accuracy():
    model = PlpredNN()
    model.fit(X_train, y_train)
    predict = model.predict(X_test)
    assert accuracy_score(y_test, predict) >= 0.9

def test_prednn_save():
    model = PlpredNN()
    model.fit(X_train, y_train)
    predition = model.fit(X_test)
    temfile = tempfile.NamedTemporaryFile().name
    model.save(tempfile)
    assert os.path.isfile(temfile)

#implementar outros testes para os demais modelos. 
#se tiver f, é porque p teste falhou