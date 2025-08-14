import torch
import torch.nn as nn
import torchvision
from torchvision import transforms
from PIL import Image
from torchvision.models import Inception_V3_Weights
from torchvision.models import inception_v3
import logging

# Configure logging
logger = logging.getLogger(__name__)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
logger.info(f"Using device: {device}")

logger.info("Loading Inception V3 architecture...")
model = inception_v3(Inception_V3_Weights.DEFAULT)
model.to(device)

num_ftrs = model.fc.in_features
logger.info(f"Modifying final layer from {num_ftrs} to 2 features for binary classification")
model.fc = nn.Linear(in_features=num_ftrs, out_features=2)

# Load the trained weights with proper device mapping
logger.info("Loading trained weights from forest_fire_classifier.pth...")
model.load_state_dict(torch.load("forest_fire_classifier.pth", map_location=device), strict=False)
logger.info("Successfully loaded PyTorch model weights!")

class_names = ["fire", "no fire"]
logger.info(f"Model configured for classes: {class_names}")

data_transforms = {
    "train": transforms.Compose([
        transforms.Resize(224),
        transforms.ToTensor(),  # Moved ToTensor before Normalize
        transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)),
        transforms.RandomHorizontalFlip(p=0.5),
    ]),
    "test": transforms.Compose([
        transforms.Resize(224),
        transforms.ToTensor(), # Moved ToTensor before Normalize
        transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)),
    ])
}

# fire: 0, no fire: 1
def predict(img_path):
  logger.info(f"Starting PyTorch inference on image: {img_path}")
  
  pil_img = Image.open(img_path).convert("RGB") # Ensure image is in RGB format
  logger.info(f"Image loaded and converted to RGB, size: {pil_img.size}")
  
  # Apply the test transformations
  img_tensor = data_transforms["test"](pil_img).unsqueeze(0) # Add batch dimension
  img_tensor = img_tensor.to(device) # Move tensor to the correct device
  logger.info(f"Image tensor shape: {img_tensor.shape}, device: {img_tensor.device}")

  model.to(device) # Ensure the model is on the correct device
  model.eval() # Set model to evaluation mode
  
  logger.info("Running PyTorch model inference...")
  with torch.inference_mode():
    pred = model(img_tensor)
    # If the model returns InceptionOutputs, get the main output
    if isinstance(pred, torchvision.models.inception.InceptionOutputs):
        pred = pred.logits
        logger.info("Extracted logits from InceptionOutputs")
    
    pred_prob = torch.softmax(pred, dim=1) # Get prediction probabilities
    pred_label_idx = torch.argmax(pred_prob, dim=1).item() # Get the predicted class index
    pred_label = class_names[pred_label_idx] # Get the predicted class name
    
    logger.info(f"Raw model output shape: {pred.shape}")
    logger.info(f"Prediction probabilities: {pred_prob}")
    logger.info(f"Predicted class index: {pred_label_idx}")
    logger.info(f"Final prediction: {pred_label}")

  return pred_label, pred_prob