# data_input.py

# Create a list of dictionaries with the required data for multiple research topics
data = [
    {
        "ResearchTopic": "AI-driven Car Damage Identification",
        "Dataset": "VehiDE dataset",
        "AnnotationDataStructure": "13,945 high-resolution images annotated across 8 damage categories",
        "UsedModels": "YOLOv5, Mask R-CNN, SGL-KRN, PoolNet, U2-Net, CSNet, DCN",
        "Purposes": "Real-time object detection (YOLOv5), precise segmentation (Mask R-CNN), "
                    "handling irregular damages and salient object detection (SGL-KRN, PoolNet, U2-Net, CSNet, DCN)",
        "ModelAccuracy": "SGL-KRN: Best performance, PoolNet: Strong, U2-Net: Decent, CSNet and DCN: Less accurate"
    },
    {
        "ResearchTopic": "Procedural Generation for Damage Assessment in Vehicles",
        "Dataset": "CrashCar101 dataset",
        "AnnotationDataStructure": "101,050 synthetic images with pixel-accurate annotations for vehicle parts and damage types",
        "UsedModels": "DeepLabv3 (ResNet-50, ResNet-101), SegFormer (B5 variant)",
        "Purposes": "Semantic segmentation for part and damage identification; few-shot learning for real-world transferability",
        "ModelAccuracy": "DeepLabv3 (ResNet-101): Significant improvement in few-shot learning (up to +17.9% mIoU); "
                         "SegFormer: Consistent outperformance over models trained on real data"
    },
    {
        "ResearchTopic": "Vision-based Car Damage Detection",
        "Dataset": "CarDD dataset",
        "AnnotationDataStructure": "4,000 high-resolution images with over 9,000 annotated instances across 6 damage categories (dent, scratch, crack, glass shatter, tire flat, lamp broken)",
        "UsedModels": "Mask R-CNN, Cascade Mask R-CNN, GCNet, HTC, DCN, DCN+, SGL-KRN, PoolNet, U2-Net, CSNet",
        "Purposes": "Instance segmentation and object detection (Mask R-CNN, Cascade Mask R-CNN, GCNet, HTC, DCN), enhanced performance on difficult damage types with DCN+, refinement of irregular damage detection with Salient Object Detection (SGL-KRN, PoolNet, U2-Net, CSNet)",
        "ModelAccuracy": "DCN+: Best performance on difficult classes (dent, scratch, crack); SGL-KRN: Best overall SOD performance with emphasis on small and slender objects"
    },
    {
        "ResearchTopic": "Vehicle Damage Severity Estimation for Insurance Operations",
        "Dataset": "Combination of public and private datasets including 18,000 claims with 200,000 images for training and 2,600 claims with 30,000 images for validation",
        "AnnotationDataStructure": "Annotated vehicle parts, damage types (broken light, broken window, dent, missing part), interior/exterior classification, vehicle angle classification",
        "UsedModels": "YOLOv4, VGG-16, ResNet-18, Mask R-CNN with Deformable Convolutions (MaskR-DCN), ResNet-34, XGBoost",
        "Purposes": "Vehicle detection (YOLOv4), interior/exterior classification (VGG-16), angle classification (ResNet-18), damage and parts segmentation (MaskR-DCN), airbag deployment detection (ResNet-34), final damage severity prediction (XGBoost)",
        "ModelAccuracy": "YOLOv4 with high-resolution input and test-time augmentation provided the best vehicle detection performance; MaskR-DCN outperformed Mask R-CNN in parts and damage detection; XGBoost combining structured and image features improved severity prediction by over 2% AUC compared to using structured data alone"
    },
    {
        "ResearchTopic": "Deep Learning-Based Car Damage Classification and Cost Estimation",
        "Dataset": "Custom dataset created from images collected from the Copart website, supplemented with the COCO dataset for additional validation",
        "AnnotationDataStructure": "Manually annotated images with bounding boxes and masks for various damage types (bumper dents, door dents, broken headlights, scratches, etc.), separated into training and testing sets",
        "UsedModels": "Two Mask R-CNN models",
        "Purposes": "First Mask R-CNN for detecting vehicle sides (front, back, left, right) to influence cost estimation; Second Mask R-CNN for detecting and segmenting specific damage areas for accurate classification and cost estimation",
        "ModelAccuracy": "98.5% accuracy in damage detection and classification; high confidence in mask generation with a performance accuracy of over 0.97"
    }
]
