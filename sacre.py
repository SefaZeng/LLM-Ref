import sacrebleu
import sys 
import argparse
         
def parse_args():
    parser = argparse.ArgumentParser(description="Sacrebleu")
    parser.add_argument("--refs", "-r", nargs="+", required=True,
                        help="reference (maybe multiple)")
    parser.add_argument("--input", "-i", required=True,
                        help="input corpora")
    parser.add_argument("--output", "-o", required=True)
    parser.add_argument("--lang", "-l", required=True)
         
    return parser.parse_args()
         
         
def bleu(pred, refs, out_file, tgt):
    with open(pred, 'r', encoding='utf-8') as f:
        pred = f.readlines()
         
    ref_list = []
    for ref in refs:
        with open(ref, 'r', encoding='utf-8') as f:
            ref_temp = []
            for line in f:
                ref_temp.append(line.strip())
        ref_list.append(ref_temp) 
    print(f">> Reference number: {len(ref_list)}")

    if tgt == 'zh' or tgt == 'cn':
        ours_bleu = sacrebleu.corpus_bleu(pred, ref_list, tokenize="zh")
    elif tgt == "en":
        ours_bleu = sacrebleu.corpus_bleu(pred, ref_list, tokenize="intl")
    else:
        ours_bleu = sacrebleu.corpus_bleu(pred, ref_list, tokenize=tgt)
        print('aha')
    log_message = "BLEU score = {0:.4f}, BP = {1:.3f}, sys_len = {2:}, ref_len = {3:}\n".format(ours_bleu.score, ours_bleu.bp, ours_bleu.sys_len, ours_bleu.ref_len)
    print(log_message, end="") 
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(log_message)
         
def main():
#    print(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    args = parse_args()
    bleu(args.input, args.refs, args.output, args.lang)
    #bleu(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
         
         
if __name__ == "__main__":
    main()
