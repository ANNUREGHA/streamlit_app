**dolma_dedup**


**Description**

The dataset was created by minhashing the textual contents i.e the text field of the dolma_dedup samples partitioned into 6 sub-folders namely dataset1 , dataset2 , dataset3 , dataset4 , dataset5 and dataset6 .

**How to pull this data?**

\- First pull the \`data.tar.zst\` file -> \`dvc-stratus pull data.tar.zst.dvc\`

\- Unzip it using command \`tar -I "zstd -T0" -xf data.tar.zst\`

\- Inside \`data\` directory you will get dvc files corresponding to each chunk/data file. Pull the required file as per the need.

**Data Preparation**

The minhash of the samples are obtained by running the [deduplicate.py](https://repository.zohocorpcloud.in/zohocorp/zlabs-deeplearning/zlabs-llm/llm-experiments#/blob/master/llm-experiments/src/data_trove/gpu_process/deduplication/deduplicate.py) over the dataset . The hyperparameters used for this run were as follows:


|hyper parameters|values|
|---|---|
|seed|10|
|fuzzy_hashes_per_bucket|13|
|fuzzy_num_buckets|20|
|fuzzy_char_ngrams|24|
|fuzzy_use_64bit_hash|False|
|id_field|dedup_temp_id|
|text_field|text|
|get_only_minhash|True|


Use the following command to run the deduplicate.py and obtain the minhashed dataset of nemotron-cc dataset .

slurm_script.sh ... --script_path /path/to/deduplicate.py \\

\--input-dir /path/to/input \\

\--cache-dir /path/to/cache \\

\--output-dir /path/to/output \\

\--id-field dedup_temp_id\\

\--text-field text \\

\--gpu-list '0,1,2,3,4,5,6,7' \\

\--get-only-minhash


**Data Format**

Each file has minhash signature of one parquet object per line with a \`dedup_temp_id\` field holding a prefix "dolma" .

\`\`\`

dedup_temp_id                                                          \_minhash_signature

0    dolma-cc-mid1-0576321364     \[4067293, 507887, 2160718, 3232980, 7144985, 7...

\`\`\`

**Storage :**

This minhashed dataset is compressed using zstd compression technique resulting in **1.7TB**  of  required storage .



