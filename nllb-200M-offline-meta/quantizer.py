from pathlib import Path
from onnxruntime.quantization import quantize_dynamic, QuantType

model_dir = Path("./onnx_model")
quantized_dir = Path("./quantized_output")
quantized_dir.mkdir(parents=True, exist_ok=True)

model_files = [
    "encoder_model.onnx",
    "decoder_model.onnx",
    "decoder_with_past_model.onnx",
    "decoder_with_past_model.onnx_data"
]

for file_name in model_files:
    input_path = model_dir / file_name
    if input_path.exists():
        output_path = quantized_dir / file_name
        data_path = model_dir / f"{file_name}_data"
        
        print(f"Quantizing {file_name}...")
        
        # Check if external data file exists and is a regular file
        if data_path.exists() and not data_path.is_file():
            print(f"Warning: {data_path.name} is not a regular file. Skipping external data check.")
            
        try:
            quantize_dynamic(
                model_input=str(input_path),
                model_output=str(output_path),
                weight_type=QuantType.QInt8
            )
        except Exception as e:
            print(f"Error quantizing {file_name}: {e}")

print("Quantization script execution finished.")
