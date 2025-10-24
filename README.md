## 🧠 Project Purpose

Fine-tune an embedding model to understand **relationship compatibility** using **contrastive learning** and **synthetic data**. After training, your model should **bring compatible people closer in vector space** and **push incompatible ones apart** — even when their preferences are expressed in different words.

🎯 Core Objectives

| Phase | Goal |
|-------|------|
| Data Generation | Create synthetic pairs labeled similar/dissimilar |
| Contrastive Fine-Tuning | Train with contrastive loss |
| Quantized LoRA | Finetune using 4-bit quantization + LoRA adapters |
| Instructional Alignment | Format prompts as natural instructions for better generalization |
| Evaluation | Use similarity scores, clustering, and recall to benchmark |

## Dataset Structure

The training data consists of synthetic dating compatibility pairs in JSONL format. Each line contains two persona statements with a compatibility label:

```json
{"text_1":"boy: I love lazy Sundays","text_2":"girl: I'm all about meeting new people","label":1,"category":"lifestyle","subcategory":"relaxed_vs_extroverted","pair_type":"subtle_mismatch"}
{"text_1":"boy: I can't stand meditation","text_2":"girl: I don't enjoy Netflix marathons","label":1,"category":"lifestyle","subcategory":"relaxed","pair_type":"compatible"}
{"text_1":"boy: I value career ambition but I love work-life balance and family time","text_2":"girl: I really enjoy professional growth and I love family priorities","label":0,"category":"lifestyle_and_values","subcategory":"score_3","pair_type":"llm_judged_incompatible"}
```

**Dataset Statistics:**
- **Total pairs:** 1,195
- **Compatible pairs:** 628 (52.5%)
- **Incompatible pairs:** 567 (47.5%)
- **Categories:** lifestyle, interests, values, dealbreakers, realistic examples
- **Pair types:** dealbreaker, complex, LLM-judged, realistic, subtle mismatch

## Technical Training Details

The model training employs several advanced techniques for efficient fine-tuning:

### Model Architecture
- **Base Model:** `all-MiniLM-L6-v2` (SentenceTransformer)
- **Training Framework:** SentenceTransformers with custom trainer
- **Loss Function:** Contrastive loss for similarity learning

### Training Configuration
- **Quantization:** 4-bit quantization for memory efficiency
- **LoRA Adapters:** Low-Rank Adaptation for parameter-efficient fine-tuning
- **Instruction Format:** Natural language instructions for better generalization
- **Evaluation:** EmbeddingSimilarityEvaluator for performance monitoring

### Data Processing Pipeline
1. **Text Extraction:** Parse persona statements from structured format
2. **Label Conversion:** Transform compatibility labels to similarity scores (1.0 for compatible, 0.0 for incompatible)
3. **Dataset Creation:** Convert to SentenceTransformer-compatible format
4. **Train/Validation Split:** Automatic splitting for model evaluation

# Training
![Training](/training_img.png)


## Model Performance & Evaluation

![Eval](/eval_img.png)

### Statistical Analysis Results

The fine-tuned model shows **dramatic improvement** in distinguishing compatible vs incompatible pairs:

| Metric | Base Model | Fine-tuned Model | Improvement |
|--------|------------|------------------|-------------|
| **Effect Size (Cohen's d)** | -0.21 | -2.47 | **11.8x stronger** |
| **T-statistic** | -3.66 | -42.22 | **11.5x more significant** |
| **P-value** | 0.0003 | 5.2e-239 | **~10^235x more significant** |
| **Mean Difference** | -0.045 | -0.603 | **13.4x larger separation** |

### Key Improvements

✅ **Effect Size:** The fine-tuned model achieves a **large effect size** (Cohen's d = -2.47) compared to the base model's small effect (d = -0.21)

✅ **Statistical Significance:** P-value improved from 0.0003 to 5.2e-239, indicating **extremely high confidence** in the model's ability to distinguish compatibility

✅ **Separation Quality:** The mean difference between compatible and incompatible pairs increased from -0.045 to -0.603, showing **much clearer separation** in embedding space

✅ **Robustness:** The t-statistic increased from -3.66 to -42.22, indicating **much more consistent** and reliable performance across test samples

### Technical Interpretation

The **Cohen's d** values indicate:
- **Base Model (d = -0.21):** Small effect size, barely distinguishable performance
- **Fine-tuned Model (d = -2.47):** Large effect size, excellent discriminative ability

The **p-value** improvement demonstrates that the fine-tuned model's performance is **statistically significant** with extremely high confidence, while the base model's performance was only marginally significant.