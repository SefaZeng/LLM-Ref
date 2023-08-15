ref_path=$1
hyp_file=$2

# zh for chinese, en for english, flores200 for f200sp(recommended)
tokenizer=$3

files=$(ls ${ref_path}/*)
ref_files=""
for file in ${files};
do
    ref_files+=" "${file}
done

python sacre.py \
    -r $ref_files \
    -i $hyp_file \
    -o $hyp_file.eval_multi_ref \
    -l $tokenizer
