from transformers import AutoTokenizer
from optimum.onnxruntime.modeling_seq2seq import ORTModelForSeq2SeqLM

model_dir = "./onnx_model"

tokenizer = AutoTokenizer.from_pretrained(model_dir, src_lang="eng_Latn")

model = ORTModelForSeq2SeqLM.from_pretrained(model_dir,
    encoder_file_name="encoder_model.onnx",
    decoder_file_name="decoder_model.onnx",
    decoder_with_past_file_name="decoder_with_past_model.onnx",

    )

source_txt = "Hello, how are you?"

inputs = tokenizer(source_txt, return_tensors="pt", padding=True)

target_lang_code = "sat_beng"

forced_bos_token_id = tokenizer.convert_tokens_to_ids(target_lang_code)
print(f"Target lang token ID for {target_lang_code}: {forced_bos_token_id}")

translated_tokens = model.generate(
    **inputs,
    forced_bos_token_id=forced_bos_token_id,
    max_length=128
)

translated_text = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)

print(f"Translated: {translated_text}")

