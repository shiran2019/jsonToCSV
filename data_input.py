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
}

]
