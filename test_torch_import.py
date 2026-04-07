import sys
print("Python version:", sys.version)
try:
    import torch
    print("Torch version:", torch.__version__)
    import torch.nn.modules._functions
    print("Imported torch.nn.modules._functions successfully.")
except Exception as e:
    print(f"Exception: {e}")
