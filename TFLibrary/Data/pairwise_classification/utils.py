from collections import Counter


def make_vocab(file_name, sequences, vocab_size=None):
    """
    Tokenization, and write to files, format:
    
    vocab.txt:
        emerson
        lake
        palmer
        
    This format can be easily read via:
    `tf.contrib.lookup.index_table_from_file`
    """
    counter = Counter()
    for seq in sequences:
        # tokenization
        tokens = seq.split()
        # remove empty
        tokens = [t for t in tokens if t != ""]
        # build vocab
        counter.update(tokens)

    with open(file_name, "w") as wtr:
        filtered_vocab = [w for w, c in counter.most_common(vocab_size)]
        wtr.write("\n".join(filtered_vocab))
    
    print("Finished writing vocab file to ", file_name)


def write_to_file(base_file_name, sequences_1, sequences_2, labels,
                  lower=True, verbose=True):
    """
    Write Sequences 1, Sequences 2 and Labels, together with
    corresponding vocab files to separate files
    """
    if not lower:
        raise NotImplementedError("Only Lower Case is supported")
    
    processed_seq_1 = list(map(str.lower, sequences_1))
    processed_seq_2 = list(map(str.lower, sequences_2))
    processed_labels = list(map(str.lower, labels))
    
    with open(base_file_name + ".sequence_1", "w") as f:
        f.write("\n".join(processed_seq_1))
    with open(base_file_name + ".sequence_2", "w") as f:
        f.write("\n".join(processed_seq_2))
    with open(base_file_name + ".labels", "w") as f:
        f.write("\n".join(processed_labels))
    
    make_vocab(file_name=base_file_name + ".label_vocab",
               sequences=processed_labels)
    make_vocab(file_name=base_file_name + ".source_vocab",
               sequences=processed_seq_1 + processed_seq_2)
    
    if verbose:
        print("First 3 Seq1:\n\n" + "\n".join(processed_seq_1[:3]), "\n")
        print("First 3 Seq2:\n\n" + "\n".join(processed_seq_2[:3]), "\n")
        print("First 3 Labels:\n\n" + "\n".join(processed_labels[:3]), "\n")
