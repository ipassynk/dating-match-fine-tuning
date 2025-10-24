## 🧠 Project Purpose

Fine-tune an embedding model to understand **relationship compatibility** using **contrastive learning** and **synthetic data**. After training, your model should **bring compatible people closer in vector space** and **push incompatible ones apart** — even when their preferences are expressed in different words.

🎯 Core Objectives
Phase	Goal
Data Generation	Create synthetic pairs labeled similar/dissimilar
Contrastive Fine-Tuning	Train with contrastive loss 
Quantized LoRA	Finetune using 4-bit quantization + LoRA adapters
Instructional Alignment	Format prompts as natural instructions for better generalization
Evaluation	Use similarity scores, clustering, and recall to benchmark
