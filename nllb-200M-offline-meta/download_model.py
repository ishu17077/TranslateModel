from optimum.onnxruntime.modeling_seq2seq import ORTModelForSeq2SeqLM
from transformers import AutoTokenizer
# from transformers.utils import logging

# logging.enable_progress_bar()
# logging.set_verbosity_info()

model_id = "facebook/nllb-200-distilled-600M" # or a smaller sequence-to-sequence model
model = ORTModelForSeq2SeqLM.from_pretrained(model_id, export=True)
tokenizer = AutoTokenizer.from_pretrained(model_id)
                                                                                                                                            
model.save_pretrained("./onnx_model")
tokenizer.save_pretrained("./onnx_model")