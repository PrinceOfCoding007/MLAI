import os

BASE = "AI_Roadmap"

# parent directories that need to exist first
top_level = [
    "00_Fundamentals",
    "01_Data_Engineering_for_AI",
    "02_Machine_Learning",
    "03_Deep_Learning",
    "04_Transformers_and_LLMs",
    "05_RAG_Vector_Search",
    "06_MLOps_Deployment",
    "07_System_Design_AI",
    "08_Portfolio_Projects",
    "09_Interview_Preparation",
    "10_Documents_and_Planning"
]

# tracking files to create inside these main directories
track_files_dirs = top_level + [
    "00_Fundamentals/Python",
    "00_Fundamentals/Math_for_ML",
    "00_Fundamentals/DSA",
    "03_Deep_Learning/PyTorch",
]

# full folder structure
folders = [
    # Fundamentals
    "00_Fundamentals/Python/code",
    "00_Fundamentals/Python/notes",
    "00_Fundamentals/Python/cheatsheets",
    "00_Fundamentals/Python/interview_QA",
    "00_Fundamentals/Python/micro_projects",
    "00_Fundamentals/Math_for_ML/linear_algebra",
    "00_Fundamentals/Math_for_ML/probability_stats",
    "00_Fundamentals/Math_for_ML/optimization",
    "00_Fundamentals/DSA/patterns",
    "00_Fundamentals/DSA/leetcode_solutions",
    "00_Fundamentals/DSA/sheets",
    "00_Fundamentals/DSA/mock_interviews",
    "00_Fundamentals/DSA/progress_tracker",

    # Data Engineering for AI
    "01_Data_Engineering_for_AI/Numpy",
    "01_Data_Engineering_for_AI/Pandas",
    "01_Data_Engineering_for_AI/Polars",
    "01_Data_Engineering_for_AI/SQL",
    "01_Data_Engineering_for_AI/PySpark",
    "01_Data_Engineering_for_AI/data_projects",

    # Machine Learning
    "02_Machine_Learning/theory",
    "02_Machine_Learning/feature_engineering",
    "02_Machine_Learning/experiment_tracking",
    "02_Machine_Learning/interview_QA",
    "02_Machine_Learning/ML_Project",

    # Deep Learning
    "03_Deep_Learning/PyTorch/code",
    "03_Deep_Learning/PyTorch/notebooks",
    "03_Deep_Learning/PyTorch/dataloaders",
    "03_Deep_Learning/PyTorch/training_loops",
    "03_Deep_Learning/PyTorch/callbacks",
    "03_Deep_Learning/PyTorch/debugging",
    "03_Deep_Learning/PyTorch/interview_QA",
    "03_Deep_Learning/Computer_Vision",
    "03_Deep_Learning/NLP_Pre_Transformers",
    "03_Deep_Learning/DL_resources",
    "03_Deep_Learning/DL_Project",

    # Transformers & LLMs
    "04_Transformers_and_LLMs/attention",
    "04_Transformers_and_LLMs/tokenizers",
    "04_Transformers_and_LLMs/architectures/BERT",
    "04_Transformers_and_LLMs/architectures/GPT",
    "04_Transformers_and_LLMs/architectures/T5",
    "04_Transformers_and_LLMs/architectures/LLaMA",
    "04_Transformers_and_LLMs/fine_tuning/full_tuning",
    "04_Transformers_and_LLMs/fine_tuning/LoRA",
    "04_Transformers_and_LLMs/fine_tuning/QLoRA",
    "04_Transformers_and_LLMs/fine_tuning/PEFT",
    "04_Transformers_and_LLMs/hugging_face/datasets",
    "04_Transformers_and_LLMs/hugging_face/model_training",
    "04_Transformers_and_LLMs/hugging_face/inference",
    "04_Transformers_and_LLMs/safety_guardrails",
    "04_Transformers_and_LLMs/interview_QA",
    "04_Transformers_and_LLMs/LLM_Project",

    # RAG & Vector Search
    "05_RAG_Vector_Search/embeddings",
    "05_RAG_Vector_Search/document_chunking",
    "05_RAG_Vector_Search/vector_databases/Qdrant",
    "05_RAG_Vector_Search/vector_databases/Milvus",
    "05_RAG_Vector_Search/vector_databases/FAISS",
    "05_RAG_Vector_Search/vector_databases/pgvector",
    "05_RAG_Vector_Search/retrievers",
    "05_RAG_Vector_Search/rerankers",
    "05_RAG_Vector_Search/context_optimization",
    "05_RAG_Vector_Search/evaluation",
    "05_RAG_Vector_Search/RAG_Project",

    # MLOps & Deployment
    "06_MLOps_Deployment/fastapi",
    "06_MLOps_Deployment/docker",
    "06_MLOps_Deployment/kubernetes",
    "06_MLOps_Deployment/bentoML",
    "06_MLOps_Deployment/model_registry",
    "06_MLOps_Deployment/CI_CD",
    "06_MLOps_Deployment/monitoring",
    "06_MLOps_Deployment/batch_vs_real_time",
    "06_MLOps_Deployment/Deployment_Project",

    # AI System Design
    "07_System_Design_AI/ML_system_design",
    "07_System_Design_AI/case_studies",
    "07_System_Design_AI/scalability",
    "07_System_Design_AI/inference_at_scale",
    "07_System_Design_AI/distributed_training",
    "07_System_Design_AI/caching_batching",
    "07_System_Design_AI/architecture_diagrams",

    # Portfolio
    "08_Portfolio_Projects/docs",
    "08_Portfolio_Projects/demos_videos",
    "08_Portfolio_Projects/01_ML_Project",
    "08_Portfolio_Projects/02_DL_Project",
    "08_Portfolio_Projects/03_LLM_Fine_Tuning",
    "08_Portfolio_Projects/04_RAG_Search_System",
    "08_Portfolio_Projects/05_AI_Platform_or_Agent",

    # Interview
    "09_Interview_Preparation/ML_AI_interview",
    "09_Interview_Preparation/LLM_RAG_interview",
    "09_Interview_Preparation/system_design_interview",
    "09_Interview_Preparation/coding_round",
    "09_Interview_Preparation/mock_interviews",
    "09_Interview_Preparation/resume_review",
    "09_Interview_Preparation/STAR_story_bank",

    # Docs
    "10_Documents_and_Planning/roadmap",
    "10_Documents_and_Planning/daily_weekly_planner",
    "10_Documents_and_Planning/certificates",
    "10_Documents_and_Planning/notes",
]

# step 1 — create parent folders first
for folder in top_level:
    os.makedirs(os.path.join(BASE, folder), exist_ok=True)

# step 2 — create the full hierarchy
for folder in folders:
    os.makedirs(os.path.join(BASE, folder), exist_ok=True)

# step 3 — add tracking files
for folder in track_files_dirs:
    for filename in ["README.md", "TODO.md", "LEARNED.md", "mistakes.md", "PROBLEMS.md"]:
        open(os.path.join(BASE, folder, filename), "a").close()

print("✔ All folders and tracking files created successfully!")
print("📁 Base Directory:", os.path.abspath(BASE))
