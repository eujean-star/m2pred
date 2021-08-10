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
    