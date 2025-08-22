import torch
import torch.nn as nn
from torchvision import models
from torchvision.models import ResNet50_Weights 

class ResNetBrain(nn.Module):
    def __init__(self, n_cls=4):
        super().__init__()
        self.backbone = models.resnet50(weights=ResNet50_Weights.DEFAULT) 
        for param in self.backbone.parameters():
            param.requires_grad = False
        self.backbone = nn.Sequential(*list(self.backbone.children())[:-2])
        self.classifier = nn.Sequential(
            nn.AdaptiveAvgPool2d((1, 1)),
            nn.Flatten(),
            nn.Linear(2048, 256), nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(256, n_cls)
        )

    def forward(self, x):
        x = self.backbone(x)
        return self.classifier(x)

def load_model(model_path="model/modelo_resnetV4.pth", n_cls=2):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = ResNetBrain(n_cls)
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.to(device)
    model.eval()
    return model, device
