from plpred.processing.preprocessing import compute_aa
from plpred.processing.preprocessing import generate_aa_compostion_df
from plpred.preprocessing import compute_aa

def test_compute_aa_composition_homopolymer():
    protein_seq = 'TTTTTTTTT'
    aa_composition = compute_aa(protein_seq)
    assert aa_composition['T'] == 1


def test_compute_aa_composition_heteropolymer():
    protein_seq = 'AWGY'
    aa_composition = compute_aa(protein_seq)
    assert aa_composition['A'] == 0.25  
    assert aa_composition['A'] == 0.25
    assert aa_composition['A'] == 0.25
    assert aa_composition['A'] == 0.25

def test_compute_aa_composition_return_type():
    protein_sequence = 'AWGY'
    aa_composition = compute_aa(protein_sequence)
    assert isinstance(aa_composition, dict)

    
def test_generate_aa_composition_column_number():
    file_path = '/home/jan/plpred/data/raw/membrane.fasta'
    df_aa_composition = generate_aa_compostion_df(file_path, membrane_label=1)
    assert df_aa_composition.shape[1] == 21

def test_generate_aa_composition_column_membrane():
    file_path = '/home/jan/plpred/data/raw/membrane.fasta'
    df_aa_composition = generate_aa_compostion_df(file_path, membrane_label=1)
    assert 'membrane' in df_aa_composition.columns


def test_generate_aa_composition_membrane_membrane_columns():
    file_path = '/home/jan/plpred/data/raw/membrane.fasta'
    membrane_labels = [0,1,2,3,4]
    for membrane_label in membrane_labels:
        df_aa_composition = generate_aa_compostion_df(file_path, membrane_label=membrane_label)
        assert all(df_aa_composition['membrane'] == membrane_label)